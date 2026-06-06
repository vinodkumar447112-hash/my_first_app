import streamlit as st

class Calculator:
    def __init__(self):
        st.title("🧮 My OOP Calculator")

    def run(self):
        # Create input fields
        num1 = st.number_input("Enter first number", value=0)
        num2 = st.number_input("Enter second number", value=0)

        # Create a button and trigger logic
        if st.button("Add Numbers"):
            result = num1 + num2
            st.success(f"The total is: {result}")

# Instantiate and run the class
if __name__ == "__main__":
    app = Calculator()
    app.run()