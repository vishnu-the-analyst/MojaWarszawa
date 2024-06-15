# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 19:19:26 2024

@author: Vishnu Kumar
"""

import json
import requests

url = f'https://api.telegram.org/bot7208080314:AAEdsdWIAqNk5jrux7cvKojMQXZ7PmG3SD4/sendMessage'

def replyinput(user_id, in_message):
    payload = {
            'chat_id': user_id,
            'text': in_message
        }
    
    r = requests.post(url, json = payload)
