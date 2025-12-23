import streamlit as st
import ollama

st.set_page_config(
    page_title="PromptCraft AI",
    layout="centered"
)

st.title("PromptCraft AI")
st.caption("Local LLM • Prompt Engineering Playground")

st.sidebar.header("Settings")

model = st.sidebar.selectbox(
    "Choose Model",
    ["llama3", "mistral", "phi3"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.write("Type `exit` to clear conversation")

if "messages" not in st.session_state:
    st.session_state.messages = []


user_input = st.text_input("Ask something:")

send = st.button("Send")


if send:
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    elif user_input.lower() == "exit":
        st.session_state.messages = []
        st.success("Conversation cleared.")
    else:
        # Add user message
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        # Call Ollama
        with st.spinner("Thinking..."):
            response = ollama.chat(
                model=model,
                messages=st.session_state.messages
            )

        assistant_reply = response["message"]["content"]

        # Add assistant message
        st.session_state.messages.append({
            "role": "assistant",
            "content": assistant_reply
        })


for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**AI:** {msg['content']}")
