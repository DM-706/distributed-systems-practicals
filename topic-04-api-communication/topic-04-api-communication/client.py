import requests
from requests import RequestException

API_URL = "http://127.0.0.1:5000"


def request_endpoint(endpoint):
    url = f"{API_URL}{endpoint}"
    print(f"Requesting: {url}")

    try:
        response = requests.get(url, timeout=5)
        print(f"Status code: {response.status_code}")

        if response.headers.get("content-type", "").startswith("application/json"):
            print(f"Response: {response.json()}")
        else:
            print("The API did not return JSON.")
    except RequestException:
        print("The API could not be reached.")

    print()


if __name__ == "__main__":
    request_endpoint("/health")

