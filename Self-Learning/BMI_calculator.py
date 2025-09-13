import streamlit as st

st.title("Welcome")

weight = st.number_input("Enter your weight")

height_unit = st.radio("Select your height format", ("cms", "meters", "feet"))

if height_unit == "cms":
    height = st.number_input("Enter your height in centimeters", 1, 250)
    bmi = weight / ((height /100)**2)
elif height_unit == "meters":
    height = st.number_input("Enter your height in meters", 0.1, 2.50)
    bmi = weight / (height**2)
else:
    height = st.number_input("Enter your height in feet", 0.1, 2.50)
    bmi = weight / ((height / 3.28)**2)

if st.button("Calculate BMI"):
    st.subheader(f"Your BMI index is {bmi}")
    if bmi < 16:
        st.error("You are Extremely Underweight")
    elif bmi >= 16 and bmi < 18.5:
        st.warning("You are Underweight")
    elif bmi >= 18.5 and bmi < 25:
        st.success("Healthy")
    elif bmi >= 25 and bmi < 30:
        st.warning("Overweight")
    else:
        st.warning("Extremely Overweight")

