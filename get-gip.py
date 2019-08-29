import requests


def getGlobalIp():
    return requests.get("http://inet-ip.info/ip").text
