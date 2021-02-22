import requests

# Stop rest app service
try:
    requests.get('http://127.0.0.1:5000/stop_server')
except requests.exceptions.ConnectionError as e:
    print("Connection refused to rest_app service", e)


# Stop web app service
try:
    requests.get('http://127.0.0.1:5001/stop_server')
except requests.exceptions.ConnectionError as e:
    print("Connection refused to web_app service", e)
