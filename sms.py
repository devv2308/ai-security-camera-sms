import requests

def send_sms():

    url = "http://10.40.65.132:8080/send-sms"

    payload = {
        "number": "7376094634",
        "message": "Motion detected!"
    }

    response = requests.post(
        url,
        json=payload
    )

    print(response.status_code)
    print(response.text)