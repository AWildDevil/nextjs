import requests
import time

url = "https://discord.com/api/v9/channels/903164072856547360  /messages"  # Replace with the appropriate channel URL
image_path = "try.jpg"  # Replace with the path to your image file

header = {
    'Authorization': 'NzU1MDczNzQ2MTgzNjUxMzMy.GDNqQv.3SLh6Ykk-2BYII_LZvmMnLLEqyQ3iSGN0XS5lI'
}

while True:
    try:
        payload = {
            'content': "MQvEQsQSYXGvthiXbh6YPVnhES59UqXQcb",
        }

        files = {
            'file': open(image_path, 'rb'),
        }

        r = requests.post(url, headers=header, data=payload, files=files)
        r.raise_for_status()  # Raise an exception if the request was unsuccessful
        print("Message sent successfully")
    except requests.exceptions.RequestException as e:
        print("Error sending message:", str(e))
        print("Retrying in 1 second...")
        time.sleep(0)
        continue

    # Add a delay of 30 seconds before the next iteration
    time.sleep(60)
