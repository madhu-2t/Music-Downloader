from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.options import Options


# Set Chrome options to load your user profile
def fun1():
    chrome_options = Options()
    chrome_options.add_argument(r"user-data-dir=C:\Users\madhu\AppData\Local\Google\Chrome\User Data")
    # chrome_options.add_argument("--profile-directory=Default") # use this if you want to download from default 
    chrome_options.add_argument("--profile-directory=Profile 1")   

    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the playlist page
    driver.get('https://music.youtube.com/playlist?list=LM')

    # Pause to let the page fully load
    time.sleep(5)

    # Scroll down the page multiple times to load dynamic content
    scroll_pause_time = 3  # Adjust this if needed
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Wait to allow more content to load
        time.sleep(scroll_pause_time)
        
        # Calculate new scroll height and compare with the last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break  # Break the loop if the page height has not changed
        last_height = new_height

    # Get the page source after scrolling
    html = driver.page_source

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all <a> tags with the specified class
    a_tags = soup.find_all('a', class_='yt-simple-endpoint style-scope yt-formatted-string')

    # Extract the href attributes starting with 'watch'
    hrefs = [link['href'] for link in a_tags if link.get('href', '').startswith('watch')]
    ##Getting already downloaded links
    file_path=r"already_downloaded.txt"
    downloaded_links=[]
    with open(file_path, 'r') as file:
            # Read each line (assuming each line is a URL)
            for line in file:
                # Strip any extra whitespace/newline characters and add to the list
                video_url = line.strip()
                if video_url:  # Only add non-empty lines
                    downloaded_links.append(video_url)




    # Write the hrefs to a text file with the prefix
    with open('output_links.txt', 'w') as file:
        for href in hrefs:
            full_link = f"https://music.youtube.com/{href}"
            if full_link not in downloaded_links:
                file.write(f"{full_link}\n")

    # Close the browser
    driver.quit()

    print("Links have been extracted and saved to output_links.txt")
