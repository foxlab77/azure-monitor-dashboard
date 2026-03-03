import os
import json
import requests
import datetime
import hashlib
import hmac
import base64

workspace_id = os.environ.get("LOG_WORKSPACE_ID")
workspace_key = os.environ.get("LOG_WORKSPACE_KEY")
log_type = "CustomAppLogs"  # Name of the table in Log Analytics

def build_signature(customer_id, shared_key, date, content_length, method, content_type, resource):
    x_headers = 'x-ms-date:' + date
    string_to_hash = f"{method}\n{content_length}\n{content_type}\n{x_headers}\n{resource}"
    bytes_to_hash = bytes(string_to_hash, 'utf-8')
    decoded_key = base64.b64decode(shared_key)
    encoded_hash = hmac.new(decoded_key, bytes_to_hash, digestmod=hashlib.sha256).digest()
    encoded_hash = base64.b64encode(encoded_hash).decode()
    authorization = f"SharedKey {customer_id}:{encoded_hash}"
    return authorization

def send_log(message: str):
    body = json.dumps([{"message": message, "timestamp": str(datetime.datetime.utcnow())}])
    method = 'POST'
    content_type = 'application/json'
    resource = '/api/logs'
    rfc1123date = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
    content_length = len(body)

    signature = build_signature(workspace_id, workspace_key, rfc1123date, content_length, method, content_type, resource)

    uri = f"https://{workspace_id}.ods.opinsights.azure.com{resource}?api-version=2016-04-01"

    headers = {
        'Content-Type': content_type,
        'Authorization': signature,
        'Log-Type': log_type,
        'x-ms-date': rfc1123date
    }

    response = requests.post(uri, data=body, headers=headers)
    if response.status_code >= 200 and response.status_code <= 299:
        return True
    else:
        print(response.text)
        return False