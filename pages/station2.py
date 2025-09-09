import streamlit as st
from datetime import datetime, timedelta
import time
import os
import socket
from typing import Optional, List

def find_free_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))  # Bind to a free port provided by the OS
    port = s.getsockname()[1]
    s.close()
    return port

# Set Streamlit to use a free port
os.environ["STREAMLIT_SERVER_PORT"] = str(find_free_port())

STATION_DATA = {
    "station_number": 2,
    "station_name": "Immunoglobulin Escape Room - Station 2",
    "groups": {
        "group1": {
            "name": "Group 1",
            "next_station": 3,
            "next_code": "ZY678",
            "is_final": False,
            "questions": [
                {
                    "question": "Is primary IG prophylaxis (before any infection if IgG level is low) recommended in haematological malignancies by existing guidelines?",
                    "options": [
                        "A) Yes, in specific cases like CAR-T therapy in children",
                        "B) No",
                        "C) Yes, in Canada only",
                        "D) Yes, but only for SCIG",
                        "E) Yes, but only for IVIG"
                    ],
                    "correct": "A"
                },
                {
                    "question": "Are there medical reasons to consider SCIG except of patient preferences?",
                    "options": [
                        "A) Yes, about 10-fold smaller frequency of systemic adverse reactions compare to IVIG",
                        "B) Yes, number of specific conditions such as hyperviscosity syndromes",
                        "C) All the above",
                        "D) None of the above",
                        "E) Answer A only"
                    ],
                    "correct": "C"
                },
                {
                    "question": "Which situation is a critical limitation for SCIG usage?",
                    "options": [
                        "A) High volume of subcutaneous fat",
                        "B) Low volume of subcutaneous fat",
                        "C) Thrombocytopenia",
                        "D) Anemia",
                        "E) Severe cognitive impairment without help from caregivers"
                    ],
                    "correct": "E"
                }
            ]
        },
        "group2": {
            "name": "Group 2",
            "next_station": 3,
            "next_code": "XW901",
            "is_final": False,
            "questions": [
                {
                    "question": "Is primary IG prophylaxis (before any infection if IgG level is low) recommended in haematological malignancies by existing guidelines?",
                    "options": [
                        "A) Yes, in specific cases like CAR-T therapy in children",
                        "B) No",
                        "C) Yes, in Canada only",
                        "D) Yes, but only for SCIG",
                        "E) Yes, but only for IVIG"
                    ],
                    "correct": "A"
                },
                {
                    "question": "Are there medical reasons to consider SCIG except of patient preferences?",
                    "options": [
                        "A) Yes, about 10-fold smaller frequency of systemic adverse reactions compare to IVIG",
                        "B) Yes, number of specific conditions such as hyperviscosity syndromes",
                        "C) All the above",
                        "D) None of the above",
                        "E) Answer A only"
                    ],
                    "correct": "C"
                },
                {
                    "question": "Which situation is a critical limitation for SCIG usage?",
                    "options": [
                        "A) High volume of subcutaneous fat",
                        "B) Low volume of subcutaneous fat",
                        "C) Thrombocytopenia",
                        "D) Anemia",
                        "E) Severe cognitive impairment without help from caregivers"
                    ],
                    "correct": "E"
                }
            ]
        },
        "group3": {
            "name": "Group 3",
            "next_station": None,
            "next_code": "IG3FINAL",
            "is_final": True,
            "questions": [
                {
                    "question": "Is primary IG prophylaxis (before any infection if IgG level is low) recommended in haematological malignancies by existing guidelines?",
                    "options": [
                        "A) Yes, in specific cases like CAR-T therapy in children",
                        "B) No",
                        "C) Yes, in Canada only",
                        "D) Yes, but only for SCIG",
                        "E) Yes, but only for IVIG"
                    ],
                    "correct": "A"
                },
                {
                    "question": "Are there medical reasons to consider SCIG except of patient preferences?",
                    "options": [
                        "A) Yes, about 10-fold smaller frequency of systemic adverse reactions compare to IVIG",
                        "B) Yes, number of specific conditions such as hyperviscosity syndromes",
                        "C) All the above",
                        "D) None of the above",
                        "E) Answer A only"
                    ],
                    "correct": "C"
                },
                {
                    "question": "Which situation is a critical limitation for SCIG usage?",
                    "options": [
                        "A) High volume of subcutaneous fat",
                        "B) Low volume of subcutaneous fat",
                        "C) Thrombocytopenia",
                        "D) Anemia",
                        "E) Severe cognitive impairment without help from caregivers"
                    ],
                    "correct": "E"
                }
            ]
        },
        "group4": {
            "name": "Group 4",
            "next_station": 3,
            "next_code": "TS567",
            "is_final": False,
            "questions": [
                {
                    "question": "Is primary IG prophylaxis (before any infection if IgG level is low) recommended in haematological malignancies by existing guidelines?",
                    "options": [
                        "A) Yes, in specific cases like CAR-T therapy in children",
                        "B) No",
                        "C) Yes, in Canada only",
                        "D) Yes, but only for SCIG",
                        "E) Yes, but only for IVIG"
                    ],
                    "correct": "A"
                },
                {
                    "question": "Are there medical reasons to consider SCIG except of patient preferences?",
                    "options": [
                        "A) Yes, about 10-fold smaller frequency of systemic adverse reactions compare to IVIG",
                        "B) Yes, number of specific conditions such as hyperviscosity syndromes",
                        "C) All the above",
                        "D) None of the above",
                        "E) Answer A only"
                    ],
                    "correct": "C"
                },
                {
                    "question": "Which situation is a critical limitation for SCIG usage?",
                    "options": [
                        "A) High volume of subcutaneous fat",
                        "B) Low volume of subcutaneous fat",
                        "C) Thrombocytopenia",
                        "D) Anemia",
                        "E) Severe cognitive impairment without help from caregivers"
                    ],
                    "correct": "E"
                }
            ]
        },
        "group5": {
            "name": "Group 5",
            "next_station": 3,
            "next_code": "RQ890",
            "is_final": False,
            "questions": [
                {
                    "question": "Is primary IG prophylaxis (before any infection if IgG level is low) recommended in haematological malignancies by existing guidelines?",
                    "options": [
                        "A) Yes, in specific cases like CAR-T therapy in children",
                        "B) No",
                        "C) Yes, in Canada only",
                        "D) Yes, but only for SCIG",
                        "E) Yes, but only for IVIG"
                    ],
                    "correct": "A"
                },
                {
                    "question": "Are there medical reasons to consider SCIG except of patient preferences?",
                    "options": [
                        "A) Yes, about 10-fold smaller frequency of systemic adverse reactions compare to IVIG",
                        "B) Yes, number of specific conditions such as hyperviscosity syndromes",
                        "C) All the above",
                        "D) None of the above",
                        "E) Answer A only"
                    ],
                    "correct": "C"
                },
                {
                    "question": "Which situation is a critical limitation for SCIG usage?",
                    "options": [
                        "A) High volume of subcutaneous fat",
                        "B) Low volume of subcutaneous fat",
                        "C) Thrombocytopenia",
                        "D) Anemia",
                        "E) Severe cognitive impairment without help from caregivers"
                    ],
                    "correct": "E"
                }
            ]
        },
        "group6": {
            "name": "Group 6",
            "next_station": 3,
            "next_code": "PO123",
            "is_final": False,
            "questions": [
                {
                    "question": "Is primary IG prophylaxis (before any infection if IgG level is low) recommended in haematological malignancies by existing guidelines?",
                    "options": [
                        "A) Yes, in specific cases like CAR-T therapy in children",
                        "B) No",
                        "C) Yes, in Canada only",
                        "D) Yes, but only for SCIG",
                        "E) Yes, but only for IVIG"
                    ],
                    "correct": "A"
                },
                {
                    "question": "Are there medical reasons to consider SCIG except of patient preferences?",
                    "options": [
                        "A) Yes, about 10-fold smaller frequency of systemic adverse reactions compare to IVIG",
                        "B) Yes, number of specific conditions such as hyperviscosity syndromes",
                        "C) All the above",
                        "D) None of the above",
                        "E) Answer A only"
                    ],
                    "correct": "C"
                },
                {
                    "question": "Which situation is a critical limitation for SCIG usage?",
                    "options": [
                        "A) High volume of subcutaneous fat",
                        "B) Low volume of subcutaneous fat",
                        "C) Thrombocytopenia",
                        "D) Anemia",
                        "E) Severe cognitive impairment without help from caregivers"
                    ],
                    "correct": "E"
                }
            ]
        },
        "group7": {
            "name": "Group 7",
            "next_station": 3,
            "next_code": "NM456",
            "is_final": False,
            "questions": [
                {
                    "question": "Is primary IG prophylaxis (before any infection if IgG level is low) recommended in haematological malignancies by existing guidelines?",
                    "options": [
                        "A) Yes, in specific cases like CAR-T therapy in children",
                        "B) No",
                        "C) Yes, in Canada only",
                        "D) Yes, but only for SCIG",
                        "E) Yes, but only for IVIG"
                    ],
                    "correct": "A"
                },
                {
                    "question": "Are there medical reasons to consider SCIG except of patient preferences?",
                    "options": [
                        "A) Yes, about 10-fold smaller frequency of systemic adverse reactions compare to IVIG",
                        "B) Yes, number of specific conditions such as hyperviscosity syndromes",
                        "C) All the above",
                        "D) None of the above",
                        "E) Answer A only"
                    ],
                    "correct": "C"
                },
                {
                    "question": "Which situation is a critical limitation for SCIG usage?",
                    "options": [
                        "A) High volume of subcutaneous fat",
                        "B) Low volume of subcutaneous fat",
                        "C) Thrombocytopenia",
                        "D) Anemia",
                        "E) Severe cognitive impairment without help from caregivers"
                    ],
                    "correct": "E"
                }
            ]
        }
    },
    "access_codes": {
        "LC567": "group1",
        "KJ890": "group2",
        "IH123": "group3",
        "GF456": "group4",
        "ED789": "group5",
        "CB012": "group6",
        "BA345": "group7"
    }
}

