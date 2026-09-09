# app.py
import time
import random
import streamlit as st
from question import DISEASES

st.set_page_config(page_title="Diseases in Agriculture", page_icon="🌱", layout="wide")

# ---------- Data Processing & Unit Generation ----------
@st.cache_data
def build_unit_data(diseases_list):
    """
    Groups diseases by crop and builds structured units containing study content,
    auto-generated MCQs, and written questions.
    """
    crop_groups = {}
    for d in diseases_list:
        crop = d["crop"]
        if crop not in crop_groups:
            crop_groups[crop] = []
        crop_groups[crop].append(d)

    units = []
    for crop, items in crop_groups.items():
        disease_names = [d["disease_name"] for d in items]
        
        # Build Study Content
        content = []
        for d in items:
            taxonomy_str = ""
            if d.get("taxonomic_classification"):
                taxonomy_str = "\n".join([f"- **{k}**: {v}" for k, v in d["taxonomic_classification"].items()])
            else:
                taxonomy_str = "Not Applicable (Physiological Disorder)"

            sections = {
                "Causative Organism": d["causative_organism"],
                "Taxonomic Classification": taxonomy_str,
                "Symptoms": d["symptoms"],
                "Disease Cycle": d["disease_cycle"],
                "Epidemiology": d["epidemiology"],
                "Management Options": [
                    f"**Cultural**: {d['management']['cultural']}",
                    f"**Host Resistance**: {d['management']['host_resistance']}",
                    f"**Chemical**: {d['management']['chemical']}",
                    f"**Biological**: {d['management']['biological']}"
                ]
            }
            content.append({
                "title": f"{d['disease_name']} ({d['causative_organism']})",
                "sections": sections
            })

        # Generate 10 MCQs per Unit
        mcqs = []
        # Question pool generator based on dataset fields
        for d in items:
            # Q: Causative Organism
            mcqs.append({
                "question": f"What is the causative organism of {d['disease_name']} in {crop}?",
                "options": [d["causative_organism"], "Puccinia graminis", "Xanthomonas citri", "Fusarium oxysporum"],
                "answer": d["causative_organism"],
                "explanation": f"The causative agent for {d['disease_name']} is {d['causative_organism']}."
            })
            # Q: Management
            mcqs.append({
                "question": f"Which chemical management strategy is recommended for {d['disease_name']}?",
                "options": [d["management"]["chemical"], "Spray Streptomycin only", "Apply Urea in high doses", "No chemical controls exist"],
                "answer": d["management"]["chemical"],
                "explanation": f"Recommended chemical control: {d['management']['chemical']}"
            })
            # Q: Epidemiology
            mcqs.append({
                "question": f"Which environmental conditions favor {d['disease_name']}?",
                "options": [d["epidemiology"], "Freezing temperatures below 0°C", "Arid desert climate with 0% humidity", "High soil salinity only"],
                "answer": d["epidemiology"],
                "explanation": f"Epidemiological requirement: {d['epidemiology']}"
            })

        # Shuffle options for every MCQ to randomize
        for q in mcqs:
            opts = list(q["options"])
            random.seed(len(q["question"])) # Deterministic shuffle
            random.shuffle(opts)
            q["options"] = opts

        # Ensure exactly 10 MCQs per unit
        while len(mcqs) < 10:
            mcqs.append(mcqs[len(mcqs) % len(items)])
        mcqs = mcqs[:10]

        # Generate Written Test Questions
        written_short = [
            f"State the primary symptoms of {items[0]['disease_name']}.",
            f"Describe the favorable epidemiological conditions for {items[0]['disease_name']}.",
            f"What are the key cultural management practices for {items[-1]['disease_name']}?",
            f"Name the causative agent and vector (if any) for {items[-1]['disease_name']}.",
            f"Outline the biological control measures applicable to diseases of {crop}."
        ]
        
        written_long = (
            f"Provide a comprehensive overview of {items[0]['disease_name']} in {crop}. "
            f"Discuss its causative organism, disease cycle, characteristic symptoms, "
            f"and an integrated disease management (IDM) strategy."
        )

        units.append({
            "crop": crop,
            "diseases": disease_names,
            "content": content,
            "mcqs": mcqs,
            "written_short": written_short,
            "written_long": written_long
        })
        
    return units

