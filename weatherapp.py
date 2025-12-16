import requests


class Weather:
    def __init__(self, api_key, city):
        self.api_key = api_key
        self.city = city
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def fetch_weather(self):
        """
        Fetch weather data from OpenWeatherMap API
        """
        try:
            params = {
                "q": self.city,
                "appid": self.api_key,
                "units": "metric"   # Celsius
            }

            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # Raises HTTPError for bad responses

            return response.json()

        except requests.exceptions.HTTPError:
            print("❌ City not found or invalid API key.")
        except requests.exceptions.ConnectionError:
            print("❌ Network error. Please check your internet connection.")
        except requests.exceptions.Timeout:
            print("❌ Request timed out.")
        except requests.exceptions.RequestException as e:
            print("❌ Something went wrong:", e)

        return None

    def display_weather(self, data):
        """
        Display formatted weather report
        """
        try:
            city_name = data["name"]
            country = data["sys"]["country"]
            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            weather_desc = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]

            print("\n🌤️  Weather Report")
            print("-" * 30)
            print(f"City        : {city_name}, {country}")
            print(f"Temperature : {temperature} °C")
            print(f"Feels Like  : {feels_like} °C")
            print(f"Humidity    : {humidity} %")
            print(f"Pressure    : {pressure} hPa")
            print(f"Condition   : {weather_desc.capitalize()}")
            print(f"Wind Speed  : {wind_speed} m/s")
            print("-" * 30)

        except KeyError:
            print("❌ Error parsing weather data.")


def main():
    print("===== Weather Report Console App =====")

    api_key = "f2455cc990ba17d72072643df1623f13"  # 🔑 Replace with your API key
    city = input("Enter city name: ")

    weather = Weather(api_key, city)
    data = weather.fetch_weather()

    if data:
        weather.display_weather(data)


if __name__ == "__main__":
    main()
