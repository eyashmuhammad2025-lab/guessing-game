import streamlit as st
import random
import time

st.title("🧠 Memory Game – Match the Pairs!")

# --- Initialize game state ---
if "cards" not in st.session_state:
    emojis = ["🍎", "🍌", "🍒", "🍇", "🍓", "🍉"]
    cards = emojis * 2          # create pairs
    random.shuffle(cards)
    st.session_state.cards = cards
    st.session_state.revealed = [False] * len(cards)
    st.session_state.flipped_indices = []
    st.session_state.matched = [False] * len(cards)

# --- Display the game board ---
cols = st.columns(4)

for i, col in enumerate(cols * 3):  # supports 12 cards
    if i >= len(st.session_state.cards):
        break

    card = st.session_state.cards[i]

    if st.session_state.revealed[i] or st.session_state.matched[i]:
        col.button(card, key=f"card{i}", disabled=True)
    else:
        if col.button("❔", key=f"card{i}"):
            st.session_state.revealed[i] = True
            st.session_state.flipped_indices.append(i)
            st.rerun()

# --- Game logic: check for match ---
if len(st.session_state.flipped_indices) == 2:
    i1, i2 = st.session_state.flipped_indices

    # If match
    if st.session_state.cards[i1] == st.session_state.cards[i2]:
        st.session_state.matched[i1] = True
        st.session_state.matched[i2] = True
    else:
        # Show for a moment, then hide
        time.sleep(1)
        st.session_state.revealed[i1] = False
        st.session_state.revealed[i2] = False

    st.session_state.flipped_indices = []
    st.rerun()

# --- Game won? ---
if all(st.session_state.matched):
    st.success("🎉 You matched all pairs! Click below to play again.")

    if st.button("Restart Game"):
        st.session_state.clear()
        st.rerun()
