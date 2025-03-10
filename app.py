import streamlit as st
import re
import string 
import random

st.title("🔐 Password Strength Meater 💪")
st.write("Please enter your password to check its strength")

st.subheader("🔑Enter your password")
password = st.text_input("Password", type="password")

def check_password_strength(password):
    score = 0

    st.spinner("Checking password strength...")
    if len(password) >= 8:
        score += 1
    else:
        st.warning("❌Password must be at least 8 characters long")
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        st.warning("❌Password must contain at least one uppercase and one lowercase letter")
    if re.search(r"[0-9]", password):
        score += 1
    else:
        st.warning("❌Password must contain at least one digit")
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        st.warning("❌Password must contain at least one special")

    st.write("Password Strength Score:")
    st.progress(score/4)

    if score == 4:
        st.success("✅ Password is strong")
    elif score == 3:
        st.info("🟡 Password is medium")
    else:
        st.warning("🔴 Password is weak")

    
if st.button("Check Password Strength"):
    check_password_strength(password)

st.markdown("---")
st.subheader("🔑 Generate a Random Strong Password")
if st.button("Generate a Random Strong Password"):

    st.spinner("Please wait...")
    
    g_password = "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=16))
    st.code(g_password)


st.markdown("---")
st.markdown("Created by: Syed Abdul Sami")