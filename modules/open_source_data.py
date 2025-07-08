import requests

# Example of open-source free weather and news API alternatives


def get_weather_news_stocks(query):
    # Simple keyword detection demo, enhance as needed
    if "weather" in query.lower():
        return get_open_meteo_weather()
    elif "news" in query.lower():
        return get_news()
    elif "stock" in query.lower() or "stocks" in query.lower():
        return get_stock_prices()
    else:
        return "No real-time data found for your query."


def get_open_meteo_weather():
    # Open-Meteo API (no auth, open)
    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=51.51&longitude=-0.13&current_weather=true"
        r = requests.get(url)
        data = r.json()
        temp = data["current_weather"]["temperature"]
        wind = data["current_weather"]["windspeed"]
        return f"Current weather: Temperature {temp}°C, Wind Speed {wind} km/h"
    except:
        return "Could not fetch weather data."


def get_news():
    # Example: Use NewsData.io free tier or any open news API
    # Here: we return static demo data (you can add your own)
    return "Open source news integration not implemented yet. Please add your API."


def get_stock_prices():
    # Use Yahoo Finance or Alpha Vantage (some have free tiers)
    return "Open source stock data integration not implemented yet."
