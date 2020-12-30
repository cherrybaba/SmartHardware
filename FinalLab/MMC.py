import requests
import time

def showAlert(message: str, duration: int=2000): # duration:ms
    url = "http://localhost:8080/api/module/alert/showAlert?message={}&timer={}".format(message, duration)
    requests.get(url)

def nextArtical():
    url = "http://localhost:8080/api/module/newsfeed/articlenext"
    requests.get(url)

def previousArtical():
    url = "http://localhost:8080/api/module/newsfeed/articleprevious"
    requests.get(url)

def readMore():
    url = "http://localhost:8080/api/module/newsfeed/articlemoredetails"
    requests.get(url)

def readLess():
    url = "http://localhost:8080/api/module/newsfeed/articlelessdetails"
    requests.get(url)

def scrollUP():
    url = "http://localhost:8080/api/module/newsfeed/articlescrollUP"
    requests.get(url)

def getBrightness()->int:
    url = "http://localhost:8080/api/brightness"
    resp = requests.get(url)
    result = resp.json()
    return result.get("result", -1)

def setBrightness(brightness: int): # 0-100
    url = "http://localhost:8080/api/brightness/{}".format(brightness)
    requests.get(url)

def hideModule(name: str):
    url = "http://localhost:8080/api/module/{}/hide".format(name)
    requests.get(url)

def showModule(name: str):
    url = "http://localhost:8080/api/module/{}/show".format(name)
    requests.get(url)

if __name__ == "__main__":
    # print("brightness is {}".format(getBrightness()))
    # setBrightness(0)
    # time.sleep(1)
    # setBrightness(100)
    # time.sleep(1)
    # hideModule("clock")
    # time.sleep(1)
    # showModule("clock")
    # time.sleep(1)
    # showAlert("Gua Gua Gua")
    # nextArtical()
    # time.sleep(0.5)
    # nextArtical()
    # time.sleep(0.5)
    # nextArtical()
    # time.sleep(0.5)
    # previousArtical()
    # time.sleep(0.5)
    # previousArtical()
    # time.sleep(0.5)
    # previousArtical()
    readLess()
    readMore()
    # readMore()
    # time.sleep(4)
    # readLess()