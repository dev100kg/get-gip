import requests


def getGlovalIp():
    return requests.get("http://inet-ip.info/ip").text
