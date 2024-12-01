import requests
import random

# Firebase Realtime Database URL
FIREBASE_DB_URL = "https://auto-ce-ac0a7-default-rtdb.asia-southeast1.firebasedatabase.app/users.json"

# Generate a random User-Agent for the login request
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

user_id = "jhdhfvgbd"

# Validate the User ID in Firebase using the REST API
def validate_user_id(user_id):
    response = requests.get(FIREBASE_DB_URL)
    if response.status_code == 200:
        users = response.json()
        if user_id in users:
            print(f"User ID {user_id} is valid.")
            return True
        else:
            print(f"User ID {user_id} not found in Firebase.")
            return False
    else:
        print(f"Failed to connect to Firebase. Status Code: {response.status_code}")
        return False

# Function to perform cookie extraction
def inc3_cookies(user_id, email, pwd):
    # Validate the User ID
    if not validate_user_id(user_id):
        return "Unauthorized User ID"

    # Generate headers and data for the Facebook login request
    ugen = useragent()
    uuid = generate_udid()
    data = {
        "adid": uuid,
        "format": "json",
        "device_id": uuid,
        "cpl": "true",
        "family_device_id": uuid,
        "credentials_type": "device_based_login_password",
        "error_detail_type": "button_with_disabled",
        "source": "device_based_login",
        "email": email,
        "password": pwd,
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

    # Debugging output
    print("Response:", response)

    if "session_cookies" in response:
        token = response["access_token"]
        cookies = {cookie['name']: cookie['value'] for cookie in response['session_cookies']}
        c_user = cookies.get('c_user', '')

        if not c_user:
            return f"{email} {pwd} wrong pass"

        datr = cookies.get('datr', '')
        sb = cookies.get('sb', '')
        xs = cookies.get('xs', '')
        fr = cookies.get('fr', '')

        cookie = f"datr={datr};sb={sb};c_user={c_user};xs={xs};fr={fr};m_page_voice={c_user}"
        return cookie
    else:
        return f"{email} {pwd} login failed, no session cookies returned"

def generate_udid(length=12):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(characters) for _ in range(length))
