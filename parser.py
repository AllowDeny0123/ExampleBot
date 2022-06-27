from bs4 import BeautifulSoup
import requests

url = "https://www.google.com/search?q=usd+rub&ei=gy8bYsezBOjrrgTloLSoDA&ved=0ahUKEwiHgeeNtZ_2AhXotYsKHWUQDcUQ4dUDCA4&uact=5&oq=usd+rub&gs_lcp=Cgdnd3Mtd2l6EAMyDwgAELEDEIMBEEMQRhCCAjILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATIKCAAQsQMQgwEQQzIFCAAQgAQyBQgAEIAEMgQIABBDMgUIABCABDIECAAQQzoICAAQgAQQsQM6CAgAELEDEIMBSgQIQRgASgQIRhgAUABYrglghQ1oAHABeACAAWSIAf8EkgEDNi4xmAEAoAEBwAEB&sclient=gws-wiz"
url2 = "https://www.google.com/search?q=eur+rub&ei=uy8bYrfFJMOGrwSG6aLgBQ&ved=0ahUKEwj3juGotZ_2AhVDw4sKHYa0CFwQ4dUDCA4&uact=5&oq=eur+rub&gs_lcp=Cgdnd3Mtd2l6EAMyDwgAELEDEIMBEEMQRhCCAjIECAAQQzIECAAQQzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CwguEIAEELEDEIMBOg4ILhCABBCxAxDHARDRAzoHCAAQsQMQQzoICAAQgAQQsQM6CwguELEDEMcBEKMCOgsILhCABBDHARCjAjoLCC4QgAQQxwEQrwE6CAgAELEDEIMBOgoIABCxAxCDARBDSgQIQRgASgQIRhgAUABYlBVgmhdoAXABeACAAesCiAHfCZIBBTYuMy0ymAEAoAEBwAEB&sclient=gws-wiz"
headers = {

    "Accept" : "*/*",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"

}

def GetData(url):
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.content, 'html.parser')
    return soup

def GetValue(soup):
    ans = soup.find("span", {"class":"DFlfde", "class":"SwHCTb"})
    return ans.text

def GetCurrency(curr):
  if curr == "usd":
    lurl = url
  if curr == "eur":
    lurl = url2
  if GetValue(GetData(lurl)) != None :
    #print(GetValue(GetData(lurl)))
    return GetValue(GetData(lurl))
  else:
    return "Unav."
  
  