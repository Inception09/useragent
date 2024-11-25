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
