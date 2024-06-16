Certainly! Here's an updated version of the `DESCRIPTION.md` file with additional information about the app's objectives and potential future developments:

---

# Warsaw Citizen Support Bot

## Overview

The Warsaw Citizen Support Bot is a Telegram bot designed to streamline citizen interactions with municipal services in Warsaw. By leveraging Telegram's platform, the bot consolidates multiple functionalities into one accessible interface, thereby eliminating the need for multiple standalone applications. This approach aims to enhance user convenience and engagement while fostering a cleaner and more efficient urban environment.

## Objectives

- **Consolidation of Services**: The bot integrates various services such as issue reporting, improvement suggestions, emergency service information, and public service details into a single platform. This consolidation reduces the clutter of multiple apps and provides a unified solution for citizen interactions with city services.

- **Simplicity and Accessibility**: By utilizing Telegram as the communication channel, the bot ensures widespread accessibility. Citizens can easily report issues, suggest improvements, or access vital city information directly through their Telegram app, eliminating the barrier of downloading and managing additional applications.

- **Potential for Future Expansion**: While currently focused on communication and information provision, the bot has the potential for future expansions such as payment functionalities and additional service provisions. These developments could further streamline citizen interactions and enhance service delivery across Warsaw.

## Features

- **Issue Reporting**: Citizens can report issues like potholes, waste management problems, etc., via text descriptions or images, facilitating prompt city response and action.
  
- **Improvement Suggestions**: Users can suggest improvements for the city, such as new parks or enhanced public transport options, contributing to urban development and citizen satisfaction.

- **Emergency Services Information**: Provides critical contact numbers and resources for emergencies, including fire, ambulance, and police services, ensuring citizen safety and preparedness.

- **Public Services Information**: Offers comprehensive details about various public services, including waste management schedules, public transport routes, and energy efficiency tips, promoting informed citizen engagement.

- **Leaderboard**: Recognizes and showcases top contributors who have made significant impacts within the community, fostering a sense of civic pride and participation.

- **Geolocation Handling**: Verifies whether reported issues are within Warsaw's city limits using geolocation data, ensuring accurate service allocation and response.

## Tech Stack

- **Python**: Backend programming language.
- **Flask**: Web framework for creating the bot's API endpoints.
- **MySQL**: Database management system for storing user interactions and issue reports.
- **Telegram Bot API**: Interface for sending and receiving messages from Telegram users.
- **Google Generative AI**: Used for natural language processing and understanding user queries and responses.
- **Ngrok**: Utility for exposing local servers to the internet, used to set up webhooks with Telegram API.

## Setup and Usage

### Prerequisites

- Python 3.7+
- MySQL database
- Telegram Bot Token
- Google API Key for Generative AI
- Ngrok (for setting up webhooks)

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/warsaw-citizen-support-bot.git
   cd warsaw-citizen-support-bot
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   Create a `.env` file in the project root and add the following:

   ```sh
   TELEGRAM_BOT_TOKEN=<Your_Telegram_Bot_Token>
   GOOGLE_API_KEY=<Your_Google_API_Key>
   DB_ENDPOINT=<Your_Database_Endpoint>
   DB_USERNAME=<Your_Database_Username>
   DB_PASSWORD=<Your_Database_Password>
   DB_NAME=<Your_Database_Name>
   ```

4. Set up MySQL database:

   Run the SQL script provided in `database_connection.py` to create the necessary `messages` table.

### Setting up Ngrok

1. Download and install Ngrok from [ngrok.com](https://ngrok.com/download).

2. Start Ngrok to expose your local server:

   ```sh
   ngrok http 5000
   ```

3. Copy the Ngrok forwarding URL provided (e.g., `https://abcd1234.ngrok.io`).

### Setting up Telegram Webhook

Replace `<NGROK_URL>` with your Ngrok forwarding URL in the following command:

```sh
curl -F "url=<NGROK_URL>/webhook" https://api.telegram.org/bot<Your_Telegram_Bot_Token>/setWebhook
```

### Running the Bot

```sh
python bot.py
```

### Files Description

- **bot.py**: Initializes the Flask app, defines webhook endpoints, and handles incoming Telegram messages.
- **image_processor.py**: Processes images using the Gemini API for classification and responds based on the content.
- **send_message.py**: Sends messages back to Telegram users using the bot API.
- **database_connection.py**: Manages MySQL connections, inserts user messages into the database, and retrieves data for processing.
- **location_processor.py**: Checks if geolocation coordinates are within Warsaw's city limits.
- **command_support.py**: Processes specific keywords in messages and sends predefined responses.

## Future Directions

While currently focused on communication and information provision, future enhancements could include:

- **Payment Integration**: Facilitating transactions for city services like parking permits or event registrations.
- **Expanded Service Offerings**: Adding functionalities for service requests and feedback loops for city improvement initiatives.
- **Enhanced AI Capabilities**: Leveraging AI for predictive analytics to anticipate citizen needs and optimize service delivery.
