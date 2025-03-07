import requests
import json
import requests
import telebot
import json
from fake_useragent import UserAgent
tok = "8128789997:AAHIE70sQCwEZYPt7p90uLLg5RUHrIYnyxU"
ch_id = "7037898496"
botA = telebot.TeleBot(token=tok)
import random
import string
url = "https://www.noon.com/_svc/cart-v1/coupon"

params = {
  'code': "VFSM50-LA7CQYLB",
  'showCart': ""
}
z="VFSM50-LA7CQYLB"

payload = {}

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36",
  'Accept': "application/json, text/plain, */*",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'Content-Type': "application/json",
  'sec-ch-ua-platform': "\"Android\"",
  'x-aby': "{\"po_v2\":{\"enabled\":1},\"mp_icon_v2\":{\"enabled\":1},\"pdp_screenshot_share_sheet\":{\"enabled\":1}}",
  'sec-ch-ua': "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
  'sec-ch-ua-mobile': "?1",
  'x-lng': "312205224",
  'x-ab-test': "901,911,951,1021,1091,1101",
  'x-content': "mobile",
  'x-locale': "ar-eg",
  'x-platform': "web",
  'x-cms': "v2",
  'x-ecom-zonecode': "EG-CAI-S10",
  'cache-control': "no-cache, max-age=0, must-revalidate, no-store",
  'x-mp': "noon",
  'x-visitor-id': "b9194577-a7e3-4109-a791-2c1298723929",
  'x-lat': "300631437",
  'origin': "https://www.noon.com",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://www.noon.com/egypt-ar/cart/",
  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
  'priority': "u=1, i",
  #'Cookie': "visitor_id=b9194577-a7e3-4109-a791-2c1298723929; _scid=HI0Z64SxQtlibhy34RGoFkKS1WbC0GWy; _ga=GA1.2.442306967.1731708859; _fbp=fb.1.1731708864191.510084225832805223; _tt_enable_cookie=1; _ttp=6T1IiS3michiWJkTgqlUh5HiDlk.tt.1; __gads=ID=e65a7c7a7526d8ab:T=1731709018:RT=1731783242:S=ALNI_Ma0kQuEhX4EFYvhcvSG6O0dm7kJmQ; __gpi=UID=00000f96034ab0f7:T=1731709018:RT=1731783242:S=ALNI_Mb1u010_IoV2R2IkcyH-2smngHmMg; __eoi=ID=b291065209006fa9:T=1731709018:RT=1731783242:S=AA-AfjajXeHjAtIfdQyxjJMieUJF; nloc=ar-eg; _gcl_gs=2.1.k1$i1736656844$u2158255; _gcl_au=1.1.1345918278.1741279817; ZLD887450000000002180avuid=e2eb9d63-f1bf-458f-bd2e-9ccb1232ab85; _ScCbts=%5B%5D; _pin_unauth=dWlkPVl6ZzRZbVU1WVdJdE5UbGpNUzAwWTJWbExUZzFOR010Wm1Fek1XRXpNMk00WVRVMQ; _sctr=1%7C1741212000000; _clck=knw1bb%7C2%7Cfu0%7C0%7C1781; nguestv2=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJraWQiOiIwNDE1ODBkZDM1Y2I0MmM5OGI5NDM3M2M2MjNiNTMwZiIsImlhdCI6MTc0MTM1ODEzMSwiZXhwIjoxNzQxMzU4NDMxfQ.te3WcC_N-6NoXHBfbfxiN6wD4gHKeTvENd6mxS7U3Cw; _etc=zFp79JAwX61NTNxG; _clsk=pfx44r%7C1741358142637%7C2%7C0%7Cx.clarity.ms%2Fcollect; _gcl_aw=GCL.1741373101.CjwKCAiArKW-BhAzEiwAZhWsIGMW38QlAKN6oS_MSp8-sinDmWe4xsXkB9IcG3IdBSttxeT1zhwcThoCR_MQAvD_BwE; noonengr-_zldp=dbw5UOFoeCxkqJyFElbxHcjmvnhPs6iyCdTLpIdOd6BQ6XGrgsoTBJEDX%252FhBGt2bmKwM1K1ctjo%253D; ZLDsiq663f5c2580454f7ed6b7bbe12e575c5570eb9b21832ce32b902ca6cbca6ffc2bavuid=e2eb9d63-f1bf-458f-bd2e-9ccb1232ab85; isAppInstallBannerDismissed=true; ak_bmsc=B9DB40ECD59EE6B386B9CA91F81F6ECF~000000000000000000000000000000~YAAQoNgRAkQwrWGVAQAApBHtcRvkS4+PGCCwiAgI7H+7Q/jw1hBY8mCc0rFyJx58QxlDMBjZ571CLQJD4oQ7WPgRmZbpSAgA20VOp+iCu5Rjjbxy7LHPBASOdRZvloj8oN1GgMDu51xN8oP6Ki/P4On4gCjeaOU/uXWz7QfI56IrKCrkJoVKTRxWsTrYCC4FmZE2Z5Ga7cdMODJSwH6MpflUjQyzw6kS/CVyrFVPWjNYecn7JlHcvsmbULFrrlGqzKqQ4FSeECE21kU/q9FMyLdhYHJke7y0wEuGWMWsR5FGkNKqQljTL2YC04SNKNUtkJMB5K4tdml5QVg4CYMasLdFFAMqgSH9Vulh8doSsYmu1JWLpVENyHDyiUwjzGjJ+iLcNoNoM8k=; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22D5oLv6WPkFN7xjmKwnOq%22%2C%22expiryDate%22%3A%222026-03-07T18%3A45%3A16.890Z%22%7D; _scid_r=Mg0Z64SxQtlibhy34RGoFkKS1WbC0GWyrAm1Ug; _uetsid=16bff2c0faab11efaaa81f7c52f97742; _uetvid=f66db350a39e11ef9dcf6fdafc400722; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3Anull%2C%22expiryDate%22%3A%222026-03-07T18%3A45%3A17.861Z%22%7D; nguestv2=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJraWQiOiI4MmI4YTc2MTQ1NGI0MDkzYjY4NWMzNWNlNzY5MzU0NSIsImlhdCI6MTc0MTM3MzEyOCwiZXhwIjoxNzQxMzczNDI4fQ.amXupgKbCs3Bg4BHsJKP51B3UV_PB9zNmZKzqkgixgY; RT=\"z=1&dm=noon.com&si=f4aefb25-c8e2-4ad9-8495-038d80934ac8&ss=m7z4kywq&sl=1&tt=10xn&bcn=%2F%2F684dd32d.akstat.io%2F&ld=10zj\"; ZLDsiq3b3ce696144e42ab351af48092266ce3dda2b3c7b2ad6e09ba5d18504de03180tabowner=undefined"
}

response = requests.post(url, params=params, data=json.dumps(payload), headers=headers).text
if "مبروك" in response:
    print('Hurray! You got a discount!')
    botA.send_message(chat_id=ch_id, text=z)
