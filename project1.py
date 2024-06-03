import re
import time
import requests
import multiprocessing
import threading
import logging

# List to store the extracted video names
videoenames = []

# Extract the URLs from video_urls.txt.
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

# Function to download video content
def download_video(url,):
    try:
        response = requests.get(url)
        # Store the raw binary content of the response body (the actual video data).
        video = response.content
        pattern = r'[^/]+$'
        match = re.search(pattern, url)
        # Store the name of the file
        title = match.group(0)
        filename = title 
        with open(filename, 'wb') as file:
            file.write(video)
        print(f'Downloaded {filename}')
    except requests.RequestException as e:
        print(f'Error downloading {url}: {e}')
    
def serial_downloader(videonames):
    start = time.perf_counter()
    for video in videonames:
        download_video(video)
    end = time.perf_counter()
    print(f'Serial run took {round(end-start, 2)} second(s)')

def parallel_downloader(videonames):
    start = time.perf_counter()
    processes = []
    for video in videonames:
        p = multiprocessing.Process(target=download_video, args=(video,))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    end = time.perf_counter()
    print(f'Parallel run took {round(end-start, 2)} second(s)')

def parallel_downloader1(videonames):
    start = time.perf_counter()

    threads = []
    for video in videonames:
        t = threading.Thread(target=download_video, args=(video,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end = time.perf_counter()
    print(f'Parallel run with threads took {round(end-start, 2)} second(s)')

# Limit to 5 concurrent downloads
semaphore = threading.Semaphore(5) 

def parallel_downloader2(videonames):
    start = time.perf_counter()
    
    def download_with_semaphore(video):
        with semaphore:
            download_video(video)
    
    threads = []
    for video in videonames:
        t = threading.Thread(target=download_with_semaphore, args=(video,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    
    end = time.perf_counter()
    print(f'Parallel run with limited threads took {round(end-start, 2)} second(s)')

'''
serial_downloder : time complexity is O(n). The function downloads each video sequentially, resulting in a linear time complexity.
Space complexity is O(1). The function does not require additional space that grows with the number of videos.

parallel_downloader's time complexity remains linear but the time can be significantly reduced due to concurrent downloads. The total time will depend on the number of available CPU cores.
Space Complexity is O(n). Each process takes some amount of memory, so the space complexity is proportional to the number of processes created.

parallel_downloader1's time complexity is O(n). The function downloads videos concurrently, but the overall time complexity remains linear.
Space Complexity is O(n). Space complexity grows linearly with the number of videos.

parallel_downloader2's time complexity is O(n). The function's time complexity is linear, similar to the previous parallel approaches.
Space Complexity is O(n). Although the semaphore limits the number of active threads to 5, the function still creates a thread for each video, resulting in linear space complexity.

'''

if __name__ == '__main__':
    urls_YouTube = ['https://www.youtube.com/shorts/CS3kviWGkH0',
                    'https://www.youtube.com/shorts/-WowH0liGfE',
                    'https://www.youtube.com/shorts/QTyQtQmpZ0g',
                    'https://www.youtube.com/shorts/KDqXneUN4CA',
                    'https://www.youtube.com/shorts/AnOJRqLnfqQ',
                    'https://www.youtube.com/shorts/LcQa94wX-O8',
                    'https://www.youtube.com/shorts/z-F3cQ7YN28',
                    'https://www.youtube.com/shorts/j_Pv6EHYo9k',
                    'https://www.youtube.com/shorts/ZTdXLfHWDJE',
                    'https://www.youtube.com/shorts/x0iC-8ZnNwM']
    
    # Filename to store the URLs
    youtube_videos = 'video_urls.txt'
    
    # Save the URLs in a text file called video_urls.txt , where each URL should be stored on a separate line.
    with open(youtube_videos, 'w', encoding='utf-8') as file:
        for text in urls_YouTube:
            file.write(text + '\n')

    # Extract URLs from the text file and store the video names.
    video_urls = extract_urls(youtube_videos)

    # Print the extracted video names
    print(videoenames)

    # Download videos serially
    serial_downloader(video_urls)

    # Download videos in parallel using multiprocessing
    parallel_downloader(video_urls)

    # Download videos in parallel using threading
    parallel_downloader1(video_urls)

    # Download videos in parallel with a limited number of threads using semaphore
    parallel_downloader2(video_urls)
