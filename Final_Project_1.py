import re
import time
import multiprocessing
import threading
import logging
import os
from pytube import YouTube
from moviepy.editor import VideoFileClip
from pathlib import Path
import speech_recognition as sr

# List to store the extracted video names
videoenames = []

# Create a lock object to ensure only one thread writes to the file at a time
file_lock = threading.Lock()

# Ensure the directories exist before configuring the logger
log_directory = 'video_records'
os.makedirs(log_directory, exist_ok=True)

# Directory to save downloaded videos
download_directory = 'downloaded_videos'
os.makedirs(download_directory, exist_ok=True)

# Directory to save extracted audio files
audio_directory = 'audios'
os.makedirs(audio_directory, exist_ok=True)

# Directory to save transcriptions
text_directory = 'texts'
os.makedirs(text_directory, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=os.path.join(log_directory, 'download_log.txt'),
    level=logging.INFO,
    format='"Timestamp": %(asctime)s, "URL":"%(url)s", "Thread": "%(threadName)s"',
    datefmt='%H:%M, %d %b %Y'
)
logger = logging.getLogger()

def video_record(url, thread_name):
    # Create path to the log file (download_log.txt) located within a directory specified by log_directory
    file_path = os.path.join(log_directory, 'download_log.txt')
    # Ensure threads don't write simultaneously
    with file_lock:
         # Open the file in append mode.
        with open(file_path, "a") as file:
            # Create a log entry with the generated phrase
            log_entry = f'"Timestamp": {time.strftime("%H:%M, %d %b %Y")}, "URL":"{url}", "Thread":"{thread_name}"\n'
             # Write the log entry to the file
            file.write(log_entry)

def download_video_and_log(url):
    download_video(url)
    # Record which video was downloaded by which process or thread
    thread_name = threading.current_thread().name
    video_record(url, thread_name)

# Extract the URLs from video_urls.txt
def extract_urls(youtube_videos):
    video_urls = []
    with open(youtube_videos, 'r', encoding='utf-8') as file:
        for url in file:
            url = url.strip()
            video_urls.append(url)
            # Regex to extract the name of the video
            pattern = r'[^/]+$'
            # Search the URL for the filename using the regex pattern
            videoename = re.search(pattern, url).group(0)
            videoenames.append(videoename)
    return video_urls

# Download video content
def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        filename = stream.download(output_path=download_directory)
        print(f'{url} downloaded.')
        extract_audio(filename, audio_directory)
    except Exception as e:
        print(f'Error downloading {url}: {e}')

def serial_downloader(video_urls):
    start = time.perf_counter()
    for video in video_urls:
        download_video_and_log(video)
    end = time.perf_counter()
    print(f'Serial run took {round(end-start, 2)} second(s)')

def parallel_downloader(video_urls):
    start = time.perf_counter()
    processes = []
    for video in video_urls:
        p = multiprocessing.Process(target=download_video, args=(video,))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    end = time.perf_counter()
    print(f'Parallel run took {round(end-start, 2)} second(s)')

def parallel_downloader1(video_urls):
    start = time.perf_counter()
    threads = []
    for video in video_urls:
        t = threading.Thread(target=download_video_and_log, args=(video,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    end = time.perf_counter()
    print(f'Parallel run with threads took {round(end-start, 2)} second(s)')

# Limit to 5 concurrent downloads
semaphore = threading.Semaphore(5)

def parallel_downloader2(video_urls):
    start = time.perf_counter()
    
    def download_with_semaphore(video):
        with semaphore:
            download_video_and_log(video)
    
    threads = []
    for video in video_urls:
        t = threading.Thread(target=download_with_semaphore, args=(video,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    
    end = time.perf_counter()
    print(f'Parallel run with limited threads took {round(end-start, 2)} second(s)')

def extract_audio(video_path, audio_directory):
    Path(audio_directory).mkdir(parents=True, exist_ok=True)
    
    try:
        video = VideoFileClip(video_path)
        video_path_obj = Path(video_path)
        audio_filename = video_path_obj.stem + '.wav'
        audio_path = Path(audio_directory) / audio_filename
        video.audio.write_audiofile(str(audio_path))
        print(f"Audio extracted and saved to {audio_path}")
        return audio_path
    except Exception as e:
        print(f"Failed to extract audio from {video_path}: {e}")
        return None
    finally:
        if video:
            video.close()

def audio_to_text(audio_path, text_directory):
    Path(text_directory).mkdir(parents=True, exist_ok=True)
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(str(audio_path)) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
        print(f"Recognized text: {text}")
    except sr.UnknownValueError:
        print(f"Speech Recognition could not understand audio in {audio_path}")
        text = ""
    except sr.RequestError as e:
        print(f"Request error for: {e}")
        text = ""
    except Exception as e:
        print(f"Error processing audio file {audio_path}: {e}")
        text = ""
    
    audio_path_obj = Path(audio_path)
    text_filename = audio_path_obj.stem + '.txt'
    text_path = Path(text_directory) / text_filename
    
    try:
        with open(text_path, 'w', encoding='utf-8') as text_file:
            text_file.write(text)
        print(f"Text converted and saved to {text_path}")
    except Exception as e:
        print(f"Failed to save text file {text_path}: {e}")

if __name__ == '__main__':
    urls_YouTube = [
        'https://www.youtube.com/shorts/CS3kviWGkH0',
        'https://www.youtube.com/shorts/-WowH0liGfE',
        'https://www.youtube.com/shorts/QTyQtQmpZ0g',
        'https://www.youtube.com/shorts/KDqXneUN4CA',
        'https://www.youtube.com/shorts/AnOJRqLnfqQ',
        'https://www.youtube.com/shorts/LcQa94wX-O8',
        'https://www.youtube.com/shorts/z-F3cQ7YN28',
        'https://www.youtube.com/shorts/j_Pv6EHYo9k',
        'https://www.youtube.com/shorts/ZTdXLfHWDJE',
        'https://www.youtube.com/shorts/x0iC-8ZnNwM'
    ]
    
    youtube_videos = 'video_urls.txt'
    with open(youtube_videos, 'w', encoding='utf-8') as file:
        for text in urls_YouTube:
            file.write(text + '\n')

    video_urls = extract_urls(youtube_videos)
    print(videoenames)

    serial_downloader(video_urls)
    parallel_downloader(video_urls)
    parallel_downloader1(video_urls)
    parallel_downloader2(video_urls)

    # Transcribe audio to text after all downloads and audio extractions
    for audio_file in Path(audio_directory).glob('*.wav'):
        audio_to_text(audio_file, text_directory)





