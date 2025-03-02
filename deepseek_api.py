from dotenv import load_dotenv
from instagrapi import Client
from instagrapi.exceptions import LoginRequired
from openai import OpenAI
import os 
import json
import logging

load_dotenv() # For script to access env file
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

API_KEYS = os.getenv("DEEPSEEK_API_KEYS")
API_URL = "https://api.deepseek.com"

system_prompt = (
    "You are a chat bot for a University Society/ Club. "
    "You will respond to inquiries from people interested in our society/ club. "
    "If they ask to join redirect them to the university website and instruct them on how to join."
    "If they ask about upcoming events redirect them to the pinned post of our instagram page."
    "If they ask any other questions not relevent to the society/ club, politely end the conversation."
)

def POST_deepseek(regular_text):

    """
    Sends DM messages to the Deepseek API to generate a human like response.
    """
    try:
        client = OpenAI(api_key=f"{API_KEYS}", base_url=f"{API_URL}")

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": regular_text },
            ],
            stream=False
        )

        print(f"Response for {regular_text} from Deepseek: {response.choices[0].message.content}")
    except Exception as e:
        logger.info("Unable to fetch Deepseek's response %s" % e)

def process_text(new_messages):

    """
    Handles processing the text to make sure no trivial messages are sent. 
    Also, makes sure that regular and pending DMs are separated 
    """
    try:
        text = new_messages.values() 
        latest_DM = [next(iter(item.values())) for item in text]
        print(f"Inside deepseek_api latest_DM: {latest_DM} \n") # debugging
        print(f"Inside deepseek_api text: {text}\n") # debugging
        

        if latest_DM:
            if len(latest_DM[0]) > 2:
                regular_text = latest_DM[0]
                print(f"Inside deepseek_api: {regular_text} \n") # debugging
                POST_deepseek(regular_text)    

                if len(latest_DM) >= 2 and len(latest_DM[1]) > 2:
                    pending_text = latest_DM[1]
                    print(f"Inside deepseek_api: {pending_text} \n") # debugging
                    POST_deepseek(pending_text)  
            else:
                pass
        else:
            print(f"Maybe there are no new messages: {new_messages}")
            
        
    except Exception as e:
        logger.info("Couldn't isolate text: %s" % e)

    
