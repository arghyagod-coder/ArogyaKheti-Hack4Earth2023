from geopy.geocoders import Nominatim
 
def GetAddressDetails(pincode):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(str(pincode), addressdetails=True)
    # try:
    #     district = location.raw["address"]["state_district"]
    # except:
    #     district = location.raw["address"]["municipality"]
    return location.raw["address"]["state"], location.raw["address"]["country"]

def GetCoordinates(pincode):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(str(pincode), addressdetails=True)
    return location.raw["lat"], location.raw["lon"]