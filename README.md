---

# Warsaw Citizen Support Bot

## Overview

The Warsaw Citizen Support Bot is a Telegram bot designed to help citizens of Warsaw report issues, suggest improvements, and get information about city services. It leverages various APIs and services to process text and image messages, classify them into relevant categories, and respond with appropriate information or instructions.

## Features

- **Report Issues**: Citizens can report issues such as potholes, waste management problems, etc.
- **Suggest Improvements**: Users can suggest improvements like new parks, better public transport, etc.
- **Emergency Services Information**: Provides contact information for emergency services.
- **Public Services Information**: Offers information about various public services in Warsaw.
- **Leaderboard**: Displays top contributors to the community.
- **Geolocation Handling**: Checks if the reported issue is within Warsaw's city limits.

## Files

1. **image_processor.py**: Handles image processing from Telegram, interacts with Gemini API to classify images and respond appropriately.
2. **send_message.py**: Contains functions to send messages via the Telegram bot.
3. **database_connection.py**: Manages database connections and inserts messages into a MySQL database.
4. **location_processor.py**: Checks if the provided geolocation is within Warsaw's city limits.
5. **command_support.py**: Processes specific keywords in incoming messages and sends appropriate responses.

## Setup

### Prerequisites

- Python 3.7+
- MySQL database
- Telegram Bot Token
- Google API Key for Generative AI
- ngrok (for webhook setup)

### Installation

1. **Clone the repository**

```sh
git clone https://github.com/yourusername/warsaw-citizen-support-bot.git
cd warsaw-citizen-support-bot
```

2. **Install dependencies**

```sh
pip install -r requirements.txt
```

3. **Set environment variables**

Create a `.env` file in the root directory of your project and add the following:

```sh
TELEGRAM_BOT_TOKEN=<Your_Telegram_Bot_Token>
GOOGLE_API_KEY=<Your_Google_API_Key>
DB_ENDPOINT=<Your_Database_Endpoint>
DB_USERNAME=<Your_Database_Username>
DB_PASSWORD=<Your_Database_Password>
DB_NAME=<Your_Database_Name>
```

4. **Setup the MySQL database**

```sql
CREATE TABLE messages (
    message_id VARCHAR(255) PRIMARY KEY,
    user_id VARCHAR(255),
    timestamp VARCHAR(255),
    text TEXT,
    picture VARCHAR(255),
    lon FLOAT,
    lat FLOAT,
    category VARCHAR(255)
);
```

### Setting up ngrok

To expose your local server to the internet, you need to use ngrok:

1. **Download and install ngrok**

```sh
https://ngrok.com/download
```

2. **Start ngrok**

```sh
ngrok http 5000
```

3. **Copy the Forwarding URL**

ngrok will provide a forwarding URL that looks something like `https://abcd1234.ngrok.io`. You will use this URL to set up the Telegram webhook.

4. **Set up the Telegram webhook**

Replace `<NGROK_URL>` with your ngrok forwarding URL:

```sh
curl -F "url=<NGROK_URL>/webhook" https://api.telegram.org/bot<Your_Telegram_Bot_Token>/setWebhook
```

### Running the Bot

```sh
python bot.py
```

### Files Description

#### image_processor.py

This script processes images received from Telegram, interacts with the Gemini API, classifies the images into predefined categories, and responds with appropriate messages.

#### send_message.py

Contains the `replyinput` function to send messages via the Telegram bot.

#### database_connection.py

Manages the database connection and inserts messages into the MySQL database. It extracts information such as user ID, message text, picture, and location from the received data.

#### location_processor.py

Contains the `is_within_warsaw` function that checks if the provided coordinates are within the bounding box of Warsaw.

#### command_support.py

Processes specific keywords in incoming messages and sends predefined responses based on the keyword detected.

## Contributing

Feel free to submit issues, fork the repository, and send pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to Vishnu Kumar for creating the initial version of this project.

---

By following this `README.md`, users should be able to understand the purpose of your project, set it up, and run the bot. If there are any additional scripts or configurations, you can extend the `README.md` accordingly.
