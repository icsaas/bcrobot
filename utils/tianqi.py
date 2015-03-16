#-*- coding:utf-8 -*-
import urllib
from xml.dom.minidom import parseString

def weather(city):
  page = urllib.urlopen("http://www.webxml.com.cn/webservices/weatherwebservice.asmx/getWeatherbyCityName?theCityName="+city);
  body = page.readlines();
  page.close();

  #body是一个list，需要转成string
  document=""
  for line in body:
    document = document + line
  #print document

  dom =parseString(document)

  strings = dom.getElementsByTagName("string")
  #今天的温度和天气
  today_temperature=getText(strings[5].childNodes)
  today_weather=getText(strings[6].childNodes)

  #明天的温度和天气

  tomorrow_weather=getText(strings[13].childNodes)
  tomorrow_temperature=getText(strings[12].childNodes)

  weather=today_weather+" " +today_temperature+" ;  " +tomorrow_weather+" "+tomorrow_temperature

  return weather

def getText(nodelist):
    rc = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc = rc + node.data
    return rc

if __name__=="__main__":
  weather = weather()
  print weather
