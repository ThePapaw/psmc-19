import requests

def grab(code):
    # If you get wmsAuth from CNN it bypasses geoblock. Then we can replace CNN (in url) with desired channel
    url = "https://ustvgo.tv/player.php?stream=CNN"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36',
        'Referer': 'https://ustvgo.tv/'
    }
    r = requests.get(url, headers=headers).text.replace('\n', '').split("var hls_src='")[1].split("'")[0]
    return r.replace("CNN", code)
