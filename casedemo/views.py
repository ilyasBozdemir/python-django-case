from django.shortcuts import render
import requests as req

def home(requests):
    latitude,longitude = 45,34
    #The valid range of latitude in degrees is -90 and +90 for the southern and northern hemisphere,
    # respectively. Longitude is in the range -180 and +180 specifying coordinates 
    # west and east of the Prime Meridian, respectively. 
    
    url = "https://api.foursquare.com/v3/places/search?ll=" + \
        str(latitude) + "%2C"+str(longitude)
    headers = {
        "Accept": "application/json",
        "Authorization": "fsq38jf5s6BtxsM5GasJ/3pdhr7HlOSL2O6cjpiwegCvd90="
    }
    response = req.get(url, headers=headers)
    print(response.text)
    return render(requests, "index.html")
