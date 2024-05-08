import os
from tqdm import tqdm
import applescript
from PIL import Image
import cv2
import pytesseract
import numpy as np
import pyautogui

YOUTUBE_LINK = 'https://www.youtube.com/channel/UC-uTdkWQ8doqRwXBlkH67Dw'
LINKEDIN_LINK = 'https://www.linkedin.com/in/jackblair876/'
GITHUB_LINK = 'https://github.com/JackBlair87'
INSTAGRAM_LINK_MAIN = 'https://www.instagram.com/jack.blairr/'
INSTAGRAM_LINK_SECONDARY = 'https://www.instagram.com/jack.bl.ai.rt/'
TWITTER_LINK = 'https://twitter.com/JackBlair87'
MEDIUM_LINK = 'https://medium.com/@jackblair87'
FACEBOOK_LINK = 'https://www.facebook.com/jack.blair.94043/'

PROFILE_LINKS = [{ 'link' : YOUTUBE_LINK, 'platform' : 'youtube', 'account' : 'main' }, 
                 { 'link' : LINKEDIN_LINK, 'platform' : 'linkedin', 'account' : 'main' },
                 { 'link' : GITHUB_LINK, 'platform' : 'github', 'account' : 'main' },
                 { 'link' : INSTAGRAM_LINK_MAIN, 'platform' : 'instagram', 'account' : 'main' },
                 { 'link' : INSTAGRAM_LINK_SECONDARY, 'platform' : 'instagram', 'account' : 'art' },
                 { 'link' : TWITTER_LINK, 'platform' : 'twitter', 'account' : 'main' },
                 { 'link' : MEDIUM_LINK, 'platform' : 'medium', 'account' : 'main' },
                 { 'link' : FACEBOOK_LINK, 'platform' : 'facebook', 'account' : 'main' }]

TOTAL_FOLLOWERS = 0

#creating a folder called screenshots
if not os.path.exists('screenshots'):
    os.makedirs('screenshots')
    
#create folder for text files
if not os.path.exists('ocr_results'):
    os.makedirs('ocr_results')


def convert_youtube_strings_to_values(string):
    # Remove commas if present
    string = string.replace(',', '')
    
    # Take in strings like '1.23K' and convert them to floats
    if string[-1] == 'K':
        return float(string[:-1]) * 1000
    elif string[-1] == 'M':
        return float(string[:-1]) * 1000000
    else:
        return float(string)


def extract_follower_count(text, platform):
    platform_mappings = {
        'youtube': 'subscribers',
        'instagram': 'followers',
        'twitter': 'followers',
        'facebook': 'friends',
        'github': 'followers',
        'linkedin': 'followers',
        'medium': 'followers'
    }

    if platform in platform_mappings:
        keyword = platform_mappings[platform]
        count_text = text.split(keyword)[0]
        count = list(map(str.strip, count_text.split()))[-1]
        print(f'{platform.capitalize()} count:', count)
        return convert_youtube_strings_to_values(count)
    else:
        print('Platform not supported')
        return None
   
        
def ocr_image(image_path, platform):
    global TOTAL_FOLLOWERS
    # Load image
    img = cv2.imread(image_path)
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply threshold to convert to binary image
    # threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # in my experience, thresholding doesn't work well for OCR

    # Pass the image through pytesseract
    text = pytesseract.image_to_string(gray)
    # Print the extracted text
    # print(text)
    
    #save to a text file
    with open('ocr_results/' + image_path.split('/')[1].split('.')[0] + '.txt', 'w') as f:
        f.write(text)
        
    TOTAL_FOLLOWERS += extract_follower_count(text.lower(), platform)
        
    return text


def take_screenshots():

    for link in tqdm(PROFILE_LINKS):
        temp_link = 'screenshots/' + link['platform'] + '[' + link['account'] + '].png'
        
        #join this path with the current path
        full_link = os.path.join(os.getcwd(), temp_link.replace(' ', '\ '))
        print(full_link)
        

        r = applescript.run(f"""
            tell application "Google Chrome"
                activate
                open location "{link['link']}"
                set thePath to "{full_link}"
                delay 5
                do shell script ("screencapture " & thePath)
            end tell
            """)
        
        #save it to the desktop
        image1 = pyautogui.screenshot(full_link)
        image1.save(full_link)
        
        r = applescript.run(f"""
            tell application "Google Chrome"
                try
                    tell window 1 of application "Google Chrome" to ¬
                        close active tab
                end try
            end tell
            """)
        
        
def do_ocr():
    for link in tqdm(PROFILE_LINKS):
        ocr_image('screenshots/' + link['platform'] + '[' + link['account'] + '].png', link['platform'])
    

if __name__ == '__main__':
    take_screenshots()
    do_ocr()

    print('Total followers:', TOTAL_FOLLOWERS)