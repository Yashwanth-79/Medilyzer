import streamlit as st
from PIL import Image
import base64
import time
import google.generativeai as genai
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import json
import requests

# Firebase initialization
if not firebase_admin._apps:
    cred = credentials.Certificate("ambition-.json")
    firebase_admin.initialize_app(cred)

#B8CAEF #7FD689
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

st.set_page_config(
    page_title="Phoenix Wizards",
    page_icon=":wizard:",
    layout="wide",
)

def cover_page():
    st.markdown(
        """
        <style>
        body {
            background-image: linear-gradient(to right, #FFFFFF, #ADD8E6);
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    logo_path = r'C:\Users\YESHWANTH M S\Documents\version 1\Medilyzer\LOGO (1).png'  
    logo_base64 = get_base64_of_bin_file(logo_path)
    st.markdown(
        f"""
        <center><img src="data:image/png;base64,{logo_base64}" width="550" style="margin-top: 12px;"></center>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        "<center><h1 style='font-family: Castellar, Times, serif; font-size: 36px; color: #FF4B4B;'>PHOENIX WIZARDS</h1></center>",
        unsafe_allow_html=True,
    )
    col1, col2 = st.columns((0.5, 0.5))
    with col1:
        st.markdown("### Features!")
        st.markdown("   Multilingual")
        st.markdown("   Enhanced security")
        st.markdown("   Real time evaluation")
        
        
    with col2:    
        st.markdown("### Usecases!")
        st.markdown("   Generic vs Branded")
        st.markdown("   Prescription Analysis")
        st.markdown("   price comparison")
    st.markdown(
        """
        <style>
        [data-testid="stButton"] {
            background-color: #FF4B4B;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 16px;
            font-weight: bold;
            color: #373E3F;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        [data-testid="stButton"]:hover {
            background-color: #34C759;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    if st.button("START😁"):
        st.session_state.page = 'auth'

def authentication_page():
    st.title("Welcome to :violet[Medilyzer ⚕️]")

    if "username" not in st.session_state:
        st.session_state.username = ""
    if "useremail" not in st.session_state:
        st.session_state.useremail = ""

    def sign_up_with_email_and_password(
        email, password, username=None, return_secure_token=True
    ):
        try:
            rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp"
            payload = {
                "email": email,
                "password": password,
                "returnSecureToken": return_secure_token,
            }
            if username:
                payload["displayName"] = username
            payload = json.dumps(payload)
            r = requests.post(
                rest_api_url,
                params={"key": ""},
                data=payload,
            )
            try:
                return r.json()["email"]
            except:
                st.warning(r.json())
        except Exception as e:
            st.warning(f"Signup failed: {e}")

    def sign_in_with_email_and_password(
        email=None, password=None, return_secure_token=True
    ):
        rest_api_url = (
            "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
        )

        try:
            payload = {"returnSecureToken": return_secure_token}
            if email:
                payload["email"] = email
            if password:
                payload["password"] = password
            payload = json.dumps(payload)
            r = requests.post(
                rest_api_url,
                params={"key": ""},
                data=payload,
            )
            try:
                data = r.json()
                user_info = {
                    "email": data["email"],
                    "username": data.get(
                        "displayName"
                    ), 
                }
                return user_info
            except:
                st.warning(data)
        except Exception as e:
            st.warning(f"Signin failed: {e}")

    def reset_password(email):
        try:
            rest_api_url = (
                "https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode"
            )
            payload = {"email": email, "requestType": "PASSWORD_RESET"}
            payload = json.dumps(payload)
            r = requests.post(
                rest_api_url,
                params={"key": ""},
                data=payload,
            )
            if r.status_code == 200:
                return True, "Reset email Sent"
            else:
                error_message = r.json().get("error", {}).get("message")
                return False, error_message
        except Exception as e:
            return False, str(e)

    def f():
        try:
            userinfo = sign_in_with_email_and_password(
                st.session_state.email_input, st.session_state.password_input
            )
            st.session_state.username = userinfo["username"]
            st.session_state.useremail = userinfo["email"]

            global Usernm
            Usernm = userinfo["username"]

            st.session_state.signedout = True
            st.session_state.signout = True
            st.session_state.pop('email_input', None)
            st.session_state.pop('password_input', None)
            st.session_state.page = 'main'  # Redirect to main page after successful login
            st.experimental_rerun()  # Force a rerun to load the main page

        except:
            ''

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False
        st.session_state.username = ""

    def forget():
        email = st.text_input("Forgot Password ❓❓ Enter your email here")
        if st.button("Send Reset Link"):
            print(email)
            success, message = reset_password(email)
            if success:
                st.success("Password reset email sent successfully.")
            else:
                st.warning(f"Password reset failed: {message}")

    if "signedout" not in st.session_state:
        st.session_state["signedout"] = False
    if "signout" not in st.session_state:
        st.session_state["signout"] = False

    if not st.session_state["signedout"]:
        choice = st.selectbox("Login/Signup", ["Login", "Sign up"])
        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")
        st.session_state.email_input = email
        st.session_state.password_input = password

        if choice == "Sign up":
            username = st.text_input("Enter your unique username")
            if st.button("Create my account"):
                user = sign_up_with_email_and_password(
                    email=email, password=password, username=username
                )
                st.success("Account created successfully!")
                st.markdown("Please Login using your email and password")
                st.balloons()
        else:
            st.button("Login", on_click=f)
            forget()

    if st.session_state.signout:
        st.text("Name " + st.session_state.username)
        st.text("Email id: " + st.session_state.useremail)
        st.button("Sign out", on_click=t)

def main_page():
    genai.configure(api_key='') 
    GOOGLE_API_KEY = ''  
    SEARCH_ENGINE_ID = ''  
    generation_config = {
        "temperature": 0.2,
        "top_p": 1,
        "top_k": 0,
        "max_output_tokens": 200,
        "response_mime_type": "text/plain",
    }
    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
    ]

    model = genai.GenerativeModel(
        model_name="gemini-1.0-pro",
        safety_settings=safety_settings,
        generation_config=generation_config,
    )

    model1 = genai.GenerativeModel("gemini-1.5-pro", safety_settings=safety_settings, generation_config=generation_config)

    def gemini_pro_response(user_prompt, language_code):
        user_prompt = f"{user_prompt} in {language_code}"
        chat_session = model.start_chat()
        response = chat_session.send_message(user_prompt)
        response_text = ""
        for chunk in response:
            response_text += chunk.text
        return response_text

    def gemini_pro_vision_response(image, language_code):
        gemini_pro_vision_model = model1
        response = gemini_pro_vision_model.generate_content(
            ["given medicine image, read it properly as much as possible like an OCR manner and give accurate text from medicine image", image])
        text = response.text
        return gemini_pro_response(text, language_code)

    def google_search(query, retries=3, delay=5):
        for i in range(retries):
            try:
                service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
                res = service.cse().list(q=query, cx=SEARCH_ENGINE_ID).execute()
                return ''
            except HttpError as e:
                st.error(f"An error occurred: {e}")
                if i < retries - 1:
                    time.sleep(delay)
                else:
                    return []
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
                return []

    user_promptt,search_results,result_snip='','',''
    st.sidebar.markdown("<h1 style='text-align: left; font-size:50px;color: green;'>Welcome to Medilyzer⚕️</h1>", unsafe_allow_html=True)
    st.sidebar.markdown("<h1 style='text-align: left; font-size:25px;font-weight:bold; color: white;'>Choose your input form🤗</h1>", unsafe_allow_html=True)

    language = st.sidebar.selectbox("Select Language👇", ["English", "Hindi"])

    if language == "English":
        language_code = "english"
    elif language == "Hindi":
        language_code = "Hindi"

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    if 'active_section' not in st.session_state:
        st.session_state['active_section'] = 'classify_compare'

    if st.sidebar.button("Classify and Compare🏥", key="classify_compare_button"):
        st.session_state['active_section'] = 'classify_compare'
    elif st.sidebar.button("Generic List📃", key="generic_list_button"):
        st.session_state['active_section'] = 'generic_list'
    elif st.sidebar.button("Prescription Analysis🩺", key="prescription_analysis_button"):
        st.session_state['active_section'] = 'prescription_analysis'

    if st.session_state['active_section'] == 'classify_compare':
        st.title("Classify and Compare🏥")
        st.markdown("##### Enter the name of a medicine or put a image, to know more about your medicine")
        option = st.radio("Choose Input Type:", ("Text", "Image"), key="input_type_radio")

        if option == "Text":
            text_input = st.text_area("Enter Text:", key="text_input_area")
            if st.button("Submit", key="text_submit_button"):
                user_prompt = (f"based on language selected from{language},,if language is english,then don't translate the following points,if {language}, is selected translate the following commands and give them in  hindi as selected output should in {language}"
                f"Note: if text is one or two word given related to medicine or company or any medicine technical term, just give output but don't give null answer or not sufficient answer. Can you provide detailed information about the following medicine from given image or text: '{text_input}'. "
                "Specifically, include:\n"
                "1. Whether this medicine is generic or branded (just specify whether it is generic/branded; caution: always give the correct answer and once cross verify, don't give irrelevant information).\n"
                f"2. {text_input} at next line mention and Give the approximate price range (for generic medicine within 50INR if available like Rs(30-35)Rs(30-45)Rs(25-30)Rs(25-35)(20-30))(for branded medicine keep price ranges at more 70 INR )(keep changing price range for other tablets only in small margin)(NOTE: Always give same answer after each iteration).\n"
                "3. A brief description (including: precautions but not much just give 3-4 points) of this medicine.\n"
                "4. Always display disclaimer to refer doctors."
                "please give formatted output,do give clean output"
                "Atlast give disclaimer"
                )
                search_results = google_search(text_input)
                if search_results:
                    result_snippets = ' '.join([item['snippet'] for item in search_results])
                    user_promptt = f" Here are some additional details from real-time search: {result_snippets}"
                response_text = gemini_pro_response(user_prompt, language)
                st.session_state['chat_history'].append({"user": text_input, "response": response_text})
                st.markdown(f"**Description:** {response_text}")

        if option == "Image":
            image_file = st.file_uploader("Upload Image:", type=["jpg", "png", "jpeg"], key="image_uploader")
            if image_file is not None:
                image = Image.open(image_file)
                st.image(image, caption="Uploaded Image", use_column_width=True)
                if st.button("Extract Text", key="extract_text_button"):
                    extracted_text = gemini_pro_vision_response(image, language)
                    user_prompt = (f"based on language selected from{language},,if language is english don't translate the following points,if {language}, is selected translate the following commands and give them in  hindi as selected output should in {language}"
                    f"Can you provide detailed information about the following medicine extracted from an image: {extracted_text}.\n"
                    "Specifically, give output each next line for following commands:\n"
                    "1. Whether this medicine is generic or branded (just specify whether it is generic/branded; caution: always give the correct answer and once cross verify, don't give irrelevant information) (NOTE: I got some wrong answers, correct it and give me proper answer and same answer for each iteration and continue at next line.\n\n"
                    f"2. {extracted_text} at next line mention and Give the approximate price range (for generic medicine within 50INR if available like Rs(30-35)Rs(30-45)Rs(25-30)Rs(25-35)(20-30))(for branded medicine keep price ranges at more 70 INR )(keep changing price range for other tablets only in small margin)(NOTE: Always give same answer after each iteration).\n"
                    "3. A very small description (including: precautions in 3-4 points) of this medicine.\n"
                    "4. Always display disclaimer to refer doctors."
                    "please give formatted output,do give clean output"
                    "Atlast give disclaimer"
                )
                    search_results = google_search(extracted_text)
                    if search_results:
                        result_snippets = ' '.join([item['snippet'] for item in search_results])
                        user_prompt += f" Here are some additional details from real-time search: {result_snippets}"

                    response_text = gemini_pro_response(user_prompt, language)
                    st.session_state['chat_history'].append({"user": extracted_text, "response": response_text})
                    st.markdown(f"**Description:** {response_text}")

    elif st.session_state['active_section'] == 'generic_list':
        st.title("Generic List📃")
        st.markdown("##### Describe your symtoms/signs of your illness in simple words, to get list of medicines in your language")
        text_input = st.text_area("Enter Text:", key="generic_list_text_input")
        if st.button("Submit", key="generic_list_submit_button"):
            user_prompt = (f"based on language selected from{language},,if language is english don't translate the following points,if {language}, is selected translate the following commands and give them in hindi as selected output should in {language}"
            f"Can you provide a list of generic and branded similar to the following: '{text_input}', with their price ranges in INR. Please display the information in a table format with columns: generic meds, generic meds price, branded meds, branded price."
            "atlast after showing output give disclaimer about the consultation and price variation"
            "Atlast give disclaimer,don't forget this"
             "please give formatted output,do give clean output"
        )   
            search_results = google_search(text_input)
            if search_results:
                result_snippets = ' '.join([item['snippet'] for item in search_results])
                user_prompt += f" Here are some additional details from real-time search: {result_snippets}"
            response_text = gemini_pro_response(user_prompt, language)
            st.session_state['chat_history'].append({"user": text_input, "response": response_text})
            st.markdown(f"**Similar Medicines and Prices:**\n\n{response_text}")

    elif st.session_state['active_section'] == 'prescription_analysis':
        st.title("Prescription Analysis🩺")
        st.markdown("##### Based on prescription medicines are suggested with ranges.")
        image_file = st.file_uploader("Upload Prescription Image:", type=["jpg", "png", "jpeg"], key="prescription_image_uploader")
        if image_file is not None:
            image = Image.open(image_file)
            st.image(image, caption="Uploaded Prescription Image", use_column_width=True)
            if st.button("Analyze Prescription", key="analyze_prescription_button"):
                extracted_text = gemini_pro_vision_response(image, language_code)
                user_prompt = (f"based on language selected from{language},if language is english don't translate the following points,if {language},if results are not found , then just translate  found answers from english to hindi"
                f"Can you analyze the prescription and provide the necessary information {extracted_text}.\n"
                f"Give the list of generic medicine that are available for {extracted_text} with the prices in INR and very small description about each tablet in 1 line"
                f"Dont say theres no information is provided {language},you fetch the information as much as possible from image and considering key points from {extracted_text} give genric medicine suggestion, dont say NO"
                f"{extracted_text} at next line mention and Give the approximate price range (for generic medicine within 50INR if available like Rs(30-35)Rs(30-45)Rs(25-30)Rs(25-35)(20-30))"
                "Atlast considering all the above outputs display the information in a table format with columns: generic meds, generic meds price, branded meds, branded price."
                "atlast after showing output give disclaimer about the consultation and price variation"
                "Atlast give disclaimer"
                 "please give formatted output,do give clean output"
            )
                search_results = google_search(extracted_text)
                if search_results:
                    result_snippets = ' '.join([item['snippet'] for item in search_results])
                    user_prompt += f" Here are some additional details from real-time search: {result_snippets}"

                response_text = gemini_pro_response(user_prompt, language)
                st.session_state['chat_history'].append({"user": extracted_text, "response": response_text})
                st.markdown(f"**Prescription Analysis:** {response_text}")

    if 'chat_history' in st.session_state and st.session_state['chat_history']:
        st.write("### Chat History")
        for i, chat in enumerate(st.session_state['chat_history']):
            st.write(f"**User:** {chat['user']}")
            st.write(f"**Response:** {chat['response']}")
    if st.sidebar.button("Logout"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.session_state.page = 'auth'
        st.experimental_rerun()


if 'page' not in st.session_state:
    st.session_state.page = 'cover'

if st.session_state.page == 'cover':
    cover_page()
elif st.session_state.page == 'auth':
    authentication_page()
elif st.session_state.page == 'main':
    main_page()
