import streamlit as st

# Set up the app title
st.title("Season-long to Max Daily Catch Converter")

# Input fields
a = st.number_input("Enter Season-long catch:", min_value=0, step=1)
x = st.number_input("Enter Flight in Weeks:", min_value=1, step=1)

# Function to calculate output
def calculate(a, x):
    if x > 0:
        answer1 = a / (2.87 * x)
        answer2 = a / (0.96 * x)
        return round(answer1, 2), round(answer2, 2)
    else:
        return 0, 0  # Avoid division by zero

# Calculate and display output
if st.button("Calculate"):
    result1, result2 = calculate(a, x)
    st.success(f"Output Range: {result1} - {result2}")

# About section
with st.expander("About"):
    st.write("**Programmed by:** Andrei Onufriev")
    st.write("2020 ©")
    st.write(
        "Onufrieva, K. S. & A. V. Onufriev. 2018. "
        "Linear relationship between peak and season-long abundances in insects. "
        "PLOS ONE 13: e0193110. doi:10.1371/journal.pone.0193110."
    )
