from django.shortcuts import render
import requests as req
import json
import api.models

def foursquareGetData(request, *args, **kwargs):
     
     latitude = request.GET.get('latitude', None)
     longitude = request.GET.get('longitude', None)
       
     apikey = request.GET.get('apikey', None)
     url = "https://api.foursquare.com/v3/places/search?ll=" + str(latitude) + "%2C"+str(longitude)
     headers = {"Accept": "application/json","Authorization": apikey }
            
     response = req.get(url, headers=headers)
     locJson = json.loads(response.text)
     results_list = locJson['results']
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
                 
     return render(request, "foursquare.html")

def home(request):
    return render(request, "index.html")

