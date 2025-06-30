import streamlit as st
from chains.creative import creative_chain
from chains.reflective import reflective_chain
from chains.socratic import socratic_chain

st.set_page_config(page_title="ILL hepl you", page_icon="💡")
st.title("Your Writing Assistant")
st.markdown(
    "Feeling stuck? I'm here to gently nudge your creativity without taking over. "
    "*You do the writing, I'll do the unblocking*"
)

user_input = st.text_area("🧠 What are you stuck with?", placeholder="e.g., My plot twist feels flat...")

help_level = st.slider(
    "How stuck are you?",
    min_value=1,
    max_value=10,
    value=5,
    step=1,
    help="1 = I'm fine, just need a nudge · 10 = I’ve been staring at the blinking cursor for hours"
)

temp = round(help_level / 10, 2)


if st.button("🪄 hepl ples"):
    with st.spinner("Thinking..."):
        if help_level < 4:
            chain = socratic_chain(temp)
        elif help_level > 7:
            chain = creative_chain(temp)
        else:
            chain = reflective_chain(temp)

        response = chain.invoke({"block": user_input})
        st.markdown("### 🤖 Here's your 'gentle' push:")
        st.success(response)


hide_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_style, unsafe_allow_html=True)
