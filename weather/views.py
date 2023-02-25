from django.shortcuts import render
import json
import urllib.request
# Create your views here.
def index(request):
    if request.method =='POST':
        city = request.POST['city']
        api_key = '154ef6ffb8da2f7745fe23bc9b206e7d'

        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+api_key).read()
        json_data = json.loads(res)
        data = {
                "country_code":str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon']) + ' ' +
                str(json_data['coord']['lat']),
                "temp":str(int(json_data['main']['temp'])-273)+'C', 
                "feels":str(int(json_data['main']['feels_like'])-273)+'C',   
                "pressure":str(json_data['main']['pressure']),
                "humidity":str(json_data['main']['humidity']), 
            }
    else:
        city=''
        data={}
    return render(request,'index.html',{'city':city,'data':data})