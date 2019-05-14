from flask import Blueprint, request, jsonify, make_response, Response
import os
import json
from src.handler.main import handle_event

hook_route = Blueprint('hook_route', __name__)


@hook_route.route("/webhook", methods=['GET', 'POST'])
def hook():
    if request.method == "GET":
        if request.args.get('hub.verify_token', '') == os.environ.get("VERIFY_TOKEN"):
            print("Verification successful!")
            return request.args.get('hub.challenge', '')
        else:
            return make_response(jsonify(status=False), 401)
    else:
        body = json.loads(request.get_data().decode())
        print("Body:",body)
        for entry in body['entry']:
            event = entry['messaging'][0]
            print(event)
            handler = handle_event(event)
            print(handler)
        return "success"
