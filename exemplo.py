import streamlit as st
import os

def main():
    page = st.sidebar.selectbox("Escolha uma opção:", ['Opção 1', 'Opção 2', 'Opção 3'])
    st.header('Tutorial Streamlit - Heroku')
    st.write('Esta é uma página de teste.')
    st.write(os.getcwd())

if __name__ == '__main__':
    main()
