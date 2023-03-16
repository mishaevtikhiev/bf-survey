import streamlit as st

# Define the questions and possible answers
questions = {
    "What is your favorite color?": ["Red", "Green", "Blue"],
    "What is your favorite animal?": ["Dog", "Cat", "Fish"],
    "What is your favorite food?": ["Pizza", "Burgers", "Tacos"]
}

# Initialize a dictionary to store the user's answers
answers = {}

# Loop through the questions and present them to the user
for question, choices in questions.items():
    # Use Streamlit's `radio` widget to create a multiple-choice question
    answer = st.radio(question, choices)
    # Store the user's answer in the dictionary
    answers[question] = answer

# Display the user's answers
st.write("Here are your answers:")
for question, answer in answers.items():
    st.write(f"- {question}: {answer}")

