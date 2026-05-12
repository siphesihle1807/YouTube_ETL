import json
import requests

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")
API_KEY = os.getenv("API_KEY")

url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle=BaileySarian&key={API_KEY}"

def get_playlist_id():
    try:
        response = requests.get(url)

        response.raise_for_status()

        data = response.json()

        channel_items = data["items"][0]
        channel_playlist_id = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]
        return channel_playlist_id
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None 
    
if __name__ == "__main__":
    get_playlist_id()
    print(get_playlist_id())