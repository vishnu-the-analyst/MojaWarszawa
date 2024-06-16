# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 19:20:36 2024

@author: Vishnu Kumar
"""

import requests
import google.generativeai as genai
from google.generativeai.protos import Blob
from database_connection import insert_message


bot_token = '7208080314:AAEdsdWIAqNk5jrux7cvKojMQXZ7PmG3SD4'
GOOGLE_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

AVAILABLE_PUBLIC_SERVICES = [
    "Waste Management",
    "Transportation",
    "Water Conservation and Management",
    "Energy Efficiency and Renewable Energy",
    "Urban Planning and Development",
    "Education and Public Awareness",
    "Health and Environmental Protection",
    "Sustainable Agriculture and Food Production",
    "Community Engagement and Cultural Initiatives",
    "Sustainable Infrastructure",
    "Economic Incentives and Green Jobs",
    "Eco-Friendly Tourism",
    "Police",
    "Fire and Emergency Services",
    "Public Healthcare Services",
    "Social Welfare Services",
    "Public Housing",
    "Public Libraries",
    "Parks and Recreation",
    "Child and Family Services",
    "Elderly Care Services",
    "Disaster Preparedness and Response",
    "Public Safety and Security",
    "Road Maintenance and Public Works",
    "Public Transportation Systems",
    "Environmental Conservation",
    "Mental Health Services",
    "Public Utilities (Electricity, Gas, Water)",
    "Employment and Job Training Services",
    "Veterans Services",
    "Animal Control and Welfare",
    "Legal Aid and Public Defender Services",
    "Immigration Services",
    "Community Centers and Youth Programs",
    "Substance Abuse and Rehabilitation Services",
    "Food Assistance Programs",
    "Civil Rights and Advocacy Services",
    "Consumer Protection Services",
    "Public Communications and Information Services",
    "Public Health Education",
    "Disability Services",
    "Transportation Infrastructure",
    "Environmental Cleanup and Remediation",
    "Emergency Shelters and Homeless Services",
    "Public Health Inspection and Regulation",
    "Community Policing Initiatives",
    "Neighborhood Watch Programs",
    "Public Art and Cultural Programs",
    "Public Economic Development Programs"
]


# Function to process image from Telegram and interact with Gemini API
def process_image_from_telegram(file_id, captions, body):
    # Example configuration or setup specific to Gemini API
    get_file_url = f"https://api.telegram.org/bot{bot_token}/getFile?file_id={file_id}"
    response = requests.get(get_file_url)
    file_path = response.json()['result']['file_path']

    download_url = f"https://api.telegram.org/file/bot{bot_token}/{file_path}"
    data = requests.get(download_url)
    
    img = Blob(mime_type="image/jpeg", data=data.content)

    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-pro')
    
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": ["Based on image and captions provided, decide whether the issue can be handled by the user on its own. Reply with 'yes' or 'no'.  If it is a suggestion or thanking or feedback then reply with 'yes'",
                    img,
                    captions,
                    ],
                },
            ]
        )
    
    
    initial_check = chat_session.send_message("captions")

    
    if initial_check.text.strip() == 'no':
        
        
        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [f"Classify the image with the captions into following categories: {', '.join(AVAILABLE_PUBLIC_SERVICES)}\n",
                    "Respond only with a choosen category for the message.\n",
                        img,
                        captions,
                        ],
                    },
                ]
            )
        
        
        response = chat_session.send_message("captions")
        
        insert_message(body, response.text)
        

        return "Could you please share the geolocation using telegram location function?\n The issue has been assigned to the office of " + response.text  +" Location of the issue will help us to speed up the action to resolve."

    elif initial_check.text.strip() =='yes':
        
        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": ["Tell the user how he should deal with the following issue in Warsaw presented in the image and captions\nAssume you are the citizen service respondent of Warsaw city. if the user made suggestion or feedback then accept it, acknowledge if there is a gratitude.try to give contact details of relavent authority wherever neccessary.",
                        img,
                        captions,
                        ],
                    },
                ]
            )
        
        
        response = chat_session.send_message("captions")
        
        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [f"Only if it is a suggestion then Classify the image with the captions into following categories: {', '.join(AVAILABLE_PUBLIC_SERVICES)} else respond null\n",
                    "Respond only with a choosen category for the message or null\n",
                        img,
                        captions,
                        ],
                    },
                ]
            )
        
        
        category = chat_session.send_message("captions")
        
        
        
        
        insert_message(body, category.text)
        

        return response.text
    

def process_text_from_telegram(message, body):
    
    
    genai.configure(api_key=GOOGLE_API_KEY)
    
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
      }
    
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
        )
    
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    "Based on the message provided, decide whether the issue can be handled by the user on its own. Reply with 'yes' or 'no'. If it is a suggestion or thanking or feedback then reply with 'yes'",
                    ],
                },
            ]
      )
    
    initial_check = chat_session.send_message(message)

    
    if initial_check.text.strip() == 'no':
        
        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [
                        f"Classify the message into the following categories: {', '.join(AVAILABLE_PUBLIC_SERVICES)}.\n",
                        "Respond only with a choosen category for the message.\n",
                        ],
                    },
                ]
          )
        
        
        response = chat_session.send_message(message)
        
        insert_message(body, response.text)
        
        return "Could you please share the geolocation using telegram location function?\n Your issue has been assigned to the office of the " + response.text + " Location of the issue help us to speed up the action to resolve."

    elif initial_check.text.strip() =='yes':
        
        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [
                        "Tell the user how they should deal with the following issue in Warsaw presented in the text. Assume you are the citizen service respondent of Warsaw city. if the user made suggestion or feedback then accept it, acknowledge if there is a gratitude.try to give contact details of relavent authority wherever neccessary.",
                        ],
                    },
                ]
          )
        
        
        response = chat_session.send_message(message)
        
        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [
                        f"only If it is a suggestion Classify the message into the following categories: {', '.join(AVAILABLE_PUBLIC_SERVICES)}.\n else respond null",
                        "Respond only with a choosen category for the message or null\n",
                        ],
                    },
                ]
          )
        
        
        category = chat_session.send_message(message)
        
        
        insert_message(body, category.text)
        
        return response.text
    
