import os
import subprocess
from pyrogram import Client, filters
from asyncio import run
from config import api_id, api_hash, bot_token

app = Client("video_note_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


@app.on_message(filters.command("start") & filters.private)
async def send_welcome(client, message):
    # Send a simple welcome message when the user starts the bot
    await message.reply(
        "Welcome! 👋\n\nSend me a video or a GIF, and I'll process it for you! 🎥✨"
    )
    print("Sent welcome message to user.")  # Feedback in IDLE


@app.on_message(filters.video & filters.private)
async def process_video(client, message):
    await process_media(client, message, "video")


@app.on_message(filters.animation & filters.private)
async def process_gif(client, message):
    await process_media(client, message, "gif")


async def process_media(client, message, media_type):
    media_file = message.video.file_id if media_type == "video" else message.animation.file_id
    extension = "mp4" if media_type == "video" else "gif"
    input_path = f"downloads/{media_file}.{extension}"
    output_path = f"downloads/{media_file}_circle.mp4"

    # Ensure the downloads directory exists
    os.makedirs("downloads", exist_ok=True)

    # Send feedback that the process has started
    await message.reply(f"Processing your {media_type}... This may take a moment. 🔄")
    print(f"Started {media_type} processing.")  # Feedback in IDLE

    # Download the media file
    await message.download(input_path)
    print(f"{media_type.capitalize()} downloaded to: {input_path}")  # Feedback in IDLE

    # Run the FFmpeg command for processing
    command = (
        f"ffmpeg -i {input_path} -vf \"crop='min(iw,ih)':'min(iw,ih)',scale=640:640\" "
        f"-c:v libx264 -crf 23 -preset veryfast -pix_fmt yuv420p {output_path}"
    )
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"FFmpeg error: {result.stderr}")
        await message.reply("There was an error processing your video. ❌")
        return

    print("FFmpeg command executed.")  # Feedback in IDLE

    # Feedback when processing is done
    await message.reply(f"Your {media_type} has been processed! 🎬")
    print(f"{media_type.capitalize()} processing completed.")  # Feedback in IDLE

    # Send the processed video
    await message.reply_video_note(output_path)
    print(f"Processed {media_type} sent: {output_path}")  # Feedback in IDLE

    # Clean up files
    os.remove(input_path)
    os.remove(output_path)
    print("Temporary files removed.")  # Feedback in IDLE


app.run()
