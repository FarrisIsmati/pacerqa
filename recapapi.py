# Test using RECAP API to pull free court documents down that have already been purchased on the site
import os
from typing import Any, Mapping
from typing_extensions import TypedDict
import requests
from urllib.parse import urlencode, urlunsplit
from dotenv import load_dotenv


class BuildBaseUrlProps(TypedDict):
    url: str
    path: str
    query: Mapping[Any, Any]


load_dotenv()

RECAP_TOKEN: str = os.getenv('RECAP_TOKEN') if os.getenv('RECAP_TOKEN') is not None else ''


def create_headers_with_token(token: str):
    headers_token = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": token
    }
    return headers_token


headers = create_headers_with_token(RECAP_TOKEN)

PDF_URL = 'https://storage.courtlistener.com/'


def build_base_url(props: BuildBaseUrlProps) -> str:
    url = props['url']
    query = props['query']
    path = props['path']
    scheme = 'http'
    netloc: str = url
    qs: str = urlencode(query)

    return urlunsplit((scheme, netloc, path, qs, ''))


def search():
    url_params: BuildBaseUrlProps = {
        'url': 'courtlistener.com',
        'path': '/api/rest/v3/search/',
        'query': {
            "court": "dcd",
            "filed_after": "07/01/2022",
            "available_only": "on",
            "order_by": "dateFiled desc",
        }
    }
    url = build_base_url(url_params)

    response = requests.get(
        url,
        headers=headers
    )

    return response.text


print(search())
