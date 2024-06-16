# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 03:00:27 2024

@author: Vishnu Kumar
"""
import json
from send_messages import replyinput


def check_keywords(text):
    if 'start' in text.lower():
        return """
        Welcome to the Warsaw Citizen Support Bot!

        🇵🇱 Whether you need to report an issue or suggest improvements for our beautiful city, we're here to help.

        How can I assist you today?

            🛠 Report an Issue
            💡 Suggest an Improvement
            🏆 View Leaderboard
            ℹ️ Get Information about City Services
        To get started, simply type one of the commands below:

            /report - Report an issue (e.g., potholes, waste management problems, etc.)
            /suggest - Suggest an improvement (e.g., new park, better public transport, etc.)
            /leaderboard - View the leaderboard of top contributors
            /info - Get information about public services
        🏅 Leaderboard Incentive:
            The top citizens who contribute the most in a year will receive a tax cut for the year as a token of appreciation for their efforts!

        Thank you for helping us make Warsaw a better place!
    
        """
    elif 'leaderboard' in text.lower():
        return """
            🏆 Explore the Warsaw Community Leaderboard! 🌍

Discover who's making a significant impact in Warsaw! Visit our leaderboard to see the top contributors and their achievements. Click here to view the leaderboard and celebrate our community heroes!


https://mojawarszawa.streamlit.app/

Keep contributing and see your name at the top! Let's build a better Warsaw together. 🌟
        
        """
        
    elif 'emergency' in text.lower():
        return """
    *Emergency Services Information*

Welcome to the Emergency Services section. Here are important contact numbers and resources for emergencies in Warsaw:

🚒 Fire Department: 112 or (https://www.warszawa-straz.pl)
🚑 Ambulance: 999 or (https://www.example.com/ambulance)
🚓 Police: 997 or (https://www.example.com/police)

For immediate assistance, please dial the emergency number directly.

Stay safe and informed!

    """
    elif 'help' in text.lower():
        return """
        Welcome to the Warsaw Citizen Support Bot!

        🇵🇱 Whether you need to report an issue or suggest improvements for our beautiful city, we're here to help.

        How can I assist you today?

            🛠 Report an Issue
            💡 Suggest an Improvement
            🏆 View Leaderboard
            ℹ️ Get Information about City Services
        To get started, simply type one of the commands below:

            /report - Report an issue (e.g., potholes, waste management problems, etc.)
            /suggest - Suggest an improvement (e.g., new park, better public transport, etc.)
            /leaderboard - View the leaderboard of top contributors
            /info - Get information about public services
        🏅 Leaderboard Incentive:
            The top citizens who contribute the most in a year will receive a tax cut for the year as a token of appreciation for their efforts!

        Thank you for helping us make Warsaw a better place!
    
        """
    elif 'info' in text.lower():
        return """
    
*Public Services Information*

Welcome to the Warsaw Citizen Support Bot's information section! Below you will find brief details and direct links about various public services available to you in Warsaw:

*🛠 Report an Issue*
Report issues like potholes or waste management problems. (https://www.warsaw.pl/report-issue)

*💡 Suggest an Improvement*
Share your suggestions for city improvements. (https://www.warsaw.pl/suggest-improvement)

*📊 View Leaderboard*
Check the top contributors and their impact. (https://www.warsaw.pl/leaderboard)

*🚮 Waste Management*
- Collection schedules and recycling guidelines. (https://www.warsaw.pl/waste-management)
- Hazardous waste disposal info. (https://www.warsaw.pl/hazardous-waste)

*🚍 Transportation*
- Public transport routes and schedules. (https://www.ztm.waw.pl)
- Bike-sharing program Veturilo. (https://www.veturilo.waw.pl)
- Electric scooter rentals. (https://www.li.me), [Bird](https://www.bird.co)

*💧 Water Conservation*
- Tips on conserving water. (https://www.mpwik.com.pl)
- Information on water quality. (https://www.mpwik.com.pl)

*⚡ Energy Efficiency*
- Energy saving tips and renewable energy projects.(https://www.warsaw.pl/energy)
- Energy-efficient appliances info. (https://www.energylabel.eu)

*🏙️ Urban Planning*
- Updates on development projects. (https://www.warsaw.pl/urban-planning)
- Zoning laws and public consultations. (https://www.warsaw.pl/zoning)

*📚 Education and Awareness*
- Educational resources and public campaigns. (https://www.warsaw.pl/education)
- Workshops and seminars. (https://www.warsaw.pl/workshops)

*🌿 Health and Environment*
- Health tips and environmental protection info. (https://www.warsaw.pl/health), [Environmental Protection](https://www.warsaw.pl/environment)
- Air quality updates.(https://www.warsaw.pl/air-quality)

*🌾 Sustainable Agriculture*
- Local farmers' markets and community gardens. (https://www.warsaw.pl/farmers-markets), [Community Gardens](https://www.warsaw.pl/community-gardens)

*🎨 Community Engagement*
- Cultural events and community projects. (https://www.warsaw.pl/culture), [Community Projects](https://www.warsaw.pl/community-projects)
- Volunteering opportunities. (https://www.warsaw.pl/volunteer)

*🏗️ Sustainable Infrastructure*
- Information on green buildings and eco-friendly public spaces. (https://www.warsaw.pl/green-buildings), [Public Spaces](https://www.warsaw.pl/public-spaces)
- Infrastructure projects. (https://www.warsaw.pl/projects)

*💼 Economic Incentives*
- Incentives for eco-friendly practices and green jobs.(https://www.warsaw.pl/incentives), [Green Jobs](https://www.warsaw.pl/green-jobs)
- Business support resources. (https://www.warsaw.pl/business-support)

*🌳 Eco-Friendly Tourism*
- Eco-friendly attractions and activities.(https://www.warsaw.pl/eco-tourism)
- Sustainable accommodations. (https://www.warsaw.pl/green-hotels)

*🚓 Police and Safety*
- Local police services and safety tips. (https://www.warsaw.pl/police), [Safety Tips](https://www.warsaw.pl/safety)
- Reporting non-emergency issues. (https://www.warsaw.pl/report-issue)

For further assistance, feel free to reach out to us. Thank you for helping to make Warsaw a better place!

        """
    return "Please try the /help for more information"

def is_bot_command(message_json):
    try:
        # Check if 'entities' is present in the 'message' part of the JSON
        if 'message' in message_json and 'entities' in message_json['message']:
            entities = message_json['message']['entities']
            for entity in entities:
                if entity['type'] == 'bot_command':
                    replyinput(message_json['message']['chat']['id'], check_keywords(message_json['message']['text']))
                    return True
        return False
    except (KeyError, TypeError, json.JSONDecodeError):
        return False