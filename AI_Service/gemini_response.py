from dotenv import load_dotenv
import google.generativeai as genai
import os
from google.generativeai.types import HarmCategory, HarmBlockThreshold, StopCandidateException


load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API key for Google Generative AI is not set in the environment variables.")

genai.configure(api_key=api_key)

def load_system_instruction(instruction):
    return instruction.strip()

def initialize_models(gemo_instruction, gemi_instruction):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 100,
        "response_mime_type": "text/plain",
    }

    safety_settings = {
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    }
    
    instruction= "Please strictly follow these instructions: Start by introducing yourself, and then continue the chat. Each answer should be no more than two lines."
    
    gemo = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction=f'Strictly act as if {gemo_instruction}. {instruction}',
        safety_settings=safety_settings
    )

    gemi = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction=f'Strictly act as if {gemi_instruction}. {instruction}',
        safety_settings=safety_settings
    )
    return gemo, gemi

# Initialize models globally
gemo, gemi = initialize_models("", "")

chat_session_gemo = gemo.start_chat(history=[])
chat_session_gemi = gemi.start_chat(history=[])
conversation_history = ["Hello!"]

def get_gemi_response(gemo_text):
    try:
        gemi_response = chat_session_gemi.send_message(gemo_text)
        return gemi_response.text
    except StopCandidateException:
        return "Aww! Stop 😊, that's not a good thing to say"

def get_gemo_response(gemi_text):
    try:
        gemo_response = chat_session_gemo.send_message(gemi_text)
        return gemo_response.text
    except StopCandidateException:
        return "Aww! Stop 😊, that's not a good thing to say"

def reset_chat_session():
    global chat_session_gemo
    chat_session_gemo = gemo.start_chat(history=[])
    global chat_session_gemi
    chat_session_gemi = gemi.start_chat(history=[])
    global conversation_history
    conversation_history = ["Hello!"]

def update_models(gemo_instruction, gemi_instruction):
    global gemo, gemi
    gemo, gemi = initialize_models(gemo_instruction, gemi_instruction)
    reset_chat_session()



