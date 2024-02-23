import requests

def get_weather(city, unit='metric'):
    api_key = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your actual API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={unit}'
    
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return data
    else:
        return None

def display_weather(data, unit='Celsius'):
    if data:
        print(f"Weather in {data['name']}:")
        print(f"Temperature: {data['main']['temp']} {unit}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
        print(f"Weather Conditions: {data['weather'][0]['description']}")
    else:
        print("Error: Unable to fetch weather data. Please check your input and try again.")

def main():
    city = input("Enter the city name: ")
    unit = input("Enter the temperature unit (Celsius/C or Fahrenheit/F): ").lower()

    if unit == 'celsius' or unit == 'c':
        unit = 'metric'
    elif unit == 'fahrenheit' or unit == 'f':
        unit = 'imperial'
    else:
        print("Invalid unit input. Defaulting to Celsius.")
        unit = 'metric'

    weather_data = get_weather(city, unit)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
