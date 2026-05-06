import requests
import time

API_URL = "https://api.github.com"

def check_api(url):
    start = time.time()
    
    try:
        response = requests.get(url)
        end = time.time()

        response_time = round(end - start, 2)

        print("API URL:", url)
        print("Status Code:", response.status_code)
        print("Response Time:", response_time, "seconds")

        if response.status_code == 200:
            print("Status: SUCCESS")
        else:
            print("Status: FAILED")

    except Exception as e:
        print("Error:", e)

# Run test
check_api(API_URL)