UNIT_DATA = build_unit_data(DISEASES)

# ---------- State Initialization ----------
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
st.sidebar.caption(f"{len(UNIT_DATA)} units • {len(DISEASES)} diseases • 10 MCQs + written test per unit")

unit = UNIT_DATA[st.session_state.unit_idx]

# ---------- Header ----------
st.title("🌱 Diseases in Agriculture")
st.caption("Study → MCQ Test → Result → 30-minute Written Test")
st.progress((st.session_state.unit_idx + 1) / len(UNIT_DATA),
            text=f"Unit {st.session_state.unit_idx + 1} of {len(UNIT_DATA)}")

st.subheader(f"Unit {st.session_state.unit_idx + 1}: {unit['crop']}")
st.write("**Diseases:** " + " • ".join(unit["diseases"]))

# ---------- Study Stage ----------
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

# ---------- MCQ Stage ----------
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

        submitted = st.form_submit_button("📝 Submit MCQ", type="primary", use_container_width=True)

    if submitted:
        unanswered = [i+1 for i, a in st.session_state.mcq_answers.items() if a is None]
        if unanswered:
            st.warning("Please answer all questions. Unanswered: " + ", ".join(map(str, unanswered)))
        else:
            st.session_state.mcq_score = sum(
                st.session_state.mcq_answers[i] == q["answer"]
                for i, q in enumerate(unit["mcqs"])
            )
            go_stage("mcq_result")

# ---------- MCQ Result Stage ----------
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
    if st.button("✍️ Start 30-minute Written Test", type="primary", use_container_width=True):
        start_written()

# ---------- Written Test Stage ----------
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

# ---------- 30-Second Transition Stage ----------
# ---------- 30-second transition ----------
elif st.session_state.stage == "transition":
    TRANSITION_SECONDS = 30
    elapsed = time.time() - st.session_state.transition_started
    remaining = max(0, int(TRANSITION_SECONDS - elapsed))

    placeholder = st.empty()

    # Full-screen overlay hiding all default UI elements
    with placeholder.container():
        st.markdown(
            f"""
            <style>
                /* Hide sidebar, header, and footer */
                [data-testid="stSidebar"], 
                header, 
                footer {{
                    display: none !important;
                }}
                
                .stApp {{
                    margin: 0;
                    padding: 0;
                    background-color: #0e1117;
                }}
                
                .fullscreen-container {{
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100vw;
                    height: 100vh;
                    background-color: #0e1117;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    z-index: 999999;
                    padding: 40px;
                    box-sizing: border-box;
                }}
                
                .message-text {{
                    max-width: 850px;
                    font-size: 24px;
                    line-height: 1.6;
                    font-weight: 500;
                    color: #ffffff;
                    text-align: center;
                    margin-bottom: 35px;
                    font-family: 'Georgia', serif;
                }}
                
                .timer-text {{
                    font-size: 32px;
                    font-weight: 700;
                    color: #ff4b4b;
                    letter-spacing: 2px;
                }}
            </style>

            <div class="fullscreen-container">
                <div class="message-text">
                    "When we first connected, I honestly knew nothing about Kathak or classical dance. 
                    But as I began learning about what it truly takes—and understood the devotion, 
                    strength, and mastery behind performing with 200 Ghungroos—I gained immense respect 
                    for your art. Even a single second of your time is deeply valuable to me, and I feel 
                    truly honored to connect with someone of your dedication."
                </div>
                <div class="timer-text">
                    {remaining:02d}s
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    if remaining <= 0:
        placeholder.empty()
        next_unit()

    time.sleep(1)
    st.rerun()
# ---------- Timer Expired Stage ----------
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

# ---------- Course Finished Stage ----------
elif st.session_state.stage == "finished":
    st.balloons()
    st.success("🎓 Course completed!")
    st.markdown("## Congratulations!")
    st.write(f"You completed all {len(UNIT_DATA)} crop units.")
    st.write("Review your written answers and revise any weak areas before the exam.")
    if st.button("🔁 Restart Course", type="primary", use_container_width=True):
        for k, v in DEFAULTS.items():
            st.session_state[k] = v
        st.rerun()