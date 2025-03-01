# Instagram DM Automation Bot with Deepseek Chat API

This project automates the process of reading Instagram Direct Messages (DMs) and generating human-like responses using the Deepseek Chat API. It also supports posting images to Instagram. The project is designed with modularity and error handling in mind, making it easy to maintain and extend.

## Features

- **Instagram DM Processing:**  
  Reads unread DMs from both the regular and pending inbox.
  
- **Deepseek Chat Integration:**  
  Uses Deepseek Chat API to generate human-like responses based on incoming DM content.
  
- **Photo Posting:**  
  Uploads photos with captions to Instagram.
  
- **Logging & Error Handling:**  
  Detailed logging and try/except blocks to help diagnose issues and improve robustness.
  
- **Environment-based Configuration:**  
  Sensitive information like API keys and login credentials are loaded from environment variables.

## Project Structure

- **automate_page.py:**  
  Main entry point for the project. Handles Instagram login, sets delays to mimic human behavior, and triggers DM processing.

- **message_handler.py:**  
  Contains functions for saving, loading, and processing DM threads. It also calls the Deepseek API module to generate responses.

- **deepseek_api.py:**  
  Integrates with the Deepseek Chat API to generate responses for incoming messages. Includes logic to ignore trivial messages.

- **posting.py:**  
  Provides functionality to upload a photo to Instagram with a predefined caption.

## Prerequisites

- **Python 3.8+**  
- **Dependencies:**  
  Install the required packages using:
  ```bash
  pip install -r requirements.txt

### Environment Variables

Create a .env file in the root directory of the project to store sensitive information. For example:
```
USERNAME=your_instagram_username
PASSWORD=your_instagram_password
DEEPSEEK_API_KEYS=your_deepseek_api_key
```
## Roadmap and Future Features

- **Automated Response Delivery:**  
  A function to send the generated response back to the user who inquired via DM is planned. This will complete the interactive loop of the bot.

- **Post Scheduler:**  
  A scheduling system for automating photo posting will be added, allowing for timed content releases.

- **Improved Error Handling & Retry Logic:**  
  Enhance the robustness of API calls by adding retry mechanisms and more detailed error reporting.


