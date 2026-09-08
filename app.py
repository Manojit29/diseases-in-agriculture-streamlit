import streamlit as st
import time
from questions import UNIT_DATA

st.set_page_config(page_title="Diseases in Agriculture", page_icon="🌱", layout="wide")

# ---------- State ----------
DEFAULTS = {
    "unit_idx": 0,
    "stage": "study",
    "mcq_answers": {},
    "mcq_score": None,
    "written_started": None,
    "written_expired": False,
    "transition_started": None,
}
for k, v in DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v

def reset_mcq():
    st.session_state.mcq_answers = {}
    st.session_state.mcq_score = None

def go_stage(stage):
    st.session_state.stage = stage
    st.rerun()

def start_transition():
    st.session_state.transition_started = time.time()
    st.session_state.stage = "transition"
    st.rerun()

def next_unit():
    if st.session_state.unit_idx < len(UNIT_DATA) - 1:
        st.session_state.unit_idx += 1
        st.session_state.stage = "study"
        reset_mcq()
        st.session_state.written_started = None
        st.session_state.written_expired = False
        st.session_state.transition_started = None
        st.rerun()
    else:
        st.session_state.stage = "finished"
        st.rerun()

def start_written():
    st.session_state.written_started = time.time()
    st.session_state.written_expired = False
    go_stage("written")

# ---------- Sidebar ----------
st.sidebar.title("🌱 Course Navigation")
for i, unit in enumerate(UNIT_DATA):
    label = f"Unit {i+1}: {unit['crop']}"
    if st.sidebar.button(label, key=f"unit_{i}", use_container_width=True):
        st.session_state.unit_idx = i
        st.session_state.stage = "study"
        reset_mcq()
        st.session_state.written_started = None
        st.session_state.written_expired = False
        st.session_state.transition_started = None
        st.rerun()

st.sidebar.divider()
st.sidebar.caption("7 units • 14 diseases • 10 MCQs + written test per unit")

unit = UNIT_DATA[st.session_state.unit_idx]

# ---------- Header ----------
st.title("🌱 Diseases in Agriculture")
st.caption("Study → MCQ Test → Result → 30-minute Written Test")
st.progress((st.session_state.unit_idx + 1) / len(UNIT_DATA),
            text=f"Unit {st.session_state.unit_idx + 1} of {len(UNIT_DATA)}")

st.subheader(f"Unit {st.session_state.unit_idx + 1}: {unit['crop']}")
st.write("**Diseases:** " + " • ".join(unit["diseases"]))

# ---------- Study ----------
if st.session_state.stage == "study":
    st.info("Study this unit carefully. When ready, start the 10-question MCQ test.")

    for disease in unit["content"]:
        with st.expander(disease["title"], expanded=False):
            for section, body in disease["sections"].items():
                st.markdown(f"### {section}")
                if isinstance(body, list):
                    for item in body:
                        st.markdown(f"- {item}")
                else:
                    st.write(body)

    st.divider()
    if st.button("✅ I'm ready for the MCQ test", type="primary", use_container_width=True):
        reset_mcq()
        go_stage("mcq")

# ---------- MCQ ----------
elif st.session_state.stage == "mcq":
    st.info("Answer all 10 questions, then submit your test.")

    with st.form("mcq_form"):
        for i, q in enumerate(unit["mcqs"]):
            st.markdown(f"**Q{i+1}. {q['question']}**")
            choice = st.radio(
                "Select one:",
                q["options"],
                key=f"mcq_{st.session_state.unit_idx}_{i}",
                index=None,
                label_visibility="collapsed",
            )
            st.session_state.mcq_answers[i] = choice

        submitted = st.form_submit_button("📝 Submit MCQ", type="primary",
                                           use_container_width=True)

    if submitted:
        unanswered = [i+1 for i, a in st.session_state.mcq_answers.items() if a is None]
        if unanswered:
            st.warning("Please answer all questions. Unanswered: " +
                       ", ".join(map(str, unanswered)))
        else:
            st.session_state.mcq_score = sum(
                st.session_state.mcq_answers[i] == q["answer"]
                for i, q in enumerate(unit["mcqs"])
            )
            go_stage("mcq_result")

