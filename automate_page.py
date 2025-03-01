from message_handler import get_unread_DMs, load_latest_messages, save_new_messages
from dotenv import load_dotenv
from instagrapi import Client
from instagrapi.exceptions import LoginRequired
import os 
import json
import logging

load_dotenv() # For script to access env file
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

def login_user(user):
    """
    Attempts to login to Instagram using either the provided session information
    or the provided username and password.
    """
    login_via_session = False
    login_via_pw = False

    try:
        session = user.load_settings("session.json")

        if session:
        
            user.set_settings(session)
            user.login(USERNAME, PASSWORD)
            user.dump_settings("session.json")

            # check if session is valid
            try:
                user.get_timeline_feed()
            except LoginRequired:
                logger.info("Session is invalid, need to login via username and password")

                old_session = user.get_settings()

                # use the same device uuids across logins
                user.set_settings({})
                user.set_uuids(old_session["uuids"])

                user.login(USERNAME, PASSWORD)
            login_via_session = True
    except FileNotFoundError:
            logger.info("Did not find the session file: ")

    except Exception as e:
            logger.info("Couldn't login user using session information: %s" % e)

    if not login_via_session:
        try:
            logger.info("Attempting to login via username and password. username: %s" % USERNAME)
            if user.login(USERNAME, PASSWORD):
                user.dump_settings("session.json") # To create the session.json if first time running script
                login_via_pw = True
        except Exception as e:
            logger.info("Couldn't login user using username and password: %s" % e)

    if not login_via_pw and not login_via_session:
        raise Exception("Couldn't login user with either password or session")

def main():

    user = Client() # An instance of class Client to send request to instagram
    user.delay_range = [5, 10] # mimic human interaction
    login_user(user) 
    #upload_photo_post(user)

    
    get_unread_DMs(user)
    



if __name__ == "__main__":
    main()
