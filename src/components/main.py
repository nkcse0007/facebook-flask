import json


def text(s_id, message):
    return json.dumps({
        "recipient": {
            "id": s_id
        },
        "message": {
            "text": message
        }
    })


def attachment(s_id, url, types="image"):
    return json.dumps({
        "recipient": {
            "id": s_id
        },
        "message": {
            "attachment": {
                "type": types.lower(),
                "payload": {
                    "url": url,
                    "is_reusable": True
                }
            }
        }
    })


def image(s_id, elements):
    return json.dumps({
        "recipient": {
            "id": s_id
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": elements
                }
            }
        }
    })
