import requests
from stem import Signal
from stem.control import Controller
from fake_useragent import UserAgent
import random, time


headers = { 'User-Agent': UserAgent().random }

print(requests.get('https://ident.me', headers=headers).text)

proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}
print(requests.get('https://api.ipify.org', proxies=proxies, headers=headers).text)

wait = random.uniform(0, 5)
print("wait : " + str(wait))
time.sleep(wait)

# signal TOR for a new connection 
# https://stackoverflow.com/questions/30286293/make-requests-using-python-over-tor
def renew_connection():
    with Controller.from_port(port = 9051) as c:
        c.authenticate(password="password")
        c.signal(Signal.NEWNYM)

renew_connection()
print(requests.get('https://api.ipify.org', proxies=proxies, headers=headers).text)


