from bs4 import BeautifulSoup
import requests

YOUTUBE_URL = "https://www.youtube.com/channel/UC-uTdkWQ8doqRwXBlkH67Dw"

def convert_youtube_strings_to_values(string):
    #take in strings like '1.23K' and convert them to floats
    if string[-1] == 'K':
        return float(string[:-1]) * 1000
    elif string[-1] == 'M':
        return float(string[:-1]) * 1000000
    else:
        return float(string)


def youtube():
    try:
        # Set your YouTube Channel URL here
        url = YOUTUBE_URL
    except:
        print("Channel  not found")

    temp = requests.get(url)
    bs = BeautifulSoup(temp.text, 'lxml')
    bs = str(bs)
    point = bs.find("subscribers")
    start = point
    while bs[start] != '"':
        start -= 1
    end = point - 1
    subscriber = bs[start + 1:end]
    
    return convert_youtube_strings_to_values(subscriber)


def instagram():
    # Set your Instagram ID here
    user = "jack.blairr"
    url = 'https://www.instagram.com/' + user
    r = requests.get(url).text

    start = '"edge_followed_by":{"count":'
    end = '},"followed_by_viewer"'

    follower = r[r.find(start)+len(start):r.rfind(end)]

    return follower


def twitter():
    # Set your Twitter ID here
    handle = 'JackBlair87'
    temp = requests.get('https://twitter.com/'+handle)
    bs = BeautifulSoup(temp.text, 'lxml')
    bs = str(bs)
    
    follow_box = bs.find('div', {'class': 'css-175oi2r r-13awgt0 r-18u37iz r-1w6e6rj'})
    followers = follow_box.find('a').find('span', {'class':'css-1rynq56 r-bcqeeo r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-1loqt21'})
    twitter_follower = followers.find('span').get('css-1qaijid r-bcqeeo r-qvutc0 r-poiln3')

    
    
    # try:
    #     follow_box = bs.find('div', {'class': 'css-175oi2r r-13awgt0 r-18u37iz r-1w6e6rj'})
    #     followers = follow_box.find('a').find('span', {'class':'css-1rynq56 r-bcqeeo r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-1loqt21'})
    #     twitter_follower = followers.find('span').get('css-1qaijid r-bcqeeo r-qvutc0 r-poiln3')
    #     return twitter_follower
    # except:
    #     print('Account name not found...')


try:
    youtube_subscriber = youtube()
    print("YouTube Subscriber: ", youtube_subscriber)
except:
    print("You may have some problem with YouTube")

# try:
#     instagram_follower = instagram()
#     print("Instagram Followers: ", instagram_follower)
# except:
#     print("You may have some problem with Instagram")

try:
    twitter_follower = twitter()
    print("Twitter Follower: ", twitter_follower)
except:
    print("You may have some problem with Twitter")

