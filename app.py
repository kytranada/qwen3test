import streamlit as st
from ollama_client import query_model
from prompts import PREDEFINED_PROMPTS
import time

st.set_page_config(page_title="Qwen3-Coder Benchmark", layout="wide")

st.title("🧠 Qwen3-Coder Benchmark (Sequential Mode)")
st.caption("Run each model one at a time to avoid RAM issues")

# Init session state
if "prompt" not in st.session_state:
    st.session_state.prompt = ""
    st.session_state.responses = {"q8": None, "full": None}
    st.session_state.timers = {"q8": None, "full": None}

# Sidebar: Prompt Selection
with st.sidebar:
    st.header("⚙️ Choose Prompt and Model")
    selected_prompt = st.selectbox("Prompt", list(PREDEFINED_PROMPTS.keys()) + ["Custom input"])
    if selected_prompt == "Custom input":
        st.session_state.prompt = st.text_area("Enter custom prompt")
    else:
        st.session_state.prompt = PREDEFINED_PROMPTS[selected_prompt]

    st.markdown("## Run one model at a time")
    model_choice = st.radio("Select model to run", ["qwen3-coder:30b-a3b-q8_0", "qwen3-coder:30b"])

    if st.button("Run selected model"):
        model_key = "q8" if "q8" in model_choice else "full"
        with st.spinner(f"Running {model_choice}..."):
            start = time.time()
            result = query_model(model_choice, st.session_state.prompt)
            elapsed = time.time() - start
            st.session_state.responses[model_key] = result
            st.session_state.timers[model_key] = elapsed
        st.success(f"{model_choice} completed in {elapsed:.2f} seconds")

# Main Display: Side-by-side if both are available
if st.session_state.responses["q8"] or st.session_state.responses["full"]:
    st.subheader("🧪 Model Comparison")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🧠 `qwen3-coder:30b-a3b-q8_0`")
        if st.session_state.responses["q8"]:
            st.code(st.session_state.responses["q8"], language="markdown")
            st.success(f"Time: {st.session_state.timers['q8']:.2f}s")
        else:
            st.info("Not yet run")

    with col2:
        st.markdown("### 🧠 `qwen3-coder:30b`")
        if st.session_state.responses["full"]:
            st.code(st.session_state.responses["full"], language="markdown")
            st.success(f"Time: {st.session_state.timers['full']:.2f}s")
        else:
            st.info("Not yet run")
