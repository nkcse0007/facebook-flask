import requests
import os


def make_request(payload):
    response = requests.post("https://graph.facebook.com/v2.6/me/messages",
                             params={'access_token': os.environ.get("PAGE_TOKEN")},
                             headers={'Content-Type': 'application/json'},
                             data=payload)
    return response.json()


def get_flow(payload):
    response = requests.post(os.environ.get("FLOW_URL"),
                             headers={'Content-Type': 'application/json'},
                             data=payload)
    return response.json()
