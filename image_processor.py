# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 19:20:36 2024

@author: Vishnu Kumar
"""

import requests
import google.generativeai as genai
from google.generativeai.protos import Blob


bot_token = '7208080314:AAEdsdWIAqNk5jrux7cvKojMQXZ7PmG3SD4'
GOOGLE_API_KEY="AIzaSyCFurY92HfBmDO1K3gRjGY8y3lAvOK5YjY"

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
def process_image_from_telegram(file_id, captions):
    # Example configuration or setup specific to Gemini API
    get_file_url = f"https://api.telegram.org/bot{bot_token}/getFile?file_id={file_id}"
    response = requests.get(get_file_url)
    file_path = response.json()['result']['file_path']

    download_url = f"https://api.telegram.org/file/bot{bot_token}/{file_path}"
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
    
    
    
    initial_check = model.generate_content([
    "Based on image and captions provided, decide whether the issue can be handled by the user on its own. Reply with 'yes' or 'no'",
    "Image:",img,
    "\nCaptions: {captions}\n",
    "Decision:\n",
    ])

    
    if initial_check.text.strip() == 'no':
        
        response = model.generate_content([
            f"Classify the image with the captions into following categories: {', '.join(AVAILABLE_PUBLIC_SERVICES)}\n",
            "Respond only with a choosen category for the message.\n",
            "Image:",
            img,
            "\nCaptions: {captions}\n",
            "Category:\n",
            ])
        return "Could you please share the geolocation using telegram location function?\n" + response.text + " Location of the issue help us to speed up the action to resolve."

    elif initial_check.text.strip() =='yes':
 
        response = model.generate_content(["Tell the user how he should deal with the following issue in Warsaw presented in the image and captions\nAssume you are the citizen service respondent of Warsaw city",
                                           "Image:",
                                           img,
                                           "\nCaptions: {captions}\n",
                                           "Solution:\n"
                                           ])
        return response.text
    

def process_text_from_telegram(message):
    
    DECISION_MAKING_PROMPT = (
    "Based on the message provided, decide whether the issue can be handled by the user on its own. Reply with 'yes' or 'no'\n",
    "Message: {message}\n",
    "Decision:\n",
    )
    
    in_message = DECISION_MAKING_PROMPT.format(message=message)
    
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-pro')
    
    
    initial_check = model.generate_content(in_message)
    print(initial_check.text)

    
    if initial_check.text.strip() == 'no':
        
        MESSAGE_CLASSIFICATION_PROMPT = (
            f"Classify the message into the following categories: {', '.join(AVAILABLE_PUBLIC_SERVICES)}.\n"
            "Respond with a choosen category for the message.\n"
            "Message: {message}\n"
            "Category:\n"
            )
        
        in_message = MESSAGE_CLASSIFICATION_PROMPT.format(message=message)
        
        DECISION_MAKING_PROMPT = (MESSAGE_CLASSIFICATION_PROMPT)
        in_message = DECISION_MAKING_PROMPT.format(message=in_message)
        response = model.generate_content()
        return "Could you please share the geolocation using telegram location function?\n Your issue has been assigned to the office of the " + response.text + " Location of the issue help us to speed up the action to resolve."

    elif initial_check.text.strip() =='yes':
        
        MESSAGE_CLASSIFICATION_PROMPT = ("Tell the user how he should deal with the following issue in Warsaw presented in the text. Assume you are the citizen service respondent of Warsaw city\n {message}",
                                           "Solution:\n"
                                           "Tell the user how he should deal with the following issue in Warsaw presented in the text. Assume you are the citizen service respondent of Warsaw city\n",
                                           "Message: {message}\n",
                                           "Decision:\n",
                                           )
        
        
        in_message = MESSAGE_CLASSIFICATION_PROMPT.format(message=message)
        response = model.generate_content(message= in_message)
        return response.text
    
