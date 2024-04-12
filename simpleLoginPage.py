import streamlit as st
from streamlit.components.v1 import html

def main():
    st.title("Simple Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Check credentials
        if username == "Mukta" and password == "mukta":
            st.write(f"Logged in successfully, {username}!")
            st.write("Click the button below to open a new tab with 'Namaste!'")
            # Embed HTML with JavaScript to open a new tab
            html_string = f"""
                <button onclick="openNewTab()">Open New Tab</button>
                <script>
                    function openNewTab() {{
                        var newTab = window.open("");
                        newTab.document.write("<h1>Namaste, {username}!</h1>");
                    }}
                </script>
            """
            st.components.v1.html(html_string)
        else:
            st.error("Invalid username or password")

if __name__ == "__main__":
    main()
