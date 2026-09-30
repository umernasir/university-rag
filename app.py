import streamlit as st
import requests

st.title("University AI Assistant")
question=st.text_input("Ask your question")
if st.button("Ask"):
    if question:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/ask",
                json={"question": question}
            )
            response.raise_for_status()
            data = response.json()
            st.subheader("Answer")
            st.write(data["answer"])
            st.subheader("Sources")
            for i in data["sources"]:
                st.write("•", i)
        except requests.exceptions.RequestException:
            st.error("Could not connect to the server.")
    else:
        st.warning("Please enter the question.")