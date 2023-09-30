import requests
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import google.generativeai as palm
import os
from dotenv import load_dotenv

load_dotenv()

fertilizerdata = pd.read_csv("datasets/Fertilizer Prediction.csv") 
openweather_api_key = os.environ.get('OPENWEATHER_API_KEY')
newsapi_api_key = os.environ.get('NEWSAPI_API_KEY')
palm_api_key = os.environ.get('GOOGLE_PALM_API_KEY')
govdata_api_key = os.environ.get('GOVDATA_API_KEY')

def getWeatherDetails(coords):
    lat = coords[0]
    lon = coords[1]
    openweather_url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={openweather_api_key}"
    response1 = requests.get(openweather_url)
    data1 = response1.json()

    weather = data1['current']['weather'][0]['main']
    temp = data1['current']['temp']
    temp = round(temp - 273.15, 2)
    humidity = data1['current']['humidity']
    wind_speed = data1['current']['wind_speed']
    pressure = data1['current']['pressure']
    return [weather, temp, humidity, wind_speed, pressure]

def getAgroNews():
    newsapi_url = f"https://newsapi.org/v2/everything?q=agriculture&apiKey={newsapi_api_key}"
    response = requests.get(newsapi_url)
    data = response.json()
    return data["articles"][:20]

def getFertilizerRecommendation(model, nitrogen, phosphorus, potassium, temp, humidity, moisture, soil_type, crop):
    le_soil = LabelEncoder()
    fertilizerdata['Soil Type'] = le_soil.fit_transform(fertilizerdata['Soil Type'])
    le_crop = LabelEncoder()
    fertilizerdata['Crop Type'] = le_crop.fit_transform(fertilizerdata['Crop Type'])
    soil_enc = le_soil.transform([str(soil_type)])[0]
    crop_enc = le_crop.transform([crop])[0]
    user_input = [[temp,humidity,moisture,soil_enc,crop_enc,nitrogen,potassium,phosphorus]]
    prediction = model.predict(user_input)
    return prediction[0]

def getMarketPricesAllStates():
    states = ["Kerala", "Uttrakhand", "Uttar Pradesh", "Rajasthan", "Nagaland", "Gujarat", "Maharashtra", "Tripura", "Punjab", "Bihar", "Telangana", "Meghalaya"]
    final_list = []
    for state in states:
        state = state.replace(" ", "+")
        govdata_url = f"https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key={govdata_api_key}&format=json&filters%5Bstate%5D={state}"
        response = requests.get(govdata_url)
        data = response.json()
        for entries in data["records"]:
            final_list.append(entries)

    return final_list

def GetResponse(query):
    defaults = {
    'model': 'models/text-bison-001',
    'temperature': 0.4,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
    'max_output_tokens': 1024,
    }

    palm.configure(api_key=palm_api_key)

    response = palm.chat(messages=query)
    if not response.last:
        response = palm.generate_text(prompt=query, **defaults)
        return response.result
    else:
        return response.last
