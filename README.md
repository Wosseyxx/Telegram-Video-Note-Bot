VIDEO NOTE BOT

This bot processes videos and GIFs sent by users, turning them into circular video notes. It's built using Python, leveraging the Pyrogram library and FFmpeg for media processing.

** FEATURES
Start Command: Sends a welcome message to the user.

Video & GIF Processing: Converts video and GIF files into circular video notes.

Feedback: The bot sends status updates to inform the user about the processing progress.

Temporary File Cleanup: After processing, the bot deletes the temporary media files.

** REQUIREMENTS

Python 3.8 or higher & pyrogram library & ffmpeg (installed on the system) & Telegram Bot Token, API ID, and API Hash (from Telegram Developer)

** INSTALLATION

Clone this repository:

git clone https://github.com/yourusername/video-note-bot.git

cd video-note-bot

Install the required dependencies:

pip install -r requirements.txt

Set up your Telegram bot by creating a bot on Telegram via BotFather.

Create a config.py file with your credentials:

api_id = 'YOUR_API_ID'

api_hash = 'YOUR_API_HASH'

bot_token = 'YOUR_BOT_TOKEN'

Install FFmpeg on your system if you haven't already.

* On Linux:

sudo apt-get install ffmpeg

* On macOS (using Homebrew):

brew install ffmpeg

* On Windows: Download FFmpeg from https://ffmpeg.org/download.html and add it to your system PATH.

** USAGE

Start a chat with the bot on Telegram and type /start to receive a welcome message.

Send a video or GIF, and the bot will process it, converting it into a circular video note and send it back to you.

Example Commands

/start: Get the welcome message.

Send any video or GIF, and it will be processed into a circular video note.


** ACKNOWLEDGEMENTS

Pyrogram for the Telegram API wrapper.

FFmpeg for media processing.
