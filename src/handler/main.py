import json
from src.request.main import *
from src.components.main import text, image


def handle_event(event):
    if 'message' in event:
        print("message event")
        if 'text' in event['message']:
            print(make_request(image(event['sender']['id'], [
                {
                    "title": "Sorry! I'm learning now.",
                    "image_url": "https://www.relinns.com/wp-content/themes/twentyseventeen-child/img/bitmap.png",
                    "subtitle": "Please Choose a option.",
                    "default_action": {
                        "type": "web_url",
                        "url": "https://relinns.com",
                        "webview_height_ratio": "tall",
                    },
                    "buttons": [
                        {
                            "type": "web_url",
                            "url": "https://relinns.com",
                            "title": "View Website"
                        }, {
                            "type": "phone_number",
                            "title": "Call Us",
                            "payload": "1234567890"
                        }
                    ]
                }
            ])))
        elif 'attachments' in event['message']:
            print("attachment event")
        else:
            print(event['message'])
    elif 'postback' in event:
        print("postback event")
        payload = json.loads(event['postback']['payload'])
        if 'event' in payload and payload['event'] == 'start':
            print("get_started")
            flow = get_flow(json.dumps({
                "botId": 179,
                "event": "get_started"
            }))
            print(flow)
            for response in flow['response']:
                print(len(flow['response']))
                print("TYPE: ", response['type'])
                if 'text' in response['type']:
                    print(make_request(text(event['sender']['id'], response['payload']['text'])))
                if 'attachment' in response['type']:
                    print("attachment found: ")
                    print(make_request(image(event['sender']['id'], [
                        {"title": response['payload']['text'], "image_url": response['payload']['url']}])))
    else:
        print("unknown event")
    return True