# ---------- MCQ Result ----------
elif st.session_state.stage == "mcq_result":
    score = st.session_state.mcq_score
    st.success(f"MCQ Score: **{score}/10**")

    pct = score * 10
    if pct >= 80:
        st.balloons()
        st.write("🎉 Excellent!")
    elif pct >= 60:
        st.write("👍 Good job. Review the incorrect answers.")
    else:
        st.write("📚 Review the study material before continuing.")

    for i, q in enumerate(unit["mcqs"]):
        selected = st.session_state.mcq_answers.get(i)
        correct = selected == q["answer"]
        icon = "✅" if correct else "❌"
        with st.expander(f"{icon} Q{i+1}: {q['question']}"):
            st.write(f"**Your answer:** {selected}")
            st.write(f"**Correct answer:** {q['answer']}")
            st.write(f"**Explanation:** {q['explanation']}")

    st.divider()
    if st.button("✍️ Start 30-minute Written Test", type="primary",
                 use_container_width=True):
        start_written()

# ---------- Written ----------
elif st.session_state.stage == "written":
    LIMIT = 30 * 60
    elapsed = time.time() - st.session_state.written_started
    remaining = max(0, int(LIMIT - elapsed))

    if remaining <= 0:
        st.session_state.written_expired = True
        start_transition()

    mins, secs = divmod(remaining, 60)
    st.markdown(
        f"""<div style="padding:14px;border:2px solid #d33;border-radius:10px;
        text-align:center;font-size:28px;font-weight:700;">
        ⏱️ Time Remaining: {mins:02d}:{secs:02d}
        </div>""",
        unsafe_allow_html=True,
    )
    st.caption("Write your answers on paper. Do not enter the answers into Streamlit.")
    st.warning("When the timer reaches 00:00, the written questions will be locked.")

    st.divider()
    st.markdown("## Part A — 5 × 2 marks")
    for i, q in enumerate(unit["written_short"]):
        st.markdown(f"**{i+1}. {q}**")
        st.write("")

    st.divider()
    st.markdown("## Part B — 1 × 5 marks")
    st.markdown(f"**{unit['written_long']}**")
    st.write("")

    st.divider()
    if st.button("🛑 Finish Written Test", type="primary", use_container_width=True):
        start_transition()

    time.sleep(1)
    st.rerun()

# ---------- 30-second transition ----------
elif st.session_state.stage == "transition":
    TRANSITION_SECONDS = 30
    elapsed = time.time() - st.session_state.transition_started
    remaining = max(0, int(TRANSITION_SECONDS - elapsed))

    st.markdown(
        """
        <div style="
            min-height: 55vh;
            display:flex;
            flex-direction:column;
            justify-content:center;
            align-items:center;
            text-align:center;
        ">
            <div style="font-size:22px; margin-bottom:25px;">
                🌱 Unit completed
            </div>
            <div style="
                max-width:900px;
                font-size:30px;
                line-height:1.5;
                font-weight:600;
                margin-bottom:25px;
            ">
                "I am grateful to you for chatting to ordinary people like us."
            </div>
            <div style="font-size:22px;">
                Next unit starts automatically in
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div style="text-align:center;font-size:48px;font-weight:700;">
            {remaining:02d}
        </div>
        """,
        unsafe_allow_html=True,
    )

    if remaining <= 0:
        next_unit()

    time.sleep(1)
    st.rerun()

# ---------- Timer expired ----------
elif st.session_state.stage == "written_expired":

    st.error("⏰ TIME'S UP!")
    st.markdown("### Please stop writing.")
    st.write("Your 30-minute written-test period has ended.")
    st.divider()
    if st.session_state.unit_idx < len(UNIT_DATA) - 1:
        if st.button("➡️ Start Next Unit", type="primary", use_container_width=True):
            next_unit()
        if st.button("🔄 Review This Unit", use_container_width=True):
            st.session_state.stage = "study"
            st.rerun()
    else:
        if st.button("🏁 Finish Course", type="primary", use_container_width=True):
            st.session_state.stage = "finished"
            st.rerun()

# ---------- Written complete ----------
elif st.session_state.stage == "written_complete":
    start_transition()

# ---------- Finished ----------
elif st.session_state.stage == "finished":
    st.balloons()
    st.success("🎓 Course completed!")
    st.markdown("## Congratulations!")
    st.write("You completed all 7 crop units.")
    st.write("Review your written answers and revise any weak areas before the exam.")
    if st.button("🔁 Restart Course", type="primary", use_container_width=True):
        for k, v in DEFAULTS.items():
            st.session_state[k] = v
        st.rerun()
