import requests
import time


def api_call(url, retries=3, timeout=5):
    for attempt in range(1, retries + 1):
        try:
            print(f"\nAttempt {attempt}: Sending request...")

            response = requests.get(url, timeout=timeout)

            if response.status_code == 200:
                print("✅ Request successful!")
                return response.json()

            else:
                print(f"⚠️ Server returned status code: {response.status_code}")

        except requests.exceptions.Timeout:
            print("⏰ Request timed out.")

        except requests.exceptions.RequestException as e:
            print("❌ Request failed:", e)

        # Exponential backoff
        if attempt < retries:
            wait_time = 2 ** (attempt - 1)
            print(f"🔄 Retrying after {wait_time} seconds...")
            time.sleep(wait_time)

    print("\n❌ API request failed after all retries.")
    return None


# API URL
url = "https://jsonplaceholder.typicode.com/posts/1"

# Call API
result = api_call(url)

if result:
    print("\nAPI Response:")
    print(result)