import streamlit as st

from email_analyzer import analyze_email
from url_analyzer import analyze_url
from risk_engine import calculate_score

st.title("PhishGuard")

email=st.text_area(
"Paste Email"
)

url=st.text_input(
"Paste URL"
)

if st.button("Analyze"):

    email_flags=analyze_email(email)

    url_flags=analyze_url(url)

    score=calculate_score(
        email_flags,
        url_flags
    )

    st.write("Threat Score:",score)

    st.write(email_flags)

    st.write(url_flags)