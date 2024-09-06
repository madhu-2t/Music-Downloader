import yt_dlp
def download_audio(video_url, output_path=".", ffmpeg_path=None):
    # Define the options for yt-dlp
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Save to the specified output path
        # No need for FFmpeg postprocessing if we're just downloading the audio in its original format (e.g., m4a)
    }

    if ffmpeg_path:
        ydl_opts['ffmpeg_location'] = ffmpeg_path  # Specify ffmpeg location if provided

    # Use yt-dlp to download the audio
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])



# Example usage
def fun2(songs_count=None):
    file_path = "output_links.txt"  # Path to the text file containing video URLs
    output_path = "downloads"  # Path to save the downloaded audio files
    ffmpeg_path = r"C:\ffmpeg\bin"  # Path to the ffmpeg installation (optional)
    to_download=[]
    already_Downloaded=[]
    with open(file_path, 'r') as file:
            # Read each line (assuming each line is a URL)
            for line in file:
                # Strip any extra whitespace/newline characters and add to the list
                video_url = line.strip()
                if video_url:  # Only add non-empty lines
                    # download_audio(video_url, output_path, ffmpeg_path)
                    to_download.append(video_url)
    if songs_count==None:
         songs_count=len(to_download)
    elif songs_count>len(to_download):
         print(f"Your trying to download more songs than your liked songs. process exited")
         return -1
    for i,link in enumerate(to_download[:songs_count]):
         download_audio(link,output_path,ffmpeg_path)
         to_download.pop(i)
         already_Downloaded.append(link)

    with open("already_downloaded.txt", 'a') as file:
            # Loop through the list and write each link to the file
            for link in already_Downloaded:
                file.write(f"{link}\n")

    with open(file_path, 'w') as file:
            for link in to_download:
                file.write(f"{link}\n")


# download_from_file(file_path, output_path, ffmpeg_path)
