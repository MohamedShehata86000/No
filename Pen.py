import requests
import random
import telebot
tok = "8128789997:AAHIE70sQCwEZYPt7p90uLLg5RUHrIYnyxU"
ch_id = "7037898496"
botA = telebot.TeleBot(token=tok)
# دالة لتوليد رقم عشوائي مكون من 12 رقماً
def generate_random_number():
    return ''.join([str(random.randint(0, 9)) for _ in range(12)])

# توليد 5 أرقام عشوائية وعرضها
def pen():

    url = "https://penduline.com/coupons/redeem"
    
    payload = {
    #  '_token': '7Lwz29wJPf9NTKXUlSERJVYTXmno9ho6Za7rsJ8v',
      '_method': 'post',
      'coupon': generate_random_number(),
      'coupon_can_be_redeemed': ''
    }
    print(payload)
    headers = {
      'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36",
      'Accept-Encoding': "gzip, deflate, br, zstd",
      'sec-ch-ua-platform': "\"Android\"",
      'x-csrf-token': "7Lwz29wJPf9NTKXUlSERJVYTXmno9ho6Za7rsJ8v",
     
      'sec-ch-ua-mobile': "?1",
      'x-requested-with': "XMLHttpRequest",
      'origin': "https://penduline.com",
      'sec-fetch-site': "same-origin",
      'sec-fetch-mode': "cors",
      'sec-fetch-dest': "empty",
      'referer': "https://penduline.com/",
      'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
      'priority': "u=1, i",
      'Cookie': "_ga=GA1.1.107393907.1744041998; _fbp=fb.1.1744042004662.401042182337194413; remember_web_3dc7a913ef5fd4b890ecabe3487085573e16cf82=eyJpdiI6IlNzc0RocjBtdVFya1RURnpGNnRBMGc9PSIsInZhbHVlIjoiaWhBOTZRcHVQWnI2ZU5DN2hoNEJERmRwNmRrTlh5YTJWKzdidU9vMmk1YzRheHZSYzRxSGY0cmMzbHh4bk9wdmhBVVhzZ2NuOTljUHcydlhGYnhOQWdUV1BPYXp2NENpK0hYRXVtOCsrUWJGcVo1Z1NkOWpYdk0wcm5WRzUwS2ZuZFdqNUc4SjI4M3R3ZFJFenl6UnZRPT0iLCJtYWMiOiIzNjNlNDEzZDY1NzcxMjk3YzI2ZmFkNWYwMjlhOWI5M2RjYTEyOGE3ZGQ1YTkwNmUzZDk3N2I4MjNmZTU3ZmNkIiwidGFnIjoiIn0%3D; _ga_9VF32W8W4K=GS1.1.1744041997.1.1.1744042415.39.0.0; XSRF-TOKEN=eyJpdiI6IkpKR1NETHlTWmlWdnBZNW5BajhaUkE9PSIsInZhbHVlIjoiQkhmOFE3bjV6cTdocGhHSXpmRlQ3K3kvazJwQ0FpYmtjOVE5Z0cwb0JSTmNqOWZrSlY4eWFoclRsemVnb0FIMEl2T1pSVXN0dUdzbll3dllnaWpnVFBEbTViTzFDSWh3a2Rnc1I3bklvSHkvdWt3N3R3eTFEbWowNm5rd1FiSXkiLCJtYWMiOiI0MTYwMjczZmU4MGQ0ZDlhOTQzZmQ5OTMzNDc2NWQ3ZjE5YmZmMzNmMGQwMDBlMmYwMjdiZWQ5MTNiNzI5NzdmIiwidGFnIjoiIn0%3D; penduline_session=eyJpdiI6InZxVk9naU1CR2VHSVA0QXBMVVVCZkE9PSIsInZhbHVlIjoiR3M0bVNTSUhQVmNLMEZpZ1k5Uyt4VkRhZTNvbDZYS1BlK3ZtekVRRWJIdDBWakhnRGkyd1g0U1Y5bWs1dExZVVRYSVFtUzRxT2lGVi82Q0c0SE9LZ3VXNVZZN1YxaXdLeVlmaEVOYnRHVWV3QXpvc1h0QnhjcFk4TTRJeHdoL20iLCJtYWMiOiJlYjc2MjQzYjc5YzZmZGM1ZmY3MWQ2NzVhNDViYTJiNWY1MDgwMTZjM2U3ZGUwM2VlNDhmYjBlNGYyMzY0YmJlIiwidGFnIjoiIn0%3D"
    }
    
    response = requests.post(url, data=payload, headers=headers)
    if response.json()["message"] =='كوبون غير صحيح'   :
        print("Bad")
    else:
        botA.send_message(chat_id=ch_id, text=response.json()["message"])
        print(response.json())
while True:
    pen()  
