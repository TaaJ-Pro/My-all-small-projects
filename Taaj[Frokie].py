import requests
import time


def sendMessage(token, chennel_ID, message):
    url = 'https://discord.com/api/v8/channels/{}/messages'.format(chennel_ID)
    data = {"content" : message}
    headers = {"authorization" : token}
    req = requests.post(url, data=data, headers=headers)

token = "ODM4NjMyOTk3NDY4MjQxOTIw.YTjGhQ.0ixZ9rZFcp8BOmrMnDybUW3Wn0M"
chennel_ID = 884771241444139018
message = ""

while True:
    message = ".get eggs"
    sendMessage(token, chennel_ID, message)
    time.sleep(1)
    message = ".boxswap Froakie"
    sendMessage(token, chennel_ID, message)
    time.sleep(3600)
    continue