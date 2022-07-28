import os
import requests
from dotenv import load_dotenv

load_dotenv()


def create_headers_with_token(token):
    headers_token = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-NEXT-GEN-CSO": token
    }
    return headers_token


def create_auth_token():
    PACER_QA_USERNAME = os.getenv('PACER_QA_USERNAME')
    PACER_QA_PASSWORD = os.getenv('PACER_QA_PASSWORD')

    api_url = "https://qa-login.uscourts.gov/services/cso-auth"
    body = {
        "loginId": PACER_QA_USERNAME,
        "password": PACER_QA_PASSWORD,
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    response = requests.post(
        api_url,
        json=body,
        headers=headers
    )

    res_body = response.json()
    login_result = int(res_body['loginResult'])
    if login_result == 1:
        return res_body['error']
    else:
        auth_token = res_body['nextGenCSO']
        return auth_token


token = create_auth_token()

def immediate_search():
    api_url = "https://qa-pcl.uscourts.gov/pcl-public-api/rest/parties/find"
    body = {
        "firstName": "John"
    }
    headers = create_headers_with_token(token)
    response = requests.get(
        api_url,
        json=body,
        headers=headers
    )

    print(response)


immediate_search()