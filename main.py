import requests
import pandas as pd
import matplotlib.pyplot as plt
from twilio.rest import Client
from tqdm import tqdm
import json


def load_credentials(filepath='credentials.json'):
    """
    Load credentials from a JSON file.
    """
    with open(filepath) as file:
        credentials = json.load(file)
    return credentials


# Función para obtener los datos del pronóstico por hora para cada día
def get_forecast(day, hour_index):
        forecast = day['hour'][hour_index]
        fecha = forecast['time'].split()[0]
        hora = int(forecast['time'].split()[1].split(':')[0])
        condicion = forecast['condition']['text']
        temperatura = forecast['temp_c']
        lluvia = forecast['will_it_rain']
        prob_lluvia = forecast['chance_of_rain']

        return fecha, hora, condicion, temperatura, lluvia, prob_lluvia


# Función para obtener los datos del clima para Rio de Janeiro

def fetch_weather_data(city, api_key, days=3):
    """
    Fetch weather data for a city using the WeatherAPI.
    """
    url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days={days}&aqi=no&alerts=no'
    response = requests.get(url)
    return response.json()


def build_forecast_dataframe(cities, api_key, days=3):

    data = []
    for city in cities:
        response = fetch_weather_data(city, api_key, days)
        for day in response['forecast']['forecastday']:  # Itera sobre todos los días del pronóstico
            for i in tqdm(range(len(day['hour'])), desc=f'Processing {city} for {day["date"]}'):
                forecast = get_forecast(day, i)
                data.append((city,) + forecast)

    columns = ['City', 'Fecha', 'Hora', 'Condicion', 'Temperatura', 'Lluvia', 'prob_lluvia']
    return pd.DataFrame(data, columns=columns)


# Función para construir el DataFrame con los datos del pronóstico para las horas específicas (5 a 8 AM)
def build_forecast_dataframe(city, api_key, days=3):
    data = []
    response = fetch_weather_data(city, api_key, days)

    for day in response['forecast']['forecastday']:  # Iterar sobre los 3 días
        for i in range(len(day['hour'])):
            hour = int(day['hour'][i]['time'].split()[1].split(':')[0])
            if 5 <= hour <= 8:  # Filtrar solo entre 5 AM y 8 AM
                forecast = get_forecast(day, i)
                data.append((city,) + forecast)

    columns = ['City', 'Fecha', 'Hora', 'Condicion', 'Temperatura', 'Lluvia', 'prob_lluvia']
    return pd.DataFrame(data, columns=columns)

# Función para enviar alerta vía Twilio
def send_alert_via_twilio(alert_df, city, client, phone_number, to_phone_number):
    if not alert_df.empty:
        message_body = f"Pronóstico de surf para {city} en las mañanas (5-8 AM) de los próximos 3 días:\n"
        for _, row in alert_df.iterrows():
            message_body += (
                f"Fecha: {row['Fecha']} - Hora: {row['Hora']}h - Condición: {row['Condicion']} - "
                f"Temp: {row['Temperatura']}°C - Probabilidad de lluvia: {row['prob_lluvia']}%\n"
            )

        if len(message_body) > 1600:
            message_body = message_body[:1600] + "\nMensaje truncado. Consulte la aplicación para más detalles."

        message = client.messages.create(
            body=message_body,
            from_=phone_number,
            to=to_phone_number
        )
        print('Mensaje enviado: ' + message.sid)

def main():
    """
    Main function to execute the weather alert.
    """
    # Cargar credenciales
    credentials = load_credentials()

    # Parámetros de configuración
    city = "Rio de Janeiro"
    api_key = credentials['WEATHER_API']['API_KEY']
    phone_number = credentials['TWILIO']['PHONE_NUMBER']

    to_number_phone ='+5521977319999'

    # Crear cliente Twilio
    client = Client(credentials['TWILIO']['ACCOUNT_SID'], credentials['TWILIO']['AUTH_TOKEN'])

    # Construir DataFrame con los pronósticos
    df = build_forecast_dataframe(city, api_key, days=3)
    print(df)

    # Enviar alertas si hay condiciones climáticas adversas
    send_alert_via_twilio(df, city, client, phone_number, to_number_phone)

if __name__ == "__main__":
    main()
