#--| This code created by: Jisshu_bots & SilentXBotz |--#
import re
import hashlib
import asyncio
from info import *
from utils import *
from pyrogram import Client, filters, enums
from database.users_chats_db import db
from database.ia_filterdb import save_file, unpack_new_file_id
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import aiohttp
from typing import Optional
from collections import defaultdict
import asyncio
import aiohttp
import hashlib

CAPTION_LANGUAGES = ["Bhojpuri", "Hindi", "Bengali", "Tamil", "English", "Bangla", "Telugu", "Malayalam", "Kannada", "Marathi", "Punjabi", "Bengoli", "Gujrati", "Korean", "Gujarati", "Spanish", "French", "German", "Chinese", "Arabic", "Portuguese", "Russian", "Japanese", "Odia", "Assamese", "Urdu"]

UPDATE_CAPTION = """<b><blockquote>📫 𝖭𝖤𝖶 𝖥𝖨𝖫𝖤 𝖠𝖣𝖣𝖤𝖣 ✅</blockquote>

🚧  Title : {}
🎧 𝖠𝗎𝖽𝗂𝗈 : {}
🔖 Type : {}
<blockquote>🚀 Telegram Files ✨</blockquote>

{}
<blockquote>〽️ Powered by @Anuj_bots</b></blockquote>
"""

QUALITY_CAPTION = """📦 {} : {}\n"""

notified_movies = set()
movie_files = defaultdict(list)
POST_DELAY = 10 
processing_movies = set() 

media_filter = filters.document | filters.video | filters.audio

@Client.on_message(filters.chat(CHANNELS) & media_filter)
async def media(bot, message):
    bot_id = bot.me.id
    media = getattr(message, message.media.value, None)
    if media.mime_type in ['video/mp4', 'video/x-matroska','document/mp4']: 
        media.file_type = message.media.value
        media.caption = message.caption
        success_sts = await save_file(media)
        if success_sts == 'suc' and await db.get_send_update_status(bot_id):
            file_id, file_ref = unpack_new_file_id(media.file_id)
            await queue_movie_file(bot, media)
            

async def queue_file(bot, media):
    try:
        # Extracting information for educational content
        file_name_cleaned = await content_name_format(media.file_name)
        caption_cleaned = await content_name_format(media.caption)

        # Example: Extracting details from file_name or caption
        # Format: course_name, subject, chapter, lecture_number, content_type
        # e.g., "Physics Wallah Yakkeen 2.0 Physics Ch-2 L-1 Assignments.pdf"

        course_match = re.search(r"(Yakkeen 2.0|Lakshya Batch|Prayas Batch)", file_name_cleaned, re.IGNORECASE)
        course_name = course_match.group(0) if course_match else "Unknown Course"

        subject_match = re.search(r"(Physics|Chemistry|Maths|Biology)", file_name_cleaned, re.IGNORECASE)
        subject = subject_match.group(0) if subject_match else "Unknown Subject"

        chapter_match = re.search(r"Ch-(\d+)", file_name_cleaned, re.IGNORECASE)
        chapter = f"Chapter {chapter_match.group(1)}" if chapter_match else "Unknown Chapter"

        lecture_match = re.search(r"L-(\d+)", file_name_cleaned, re.IGNORECASE)
        lecture_number = f"Lecture {lecture_match.group(1)}" if lecture_match else "Unknown Lecture"

        content_type_match = re.search(r"(Assignments|Classnotes|Lecture|Solutions|DPP)", file_name_cleaned, re.IGNORECASE)
        content_type = content_type_match.group(0) if content_type_match else "General Document"

        # Determine file format (e.g., PDF, MP4)
        file_extension = media.file_name.split(".")[-1].upper() if "." in media.file_name else "UNKNOWN"

        file_size_str = format_file_size(media.file_size)
        file_id, file_ref = unpack_new_file_id(media.file_id)

        # Use a unique key for grouping, e.g., based on course, subject, chapter
        grouping_key = "f{course_name}_{subject}_{chapter}"

        movie_files[grouping_key].append({
            "course_name": course_name,
            "subject": subject,
            "chapter": chapter,
            "lecture_number": lecture_number,
            "content_type": content_type,
            "file_format": file_extension,
            "file_id": file_id,
            "file_size": file_size_str,
            "caption": caption_cleaned,
            "original_file_name": media.file_name
        })

        if grouping_key in processing_movies:
            return

        processing_movies.add(grouping_key)
        try:
            # Adjust POST_DELAY as needed, maybe longer for educational content to group more files
            await asyncio.sleep(5) # Reduced delay for testing, adjust as needed
            if grouping_key in movie_files:
                await send_update(bot, grouping_key, movie_files[grouping_key])
                del movie_files[grouping_key]
        finally:
            processing_movies.remove(grouping_key)

    except Exception as e:
        print(f"Error in queue_file: {e}")
        if grouping_key in processing_movies:
            processing_movies.remove(grouping_key)
        await bot.send_message(LOG_CHANNEL, f'Failed to process educational file. Error - {e}')

