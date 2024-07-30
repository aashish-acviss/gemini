"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="API_KEY")

# Set up the model
# generation_config = {
#     "temperature": 0,
#     "top_p": 1,
#     "top_k": 1,
#     "max_output_tokens": 10000,
# }
#
# safety_settings = [
#     {
#         "category": "HARM_CATEGORY_HARASSMENT",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#     },
#     {
#         "category": "HARM_CATEGORY_HATE_SPEECH",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#     },
#     {
#         "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#     },
#     {
#         "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#     }
# ]

# import PIL.Image
#
# img = PIL.Image.open('image_2.jpg')
# model = genai.GenerativeModel('gemini-1.5-flash')
#
# response = model.generate_content(img)
#
# print(response.candidates)

import google.generativeai as genai
import os

# Function to read text from a file
def read_text_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Read text from the file
text_path = "text.txt"  # Update with your text file path
text = read_text_from_file(text_path)

# Create the prompt
prompt = f"Act like you are an intelligent AI system whose job is to create a detailed description from broken words. Now, using each word from the below text, provide a detailed and coherent description in one sentence without any extra punctuation: {text}"

# Initialize the GenerativeModel
model = genai.GenerativeModel('gemini-pro')

# Generate content using the model
response = model.generate_content(prompt)

# Print the generated content
print(response.text)