# Application configuration
st.set_page_config(
    page_title=f"🧬 Escape room - {STATION_DATA['station_name']}",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for improved appearance
st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    h1, h2, h3 {
        color: #1E88E5;
    }
    .stButton button {
        background-color: #1E88E5;
        color: white;
        border-radius: 5px;
        height: 3em;
        font-weight: bold;
    }
    .hint-box {
        background-color: #E3F2FD;
        border-left: 5px solid #1E88E5;
        padding: 15px;
        margin: 15px 0;
        border-radius: 5px;
    }
    .answer-box {
        background-color: #E8F5E9;
        border-left: 5px solid #4CAF50;
        padding: 15px;
        margin: 15px 0;
        border-radius: 5px;
    }
    .timeout-box {
        background-color: #FFEBEE;
        border-left: 5px solid #F44336;
        padding: 20px;
        margin-bottom: 20px;
    }
    .success-box {
        background-color: #E8F5E9;
        border-left: 5px solid #4CAF50;
        padding: 20px;
        margin-bottom: 20px;
    }
    .question-box {
        background-color: #F5F5F5;
        border-radius: 5px;
        padding: 15px;
        margin-bottom: 15px;
    }
    .code-format {
        font-family: monospace;
        font-size: 1.2em;
        letter-spacing: 2px;
        background-color: #F5F5F5;
        padding: 5px 10px;
        border-radius: 4px;
        border: 1px solid #DDD;
    }
    .timer-display {
        color: #F44336;
        font-weight: bold;
        margin-top: 8px;
        font-size: 1.1em;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Session and penalty helpers
# ---------------------------

def initialize_session():
    """Initialize session variables"""
    defaults = {
        'group_id': None,
        'group_name': None,
        'start_time': None,

        # Penalty model
        'penalty_end_time': None,
        'total_penalties': 0,
        'penalty_triggered': False,

        # Help usage counters (for button label)
        'hint_count': 0,
        'answer_count': 0,

        # Previous input
        'last_code_attempt': "",
        'access_code': "",

        # One-shot banners (TTL)
        'hint_until': None,
        'answer_until': None,
        'hint_text': "",
        'answer_text': "",
        
        # For progressive answer reveals
        'revealed_answers': set(),

        'quiz_completed': False,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def is_penalty_active():
    """Check if penalty is active"""
    end = st.session_state.penalty_end_time
    if end is None:
        return False
    return datetime.now() < end


def get_penalty_remaining():
    """Get remaining penalty time in seconds"""
    if not is_penalty_active():
        return 0
    return max(0, int((st.session_state.penalty_end_time - datetime.now()).total_seconds()))


def add_penalty_cooldown(seconds: int):
    """
    Adds a fixed penalty amount, cumulatively.
    If a penalty is already active, extend from its end.
    """
    now = datetime.now()
    st.session_state.total_penalties += seconds

    if st.session_state.penalty_end_time is None or now >= st.session_state.penalty_end_time:
        st.session_state.penalty_end_time = now + timedelta(seconds=seconds)
    else:
        current_remaining = (st.session_state.penalty_end_time - now).total_seconds()
        new_total = current_remaining + seconds
        st.session_state.penalty_end_time = now + timedelta(seconds=new_total)

    # signal input reset
    st.session_state.penalty_triggered = True


# ---------------------------
# Quiz helpers
# ---------------------------

def get_all_wrong_positions(code_attempt: str, correct_answers: List[str]) -> List[int]:
    """Returns list of 0-based indices of ALL wrong positions"""
    if not code_attempt:
        return []
    
    code_upper = code_attempt.upper()
    wrong_positions = []
    
    for i in range(min(len(code_upper), len(correct_answers))):
        if code_upper[i] != correct_answers[i]:
            wrong_positions.append(i)
    
    return wrong_positions


def get_next_unrevealed_wrong_position(code_attempt: str, correct_answers: List[str]) -> Optional[int]:
    """Returns 0-based index of next wrong position that hasn't been revealed yet"""
    if not code_attempt:
        return None
    
    wrong_positions = get_all_wrong_positions(code_attempt, correct_answers)
    
    # Convert revealed_answers to set if it's not already
    if not isinstance(st.session_state.revealed_answers, set):
        st.session_state.revealed_answers = set(st.session_state.revealed_answers)
    
    # Find first wrong position that hasn't been revealed yet
    for pos in wrong_positions:
        if pos not in st.session_state.revealed_answers:
            return pos
    
    return None


def show_welcome():
    """Display welcome screen"""
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/4335/4335164.png", width=150)

    st.markdown(f"## 👋 Welcome to {STATION_DATA['station_name']}")
    st.markdown("""
    Here we will play escape room quiz. The rules are simple:

    1. 📝 Answer all questions and write down your answers
    2. 🔑 Convert your answers into a **code** (e.g. ABC)
    3. ✅ Enter the code to proceed to the next station
    4. 💡 You can use help, but it comes with **time penalties**
    """)

    st.markdown("### 🔑 Enter access code to begin")
    st.markdown("Code format: <span class='code-format'>XY123</span> (2 letters + 3 digits)", unsafe_allow_html=True)


# ---------------------------
# Main
# ---------------------------

def main():
    station_data = STATION_DATA
    initialize_session()

    station_number = station_data["station_number"]
    station_name = station_data["station_name"]

    # Access gate
    if st.session_state.group_id is None:
        show_welcome()

        col1, col2 = st.columns([3, 1])
        with col1:
            access_code = st.text_input(
                "📝 Access code:",
                value=st.session_state.access_code,
                key="access_code_input",
                placeholder="Format: XY123 (e.g. AB123)"
            )

        with col2:
            start_btn = st.button("🚀 Start", use_container_width=True)

        if start_btn:
            st.session_state.access_code = access_code
            code_upper = access_code.strip().upper()

            access_code_match = None
            for stored_code, group in station_data["access_codes"].items():
                if stored_code.strip().upper() == code_upper:
                    access_code_match = stored_code
                    break

            if access_code_match:
                group_id = station_data["access_codes"][access_code_match]
                group_data = station_data["groups"][group_id]

                st.session_state.group_id = group_id
                st.session_state.group_name = group_data["name"]
                st.session_state.start_time = datetime.now()
                st.session_state.questions = group_data["questions"]
                st.session_state.next_station = group_data["next_station"]
                st.session_state.next_code = group_data["next_code"]
                st.session_state.is_final = group_data["is_final"]

                st.success(f"✅ Welcome, {group_data['name']}!")
                st.rerun()
            else:
                st.error("❌ Invalid access code!")
        return

    # Group data
    group_id = st.session_state.group_id
    group_data = station_data["groups"][group_id]
    group_name = group_data["name"]
    questions = st.session_state.questions
    next_station = st.session_state.next_station
    next_code = st.session_state.next_code
    is_final = st.session_state.is_final

    # Title
    st.title(f"🧬 {station_name}")
    st.subheader(f"👥 {group_name}")

    if st.session_state.total_penalties > 0:
        st.metric("⚠️ Total penalties", f"+{st.session_state.total_penalties}s")

    # Quiz body
    if not st.session_state.quiz_completed:
        st.markdown(f"### 📋 Questions")

        correct_answers = [q["correct"] for q in questions]
        correct_code = "".join(correct_answers)

        # Render questions (no radios)
        for i, q in enumerate(questions):
            st.markdown(f'<div class="question-box">', unsafe_allow_html=True)
            st.markdown(f"#### 🔢 Question {i+1}")
            st.write(q["question"])
            for option in q["options"]:
                st.write(f"   {option}")
            st.markdown('</div>', unsafe_allow_html=True)

        # Check penalty status
        penalty_active = is_penalty_active()
        penalty_remaining = get_penalty_remaining()

        # Verification
        st.markdown("### 🎯 Verification and moving to next station")

        col1, col2, col3 = st.columns([2, 1, 1])

        with col1:
            # Reset input value when a new penalty starts
            input_value = ""
            if penalty_active:
                if st.session_state.penalty_triggered:
                    st.session_state.penalty_triggered = False
                    input_value = ""
                else:
                    input_value = st.session_state.last_code_attempt

                verification_code = st.text_input(
                    "🔑 Code:",
                    disabled=True,
                    value=input_value,
                    key="code_input",
                    help="🚫 Blocked due to penalty"
                )
            else:
                verification_code = st.text_input(
                    "🔑 Enter code:",
                    placeholder="Three letters (e.g. ABC)",
                    max_chars=3,
                    key="code_input"
                )

        with col2:
            # FIXED TIMER - show countdown directly in this column
            if penalty_active:
                st.markdown(f'<div class="timer-display">⛔ {penalty_remaining}s</div>', unsafe_allow_html=True)
                progress = 1 - (penalty_remaining / 60) if penalty_remaining <= 60 else 0
                st.progress(max(0, progress))

        with col3:
            if penalty_active:
                st.button("✅ Verify code", disabled=True)
            else:
                if st.button("✅ Verify code", use_container_width=True):
                    st.session_state.last_code_attempt = verification_code

                    if verification_code.upper() == correct_code:
                        st.balloons()
                        st.markdown('<div class="success-box">', unsafe_allow_html=True)

                        if is_final:
                            st.success("🎉 CONGRATULATIONS! You've completed all stations!")
                            st.markdown("### 🏆 Your completion code:")
                            st.markdown(f"<span class='code-format'>{next_code}</span>", unsafe_allow_html=True)
                            st.markdown("Please enter this code into the central computer.")
                        else:
                            st.success("🎉 SUCCESS! You're moving to the next station!")
                            st.markdown("### 🗺️ Continue to the next station:")
                            st.markdown(f"Next station: **{next_station}**")
                            st.markdown(f"Code for next station: <span class='code-format'>{next_code}</span>", unsafe_allow_html=True)

                        st.markdown('</div>', unsafe_allow_html=True)
                        st.session_state.quiz_completed = True
                        return
                    else:
                        st.error("❌ Incorrect code!")
                        add_penalty_cooldown(30)  # fixed 30s penalty for wrong code
                        st.warning("⚠️ +30s penalty!")

        # Help section - ALWAYS AVAILABLE
        st.markdown("### 🆘 Help")
        
        if penalty_active:
            st.info("ℹ️ Help functions are available even during penalty time")

        help_col1, help_col2 = st.columns(2)

        with help_col1:
            hint_button_text = f"💡 Show incorrect questions (+30s)"
            if st.session_state.hint_count > 0:
                hint_button_text += f" [{st.session_state.hint_count}x]"

            # Help buttons are NEVER disabled
            if st.button(hint_button_text, use_container_width=True, key="hint_btn"):
                # Fixed +30s penalty, cumulative if active
                add_penalty_cooldown(30)
                st.session_state.hint_count += 1

                # Get current code input
                current_code_input = verification_code if verification_code else ""
                wrong_positions = get_all_wrong_positions(current_code_input, correct_answers)
                
                if not current_code_input:
                    hint_text = "Please enter a code first to analyze"
                elif not wrong_positions:
                    hint_text = "All entered answers are correct!"
                elif len(wrong_positions) == 1:
                    hint_text = f"Question {wrong_positions[0] + 1} is incorrect"
                else:
                    position_list = ", ".join([str(pos + 1) for pos in wrong_positions])
                    hint_text = f"Questions {position_list} are incorrect"

                st.session_state.hint_text = hint_text
                st.session_state.hint_until = datetime.now() + timedelta(seconds=30)

        with help_col2:
            answer_button_text = f"🎯 Reveal correct answer (+60s)"
            if st.session_state.answer_count > 0:
                answer_button_text += f" [{st.session_state.answer_count}x]"

            # Help buttons are NEVER disabled
            if st.button(answer_button_text, use_container_width=True, key="answer_btn"):
                # Fixed +60s penalty, cumulative if active
                add_penalty_cooldown(60)
                st.session_state.answer_count += 1

                # Get current code input
                current_code_input = verification_code if verification_code else ""
                next_wrong_idx = get_next_unrevealed_wrong_position(current_code_input, correct_answers)
                
                if not current_code_input:
                    ans_text = "Please enter a code first to get answers"
                elif next_wrong_idx is None:
                    # Check if there are any wrong positions at all
                    all_wrong = get_all_wrong_positions(current_code_input, correct_answers)
                    if not all_wrong:
                        ans_text = "All entered answers are already correct!"
                    else:
                        ans_text = "All incorrect answers have been revealed"
                else:
                    # Add this position to revealed set
                    st.session_state.revealed_answers.add(next_wrong_idx)
                    ans_text = f"Question {next_wrong_idx + 1}: Correct answer is {correct_answers[next_wrong_idx]}"

                st.session_state.answer_text = ans_text
                st.session_state.answer_until = datetime.now() + timedelta(seconds=30)

        # BANNERS DIRECTLY BELOW HELP BUTTONS
        now = datetime.now()

        # Hint banner
        if (st.session_state.hint_until and 
            isinstance(st.session_state.hint_until, datetime) and 
            now < st.session_state.hint_until and 
            st.session_state.hint_text):
            
            st.markdown('<div class="hint-box">', unsafe_allow_html=True)
            st.info(f"💡 **Hint:** {st.session_state.hint_text}")
            st.markdown('</div>', unsafe_allow_html=True)

        # Answer banner
        if (st.session_state.answer_until and 
            isinstance(st.session_state.answer_until, datetime) and 
            now < st.session_state.answer_until and 
            st.session_state.answer_text):
            
            st.markdown('<div class="answer-box">', unsafe_allow_html=True)
            st.success(f"🎯 **Answer:** {st.session_state.answer_text}")
            st.markdown('</div>', unsafe_allow_html=True)

    # SIMPLE AUTO-REFRESH for timer - only when penalty is active and quiz not completed
    if not st.session_state.quiz_completed and is_penalty_active():
        # Auto-refresh every 1 second to update countdown
        time.sleep(1)
        st.rerun()


if __name__ == "__main__":
    main()
