from django.shortcuts import render
import requests as req
import json
import api.models


def home(requests):
    
    latitude, longitude = 38.630554, 27.422222
    # The valid range of latitude in degrees is -90 and +90 for the southern and northern hemisphere,
    # respectively. Longitude is in the range -180 and +180 specifying coordinates
    # west and east of the Prime Meridian, respectively.

    url = "https://api.foursquare.com/v3/places/search?ll=" + \
        str(latitude) + "%2C"+str(longitude)
    headers = {
        "Accept": "application/json",
        "Authorization": "fsq38jf5s6BtxsM5GasJ/3pdhr7HlOSL2O6cjpiwegCvd90="
    }
    response = req.get(url, headers=headers)

    locJson = json.loads(response.text)
    
    
    #print(locJson['results'][1]['location'])
    
    results_list = locJson['results']
    print('results_list',type(results_list))
    for result in results_list:
        locationModel = api.models.Location()
        
        locationModel.fsq_id = result['fsq_id']
        
        lat = result['geocodes']['main']['latitude']
        lng = result['geocodes']['main']['longitude']
        
        locationModel.latitude = lat
        locationModel.longitude = lng
        
        
        locationModel.country = result['location']['country']
        
        if "address" in result['location']:
            locationModel.address = result['location']['address']
        elif "formatted_address" in result['location']:
            locationModel.address = result['location']['formatted_address']
            
        if "region" in result['location']:
                locationModel.region = result['location']['region']  
    
        locationModel.name = result['name']
        locationModel.save()
    
    return render(requests, "index.html")

