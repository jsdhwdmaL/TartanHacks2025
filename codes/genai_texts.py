import google.generativeai as genai

API_KEY = "AIzaSyCvEAFPwUCTRIl-BdsyCOeoZZFODf6rdKY"
genai.configure(api_key=API_KEY)

# Function to get AI-generated puzzle (riddle)
def generate_riddle1():
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = model.generate_content("Create a puzzle for the player based on underwater themes, and the answer must be fish.")
    return response.text
