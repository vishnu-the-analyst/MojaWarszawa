from flask import Flask, request
import json
from send_messages import replyinput 
from image_processor import process_image_from_telegram
from database_connection import insert_message



app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '7208080314:AAEdsdWIAqNk5jrux7cvKojMQXZ7PmG3SD4'

@app.route('/webhook', methods=['POST'])
def webhook():
    body = request.get_json()
    # Your logic to handle the update goes here
    print(body)

    
    message = body.get('message', {})
    user_id = message['chat']['id']
    
    insert_message(body)
    
    # Check message type and handle accordingly
    if 'text' in message:
        # Process text message
        in_message = message['text']
        processed = in_message.lower()
        replyinput(user_id, processed)
    
    elif 'photo' in message:
        # Process photo message using image_processor
        photos = message['photo']
        photo_details = photos[-1]  # Get the last (largest) photo in the array
        file_id = photo_details['file_id']
        caption = message.get('caption', 'No caption provided')
        
        response_text = process_image_from_telegram(file_id, )
        replyinput(user_id, f"Processed image with caption: {caption}. Response: {response_text}")
    
    elif 'location' in message:
        # Handle location message
        replyinput(user_id, "Received a location")
    
    else:
        # Handle other types of messages or no specific content
        replyinput(user_id, "Received a message with no specific content")
    
    # Return a successful response
    return {
        'statusCode': 200,
        'body': json.dumps('Message processed successfully')
    }
    
    
    return body

if __name__ == '__main__':
    event = app.run(port=5000)