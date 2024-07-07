import streamlit as st
import requests
from bs4 import BeautifulSoup
import random
import os
from dotenv import load_dotenv


def load_words_alpha():
    with open("words_alpha.txt") as word_file:
        words_alpha = set(word_file.read().split())
    return words_alpha


def is_valid_word(word):
    """Checks if a word exists using a dictionary API (e.g., Merriam-Webster)."""
    # Replace with your API key and endpoint
    api_key = os.getenv("DICTIONARY_API_KEY")
    url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for errors
        data = response.json()
        return isinstance(
            data[0], dict
        )  # Check if it's a valid word definition (and not a list of suggestions)
    except requests.RequestException:
        return False


def get_word_list(letters, center_letter):
    if not letters or not center_letter:
        return []
    words_alpha = load_words_alpha()
    word_list = [
        word
        for word in words_alpha
        if set(word).issubset(set(letters)) and len(word) >= 4 and center_letter in word
    ]
    return word_list


def give_hint(word_list):
    if not word_list:
        return "No words found."

    while True:
        word = random.choice(word_list)
        if is_valid_word(word):
            break

    length = len(word)
    revealed = random.randint(1, length - 1)
    hint = ["_" if i >= revealed else char for i, char in enumerate(word)]

    return f"{''.join(hint)} (Length: {length})"


# Streamlit UI
st.title("Spelling Bee Hint Generator")

# User input for letters
st.write("Enter the Spelling Bee letters:")
center_letter = st.text_input("Center letter", max_chars=1).lower()
outer_letters = st.text_input("Outer letters (no spaces)", max_chars=6).lower()

if center_letter and outer_letters and len(outer_letters) == 6:
    all_letters = center_letter + outer_letters

    if (
        "word_list" not in st.session_state
        or st.session_state.get("previous_letters") != all_letters
    ):
        st.session_state.word_list = get_word_list(all_letters, center_letter)
        st.session_state.previous_letters = all_letters

    st.write(f"Center letter: {center_letter}")
    st.write(f"Outer letters: {', '.join(outer_letters)}")

    if st.button("Get Hint"):
        hint = give_hint(st.session_state.word_list)
        st.write(f"Hint: {hint}")
else:
    st.write("Please enter a center letter and exactly 6 outer letters.")

# Footer
st.markdown("---")
st.write("Note: This tool is for fun purposes only. Please use responsibly.")