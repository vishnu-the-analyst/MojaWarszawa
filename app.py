from flask import Flask, request
import json
from send_messages import replyinput 
from image_processor import process_image_from_telegram, process_text_from_telegram
from location_processor import is_within_warsaw
from command_support import is_bot_command


app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '7208080314:AAEdsdWIAqNk5jrux7cvKojMQXZ7PmG3SD4'

@app.route('/webhook', methods=['POST'])
def webhook():
    body = request.get_json()
    # Your logic to handle the update goes here
    
    print(body)
    
    message = body.get('message', {})
    user_id = message['chat']['id']
    
    # Check message type and handle accordingly
    
    if is_bot_command(body):
        print("The message contains a bot command.")
        # You can add additional logic here if needed for bot commands
    
    elif 'text' in message:
        # Process text message
        in_message = message['text']
        processed = in_message.lower()
        
        output_message = process_text_from_telegram(processed, body)
        
        replyinput(user_id, output_message)
    
    elif 'photo' in message:
        # Process photo message using image_processor
        photos = message['photo']
        photo_details = photos[-1]  # Get the last (largest) photo in the array
        file_id = photo_details['file_id']
        response_text = process_image_from_telegram(file_id,message.get('caption', 'No caption provided'), body)
        
        replyinput(user_id, response_text)
    
    elif 'location' in message:
        # Handle location message
        
        lon = body['message'].get('location', {}).get('longitude')
        lat = body['message'].get('location', {}).get('latitude')
        
        
        replyinput(user_id, is_within_warsaw(lon, lat))
    
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