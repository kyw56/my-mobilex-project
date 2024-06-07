import i18n
import streamlit as st

from utils.init import init_once


if __name__ == '__main__':
    # Init
    init_once()

    # Show title
    st.title(i18n.t('Welcome to Recommending Menu for the Meal'))

    # Show page description
    st.write(i18n.t('By entering a few simple pieces of information, you can receive food recommendations tailored to your situation!'))
