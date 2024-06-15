# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 19:20:36 2024

@author: Vishnu Kumar
"""

import requests
import google.generativeai as genai
from google.generativeai.protos import Blob


bot_token = '7208080314:AAEdsdWIAqNk5jrux7cvKojMQXZ7PmG3SD4'
GOOGLE_API_KEY="AIzaSyB9zwtlH43IJMALfavtHN4YN-8PukXTtAI"

# Function to process image from Telegram and interact with Gemini API
def process_image_from_telegram(file_id):
    # Example configuration or setup specific to Gemini API
    get_file_url = f"https://api.telegram.org/bot{bot_token}/getFile?file_id={file_id}"
    response = requests.get(get_file_url)
    file_path = response.json()['result']['file_path']

    download_url = f"https://api.telegram.org/file/bot{bot_token}/{file_path}"
    file_response = requests.get(download_url)
    data = requests.get(download_url)
    
    img = Blob(mime_type="image/jpeg", data=data.content)

    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-pro')
    
    AVAILABLE_PUBLIC_SERVICES = [
    "Waste Management",
    "Transportation",
    "Water Conservation and Management",
    "Energy Efficiency and Renewable Energy",
    "Urban Planning and Development",
    "Education and Public Awareness"
    "Health and Environmental Protection",
    "Sustainable Agriculture and Food Production",
    "Community Engagement and Cultural Initiatives",
    "Sustainable Infrastructure",
    "Economic Incentives and Green Jobs",
    "Eco-Friendly Tourism",
    ]
    
    MESSAGE_CLASSIFICATION_PROMPT = (
    f"Classify the message into the following categories: {', '.join(AVAILABLE_PUBLIC_SERVICES)}\n"
    "Message: {message}\n"
    "Category:\n"
    )
    
    response = model.generate_content([
    f"Classify the image into following categories: {', '.join(AVAILABLE_PUBLIC_SERVICES)}\n",
    img,
    "Category:\n",
    ])
    return response.text
