# Surf Forecast for Morning Sessions in Rio de Janeiro

## Description

This Python application retrieves the weather forecast for **Rio de Janeiro** between **5:00 AM and 8:00 AM** for the next **3 days**, specifically for those who surf in the early morning. The app uses the **WeatherAPI** to gather data and sends notifications via **Twilio SMS**.

### Features

- Fetches weather forecast data between 5:00 AM and 8:00 AM for the next 3 days.
- Filters specific hours to provide relevant morning weather information.
- Sends weather alerts via **Twilio SMS**.
- Key information includes: date, hour, weather condition, temperature, and probability of rain.

## Requirements

### API Keys

1. **Twilio**: You need a Twilio account to send SMS messages. Place your credentials in a `credentials.json` file at the root of the project.
2. **WeatherAPI**: You will need an API key from WeatherAPI to get weather data.

The `credentials.json` file should have the following structure:

```json
{
    "TWILIO": {
        "ACCOUNT_SID": "your_twilio_account_sid",
        "AUTH_TOKEN": "your_twilio_auth_token",
        "PHONE_NUMBER": "your_twilio_phone_number"
    },
    "WEATHER_API": {
        "API_KEY": "your_weather_api_key"
    }
}
