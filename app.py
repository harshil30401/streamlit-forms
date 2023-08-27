import streamlit as st
import re

def is_valid_phone_number(phone_number):
    # Define a regular expression pattern for a basic phone number format
    pattern = r"^\d{10}$"
    return re.match(pattern, phone_number)

def main():
    st.title("Streamlit Form Example")
    
    # Create a form using st.form()
    with st.form("user_info_form"):
        st.write("Enter your information:")
        
        # Add input fields to the form
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, max_value=120)
        phone_number = st.text_input("Phone Number")
        favorite_color = st.selectbox("Favorite Color", ["Red", "Green", "Blue", "Yellow", "Other"])
        
        # Add a submit button
        submitted = st.form_submit_button("Submit")
        
        # Validate phone number before submission
        if submitted:
            if not is_valid_phone_number(phone_number):
                st.warning("Please enter a valid 10-digit phone number.")
            else:
                st.write("Submitted Information:")
                st.write(f"Name: {name}")
                st.write(f"Age: {age}")
                st.write(f"Phone Number: {phone_number}")
                st.write(f"Favorite Color: {favorite_color}")

if __name__ == "__main__":
    main()
