import streamlit as st
import random

st.title("🎯 Number Guessing Game")

# Initialize session state variables
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
if "message" not in st.session_state:
    st.session_state.message = ""

st.write("I'm thinking of a number between 1 and 100. Try to guess it!")

# User input
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Guess"):
    if guess < st.session_state.number:
        st.session_state.message = "📉 Too low! Try again."
    elif guess > st.session_state.number:
        st.session_state.message = "📈 Too high! Try again."
    else:
        st.session_state.message = "🎉 Correct! You guessed the number!"
        
    st.rerun()

st.write(st.session_state.message)

# Reset game
if st.button("Reset Game"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.message = ""
    st.rerun()