async def send_update(bot, grouping_key, files):
    try:
        if grouping_key in notified_movies:
            return
        notified_movies.add(grouping_key)

        # Extract common details from the first file in the group
        first_file = files[0]
        course_name = first_file["course_name"]
        subject = first_file["subject"]
        chapter = first_file["chapter"]

        # Prepare the list of files with their types and sizes
        file_details_list = []
        for file in files:
            file_details_list.append(
                f"• {file['content_type']} ({file['lecture_number']}) - {file['file_format']} "
                f"<a href='https://t.me/{temp.U_NAME}?start=file_0_{file['file_id']}}'>{file['file_size']}</a>"
            
        files_text = "\n".join(file_details_list)

        # You might want to fetch a generic image for educational content or allow custom images
        # For now, using a placeholder or a default image
        image_url = "https://ibb.co/bgxC53yR" # Placeholder, replace with a relevant image

        # Construct the full caption for educational content
        full_caption = (
            f"📚 **{course_name}**\n\n"
            f"✨ **Subject:** {subject}\n"
            f"📖 **{chapter}**\n\n"
            f"🔗 **Available Content:**\n{files_text}\n\n"
            f"_Join our channel for more educational resources!_"
         )

        # Send the update to the designated channel
        # Assuming MOVIE_UPDATE_CHANNEL can be repurposed or a new EDUCATIONAL_UPDATE_CHANNEL is defined
        update_channel = await db.update_channel_id() # Reusing, consider renaming in info.py
        await bot.send_photo(
            chat_id=update_channel if update_channel else UPDATE_CHANNEL,
            photo=image_url,
            caption=full_caption,
            parse_mode=enums.ParseMode.HTML
        )
    except Exception as e:
        print(f'Failed to send update. Error - {e}')
        await bot.send_message(LOG_CHANNEL, f'Failed to send update. Error - {e}')

# Removed get_imdb and fetch_movie_poster as they are movie-specific
# You might want to implement similar functions for fetching educational content metadata or images if available

def generate_unique_id(content_name):
    return hashlib.md5(content_name.encode('utf-8')).hexdigest()[:5]

# Simplified quality extraction, can be adapted for educational content types
async def get_qualities(text):
    # For educational content, 'quality' might refer to resolution for videos or 'HD' for documents
    # You can define specific keywords for educational content types here
    Type = ["CLASSNOTES", "LECTURE", "DPP", "DPP QUIZ", "ASSIGNMENT", "HOMEWORK", "PLANNER", "SHORTS NOTES", "PYQS"]
    found_Type = [t for t in type if q.lower() in text.lower()]
    return ", ".join(found_type) or "General"

async def Anuj_qualities(text, file_name):
    # This function might be less relevant for diverse educational content, or can be adapted
    # For now, returning a generic 'Standard' or based on file type
    combined_text = (text.lower() + " " + file_name.lower()).strip()
    if "pdf" in combined_text:
        return "PDF Document"
    elif "mp4" in combined_text or "mkv" in combined_text:
        return "Video Lecture"
    return "Standard"

async def content_name_format(file_name):
  # This function cleans up the file name for better parsing
  filename = re.sub(r'http\S+', '', re.sub(r'@\w+|#\w+', '', file_name ).replace('_', ' ').replace('[', '').replace(']', '').replace('(', '').replace(')', '').replace('{', '').replace('}', '').replace('.', ' ').replace('@', '').replace(':', '').replace(';', '').replace("'", '').replace('-', '').replace('!', '')).strip()
  return filename

def format_file_size(size_bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} PB"
