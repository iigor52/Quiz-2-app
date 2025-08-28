import os
import random
from datetime import datetime
import streamlit as st
import psycopg2
import pandas as pd

VERSION = "1.0.0"

st.set_page_config(page_title="Quiz App", page_icon="🧠")

DATABASE_URL = st.secrets.get("DATABASE_URL") or os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    st.error("DATABASE_URL nije postavljen u Secrets.")
    st.stop()

@st.cache_resource
def get_conn():
    return psycopg2.connect(DATABASE_URL)

def run_query(sql, params=None, fetch=True):
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(sql, params)
        if fetch and cur.description:
            rows = cur.fetchall()
            cols = [d[0] for d in cur.description]
            return pd.DataFrame(rows, columns=cols)
        if not fetch:
            conn.commit()
    return None

st.title("Quiz / DB test")
st.caption(f"App version: {VERSION}")

# GORNJA TEST DUGMAD
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Test konekcije"):
        try:
            df = run_query("select now() as server_time")
            st.success(f"Konekcija OK. Server time: {df['server_time'][0]}")
        except Exception as e:
            st.exception(e)
with col2:
    if st.button("Broj public tabela"):
        try:
            df = run_query("select count(*) as cnt from pg_catalog.pg_tables where schemaname='public'")
            st.info(f"Public tabela: {df['cnt'][0]}")
        except Exception as e:
            st.exception(e)
with col3:
    if st.button("Reset session"):
        st.session_state.clear()
        st.success("Session state očišćen – osvježi stranicu.")
        st.stop()

st.markdown("---")
st.subheader("Tabela pitanja (primjer)")

if st.button("Prvih 20 pitanja"):
    try:
        dfq = run_query("select id, question_text, correct_answer, created_at from quiz_questions order by id asc limit 20")
        if dfq is None or dfq.empty:
            st.warning("Nema pitanja.")
        else:
            st.dataframe(dfq)
    except Exception as e:
        st.exception(e)

# FORMA ZA DODAVANJE PITANJA
st.markdown("---")
st.subheader("Dodaj novo pitanje")

with st.form("add_q"):
    q_text = st.text_area("Tekst pitanja")
    correct = st.text_input("Tačan odgovor")
    submitted = st.form_submit_button("Snimi pitanje")
    if submitted:
        if not q_text.strip() or not correct.strip():
            st.warning("Popuni oba polja.")
        else:
            try:
                run_query(
                    "insert into quiz_questions (question_text, correct_answer) values (%s, %s)",
                    (q_text.strip(), correct.strip()),
                    fetch=False
                )
                st.success("Pitanje dodano.")
            except Exception as e:
                st.exception(e)

if st.button("Osvježi listu pitanja"):
    try:
        df_all = run_query("select id, question_text, correct_answer, created_at from quiz_questions order by id desc limit 50")
        st.dataframe(df_all)
    except Exception as e:
        st.exception(e)

# KVIZ SEKCIJA
st.markdown("---")
st.subheader("Pokreni kviz")

# Inicijalizacija session state
defaults = {
    "quiz_active": False,
    "question_ids": [],
    "current_index": 0,
    "score": 0,
    "attempt_id": None,
}
for k, v in defaults.items():
    st.session_state.setdefault(k, v)

def start_quiz(num_questions: int, participant: str):
    try:
        df_ids = run_query("select id from quiz_questions")
    except Exception as e:
        st.exception(e)
        return
    if df_ids is None or df_ids.empty:
        st.warning("Nema pitanja u bazi.")
        return
    all_ids = df_ids["id"].tolist()
    random.shuffle(all_ids)
    chosen = all_ids[:num_questions]
    st.session_state.question_ids = chosen
    st.session_state.current_index = 0
    st.session_state.score = 0
    # attempt
    try:
        df_attempt = run_query(
            "insert into quiz_attempts (participant_id) values (%s) returning id",
            (participant,),
            fetch=True
        )
        st.session_state.attempt_id = int(df_attempt.iloc[0, 0])
        st.session_state.quiz_active = True
    except Exception as e:
        st.exception(e)

def finish_quiz():
    try:
        run_query(
            "update quiz_attempts set score=%s, finished_at=now() where id=%s",
            (st.session_state.score, st.session_state.attempt_id),
            fetch=False
        )
    except Exception as e:
        st.exception(e)
    st.success(f"Kviz završen. Score: {st.session_state.score}/{len(st.session_state.question_ids)}")
    st.session_state.quiz_active = False

with st.form("quiz_start_form", clear_on_submit=False):
    participant = st.text_input("Učesnik", value="anon")
    num_questions = st.number_input("Broj pitanja", min_value=1, max_value=50, value=3)
    start_btn = st.form_submit_button("Start kviz")
    if start_btn:
        start_quiz(int(num_questions), participant)

if st.session_state.quiz_active:
    idx = st.session_state.current_index
    if idx < len(st.session_state.question_ids):
        q_id = st.session_state.question_ids[idx]
        try:
            df_q = run_query("select question_text, correct_answer from quiz_questions where id=%s", (q_id,))
        except Exception as e:
            st.exception(e)
            st.stop()
        if df_q is None or df_q.empty:
            st.error("Pitanje nije pronađeno.")
            st.stop()
        question_text = df_q.iloc[0]["question_text"]
        correct_answer = df_q.iloc[0]["correct_answer"]

        st.write(f"Pitanje {idx+1}/{len(st.session_state.question_ids)}")
        st.info(question_text)

        with st.form("answer_form"):
            user_answer = st.text_input("Tvoj odgovor")
            submit_answer = st.form_submit_button("Pošalji odgovor")
            if submit_answer:
                is_correct = user_answer.strip().lower() == str(correct_answer).strip().lower()
                if is_correct:
                    st.session_state.score += 1
                    st.success("Tačno ✅")
                else:
                    st.error(f"Netačno ❌ (Tačan: {correct_answer})")
                # Snimi odgovor
                try:
                    run_query(
                        "insert into quiz_attempt_answers (attempt_id, question_id, given_answer, is_correct) values (%s, %s, %s, %s)",
                        (st.session_state.attempt_id, q_id, user_answer.strip(), is_correct),
                        fetch=False
                    )
                except Exception as e:
                    st.exception(e)

                st.session_state.current_index += 1
                if st.session_state.current_index >= len(st.session_state.question_ids):
                    finish_quiz()
                    st.stop()
                else:
                    st.rerun()

# LEADERBOARD
st.markdown("---")
st.subheader("Leaderboard")
try:
    df_lb = run_query("select * from quiz_leaderboard limit 50")
    if df_lb is not None and not df_lb.empty:
        st.dataframe(df_lb)
    else:
        st.caption("Još nema završenih pokušaja.")
except Exception as e:
    st.exception(e)

st.caption("Ako nešto ne radi, kopiraj gornju grešku i pošalji.")
