## It's a Python Client for WeatherAPI.com

## Usage
**To get the weather just init the Client:**
```python
client = weatherapi.Client(
    session=httpx.Client(
        base_url="http://api.weatherapi.com/v1",
        timeout=httpx.Timeout(10.),
        limits=httpx.Limits(
            max_connections=10,
        ),
    ),
    api_key="***API_KEY***",
)
```

**and call the method:**
```python
weather = client.get_realtime_weather("New-York")
```
