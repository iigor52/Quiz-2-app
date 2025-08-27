        if submit_answer:
            is_correct = user_answer.strip().lower() == str(correct_answer).strip().lower()
            if is_correct:
                st.session_state.score += 1
                st.success("Tačno ✅")
            else:
                st.error(f"Netačno ❌ (Tačan odgovor: {correct_answer})")

            # Snimi odgovor
            run_query(
                "insert into quiz_attempt_answers (attempt_id, question_id, given_answer, is_correct) values (%s, %s, %s, %s)",
                (st.session_state.attempt_id, q_id, user_answer.strip(), is_correct),
                fetch=False
            )

            st.session_state.answers.append({
                "question_id": q_id,
                "given_answer": user_answer.strip(),
                "is_correct": is_correct
            })

            # Pređi na sljedeće
            st.session_state.current_index += 1
            if st.session_state.current_index >= len(st.session_state.question_ids):
                # Završavamo kviz
                finish_quiz()
                # Nema potrebe za rerun odmah; korisniku već prikazujemo rezultat.
                st.stop()
            else:
                # Rerun za prikaz sljedećeg pitanja
                st.rerun()
