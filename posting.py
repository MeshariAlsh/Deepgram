from dotenv import load_dotenv
from instagrapi import Client
from instagrapi.exceptions import LoginRequired
import os 
import json
import logging

load_dotenv() # For script to access env file
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

image_path = 'posts/photos/ps7.png'
caption = 'Leaked Playstation 7'

def load_scheduled_posts():

    """
    Loads the path and caption of pre-defined posts to be published on the instagram account. 
    """
    try:
        with open("scheduled_posts", "r") as f:
            new_posts = json.load(f)
            return new_posts

    except Exception as e:
       logger.info("Couldn't load post from JSON file: %s" % e)

def  process_posts():

    #TODO add block here the checks if the caption was written before by comaparing it with a json of all successful posts. if written before ignore it and dont post. 

    post_into_list = load_scheduled_posts()
    #TODO add block here the sends the new and unrepititve posts  


def upload_photo_post(user):

    process_posts()

    """
    Uploads an image with a predefined caption (see line 15) to the instagram account logged in (see line 11 & 12). 
    """

    if not os.path.exists(image_path):
        logger.error(f"Image Not Found:{image_path}")
        return
    
    try:
        media = user.photo_upload(
            path=image_path, 
            caption=caption
        )
        if media:
            logger.info("Succesfully Posted Photo.")
            print(media)
    except Exception as e:
        logger.error(f"Error posting photo: {str(e)}")
