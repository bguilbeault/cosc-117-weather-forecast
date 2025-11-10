CITY = "Chengdu"

WEATHER_EMOJI = {
    # Clear/Sunny
    "1000": "☀️",  # Sunny / Clear

    # Cloudy
    "1003": "🌥️",  # Partly cloudy
    "1006": "☁️",  # Cloudy
    "1009": "☁️",  # Overcast

    # Fog / Mist
    "1030": "🌫️",  # Mist
    "1135": "🌫️",  # Fog

    # Light Rain / Drizzle
    "1063": "🌦️",  # Patchy rain possible
    "1150": "🌦️",  # Patchy light drizzle
    "1153": "🌦️",  # Light drizzle
    "1180": "🌦️",  # Patchy light rain
    "1183": "🌦️",  # Light rain
    "1240": "🌦️",  # Light rain shower

    # Moderate / Heavy Rain
    "1186": "🌧️",  # Moderate rain at times
    "1189": "🌧️",  # Moderate rain
    "1192": "🌧️",  # Heavy rain at times
    "1195": "🌧️",  # Heavy rain
    "1243": "🌧️",  # Moderate or heavy rain shower
    "1246": "🌧️",  # Torrential rain shower

    # Snow
    "1066": "🌨️",  # Patchy snow possible
    "1117": "🌨️",  # Blizzard
    "1210": "🌨️",  # Patchy light snow
    "1213": "🌨️",  # Light snow
    "1216": "🌨️",  # Patchy moderate snow
    "1219": "🌨️",  # Moderate snow
    "1222": "🌨️",  # Patchy heavy snow
    "1225": "🌨️",  # Heavy snow
    "1255": "🌨️",  # Light snow showers
    "1258": "🌨️",  # Moderate or heavy snow showers

    # Sleet / Ice Pellets
    "1069": "🌨️",  # Patchy sleet possible
    "1204": "🌨️",  # Light sleet
    "1207": "🌨️",  # Moderate or heavy sleet
    "1237": "🌨️",  # Ice pellets
    "1249": "🌨️",  # Light sleet showers
    "1252": "🌨️",  # Moderate or heavy sleet showers
    "1261": "🌨️",  # Light showers of ice pellets
    "1264": "🌨️",  # Moderate or heavy showers of ice pellets

    # Freezing Conditions
    "1072": "🥶",  # Patchy freezing drizzle possible
    "1147": "🥶",  # Freezing fog
    "1168": "🥶",  # Freezing drizzle
    "1171": "🥶",  # Heavy freezing drizzle
    "1198": "🥶",  # Light freezing rain
    "1201": "🥶",  # Moderate or heavy freezing rain

    # Thunder
    "1087": "⛈️",  # Thundery outbreaks possible
    "1273": "⛈️",  # Patchy light rain with thunder
    "1276": "⛈️",  # Moderate or heavy rain with thunder
    "1279": "⛈️",  # Patchy light snow with thunder
    "1282": "⛈️",  # Moderate or heavy snow with thunder
    
    # Wind
    "1114": "🌬️",  # Blowing snow
}

POLLUTANTS = {
    "co": "Carbon Monoxide",
    "no2": "Nitrogen Dioxide",
    "o3": "Ozone",
    "so2": "Sulfur Dioxide",
    "pm2_5": "Fine Particulate Matter (PM2.5)",
    "pm10": "Coarse Particulate Matter (PM10)"
}

# AQI Levels
AQI_INTERVALS = {
    "co" : [
        (1, 2000),
        (2, 4000),
        (3, 14000),
        (4, 24000),
        (5, 36000),
        (6, 48000),
        (7, 60000)
    ],

    "no2": [
        (1, 40),
        (2, 80),
        (3, 180),
        (4, 280),
        (5, 565),
        (6, 750),
        (7, 940)
    ],

    "o3": [
        (1, 160),
        (2, 200),
        (3, 300),
        (4, 400),
        (5, 800),
        (6, 1000),
        (7, 1200),
    ],


    "so2" : [
        (1, 50),
        (2, 150),
        (3, 475),
        (4, 800),
        (5, 1600),
        (6, 2100),
        (7, 2620)
    ],

    "pm2_5":[
        (1, 35),
        (2, 75),
        (3, 115),
        (4, 150),
        (5, 250),
        (6, 350),
        (7, 500)
    ],

    "pm10": [
        (1, 50),
        (2, 150),
        (3, 250),
        (4, 350),
        (5, 420),
        (6, 500),
        (7, 600)
    ]
}

INTERVAL_DESC = {
    1: "Exellent",
    2: "Good",
    3: "Lightly Polluted",
    4: "Moderately Polluted",
    5: "Heavily Polluted",
    6: "Severely Polluted",
    7: "Dangerous!" 

}