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
    client = OpenAI(api_key=f"{API_KEYS}", base_url=f"{API_URL}")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": regular_text },
        ],
        stream=False
    )

    print(f"Response for {regular_text} {response.choices[0].message.content}")


def process_text():

    """
    Handles processing the text to make sure no trivial messages are sent. 
    Also, makes sure that regular and pending DMs are separated 
    """
    try:
        #text = recent_messages.values() for later 
        text_into_list = [{'1234567': 'Yo bro?'}, {'11223344': 'Amigoos'}] # Example, I did lot of testing in sequence and my instagram account is under suspicion of botting, lol
        latest_DM = [next(iter(item.values())) for item in text_into_list]
        print(f"Inside deepseek_api: {latest_DM}") # debugging
        
        if latest_DM:
            if len(latest_DM[0]) < 2:
                pass
            elif len(latest_DM[1]) < 2:
                pass
            else:
                regular_text = latest_DM[0]
                pending_text = latest_DM[1]
                POST_deepseek(regular_text)    
        else:
            pass
            # do nothing as there are no new messages.
   
    except Exception as e:
        logger.info("Couldn't isolate text: %s" % e)

    
process_text()