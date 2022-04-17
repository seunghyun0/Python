import requests
import xmltodict
import json
import datetime

class API_READ:
    def virus_api(url,key):
        today =datetime.datetime.now() 
        yesterday = today - datetime.timedelta(1) 
        now = today.strftime("%Y%m%d") 
        past = yesterday.strftime("%Y%m%d") 
        params ={'serviceKey' : key, 'pageNo' : '1', 'numOfRows' : '10', 'startCreateDt' : past, 'endCreateDt' : now }
        response = requests.get(url, params=params)
        if response.status_code == 200: # 응답 코드가 200이면 정상
            changeText = xmltodict.parse(response.text)
            mkJson = json.loads(json.dumps(changeText))
        print ('누적 확진자:', mkJson['response']['body']['items']['item'][0]['decideCnt']) 
        print ('오늘 확진자:', int(mkJson['response']['body']['items']['item'][0]['decideCnt']) - int(mkJson['response']['body']['items']['item'][1]['decideCnt']))
        
        
    def weather_api(api_key,base_url):
        city_name = "seoul"
        complete_url = base_url + "appid=" + api_key + "&q="+city_name +"&units=metric"
        respnse = requests.get(complete_url)
        x = respnse.json()
        if x["cod"]!= "404":
            y=x["main"]
            current_temperature  = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]

            weather_description = z[0]["description"]

            print("온도 = "+
                            str(current_temperature)+
                "\n기압 = " +
                            str(current_pressure)+
            "\n습도 ="+ 
                            str(current_humidity)+
            "\n날씨 ="+ 
                            str(weather_description))
        else :
            print("City Not Found")
