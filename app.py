import os
import streamlit as st
import psycopg2
import pandas as pd

st.set_page_config(page_title="Quiz App", page_icon="🧠")

# Uzimamo DATABASE_URL iz Streamlit Secrets ili env
DATABASE_URL = st.secrets.get("DATABASE_URL") or os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    st.error("DATABASE_URL nije postavljen (dodaj ga u Secrets na Streamlit Cloud).")
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

col1, col2 = st.columns(2)
with col1:
    if st.button("Test konekcije"):
        try:
            df = run_query("select now() as server_time")
            st.success(f"Konekcija OK. Server time: {df['server_time'][0]}")
        except Exception as e:
            st.error(f"Greška: {e}")

with col2:
    if st.button("Broj public tabela"):
        try:
            df = run_query("select count(*) as cnt from pg_catalog.pg_tables where schemaname='public'")
            st.info(f"Broj public tabela: {df['cnt'][0]}")
        except Exception as e:
            st.error(f"Greška: {e}")

st.markdown("---")
st.subheader("Tabela pitanja (primjer)")

TABLE_NAME = "quiz_questions"

if st.button("Prvih 20 pitanja"):
    try:
        dfq = run_query(f"select * from {TABLE_NAME} limit 20")
        if dfq is None or dfq.empty:
            st.warning("Tabela ne postoji ili nema redova.")
        else:
            st.dataframe(dfq)
    except Exception as e:
        st.error(f"Ne mogu čitati {TABLE_NAME}: {e}")

st.caption("Sve radi online. Poslije dodajemo formu za unos pitanja.")
