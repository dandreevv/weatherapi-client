import httpx

import weatherapi


def main() -> None:
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
    response = client.get_realtime_weather("New-York")
    print(response)


if __name__ == "__main__":
    main()
