# Pronóstico de Surf para las Mañanas en Rio de Janeiro

## Descripción

Este proyecto es una aplicación en Python que consulta el pronóstico del tiempo para la ciudad de **Rio de Janeiro** entre las **5:00 AM y 8:00 AM** durante los próximos **3 días**. La aplicación está orientada a quienes hacen surf por la mañana y envía notificaciones con las condiciones climáticas a través de **Twilio SMS**.

### Funcionalidades

- Obtención del pronóstico del clima entre las 5:00 AM y 8:00 AM de los próximos 3 días.
- Filtrado por horas para obtener información específica para la mañana.
- Envío de alertas climáticas vía SMS utilizando **Twilio**.
- Información clave: fecha, hora, condición climática, temperatura, y probabilidad de lluvia.

## Requisitos

### Claves API

1. **Twilio**: Necesitarás una cuenta de Twilio para enviar mensajes SMS. Coloca tus credenciales en un archivo `credentials.json` en la raíz del proyecto.
2. **WeatherAPI**: Necesitarás una clave de API de WeatherAPI para obtener datos del clima.

El archivo `credentials.json` debe tener la siguiente estructura:

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
