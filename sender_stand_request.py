import configuration
import data
import requests

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body,headers=data.headers)

def post_new_client_kit(body):
    headers = data.headers.copy()
    authorization = post_new_user(data.user_body).json()['authToken']
    headers["Authorization"] = f"Bearer {authorization}"
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, json=body,headers=data.headers)
