import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def get_new_user_token():
    user_response = post_new_user(data.user_body)
    return user_response.json()["authToken"]

autorization = get_new_user_token()
header_auto = {"Content-Tipe": "application/json", "Autorization": f'Bearer [autorization_Token]'}


def post_new_client_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

