from django.shortcuts import render
import json
import urllib

def index(request):
    
    if request.method == "POST":
        city = request.POST.get("city", "")
        res = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=a59b2c9459bc67f4c5ebcdb3fdad50bc").read()
        json_data = json.loads(res)
        data = {
            "countrycode": str(json_data["sys"]["country"]),
            "coordinate": str(json_data["coord"]["lon"]) + " " + str(json_data["coord"]["lat"]),
            "temp": str(json_data["main"]["temp"]),
            "pressure": str(json_data["main"]["pressure"]),
            "Humidity": str(json_data["main"]["humidity"]),
        }

    else:
        city = ''
        data = {}
    return render(request, "index.html", {"city": city, "data": data})
