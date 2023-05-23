import json  
from django.shortcuts import render  
import urllib.request  
import json  
  
# Create your views here.  
  
def index(request):  
    if request.method == 'POST':  
        # Get the city name from the user api = http://api.openweathermap.org/data/2.5/weather  
        city = request.POST.get('city', 'True')  
          
        # retreive the information using api  
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=c03df51b2bc7b5a6ecc749bad70e4e76').read()  
          
        # convert json data file into python dictionary  
        list_of_data = json.loads(source)  
        
        # create dictionary and convert value in string  
        context = {  
            'city': city,  
            "country_code": str(list_of_data['sys']['country']),  
            "coordinate": str(list_of_data['coord']['lon']) + ' '  
                            + str(list_of_data['coord']['lat']),  
            "temp": str(list_of_data['main']['temp']) + ' °C',  
            "pressure": str(list_of_data['main']['pressure'])+' Pa',  
            "humidity": str(list_of_data['main']['humidity'])+' %',  
        }  
    else:  
        context = {}  
      
    # send dictionary to the index.html  
    return render(request, 'index.html', context)  