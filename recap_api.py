import os
import requests
from url import Url
from constants import constants
from recap_types import BuildBaseUrlProps
from dotenv import load_dotenv

load_dotenv()


class RecapApi:
    url = Url()

    def __init__(self, token: str) -> None:
        self.token: str = os.environ['RECAP_TOKEN']

    def search(self):
        url_params: BuildBaseUrlProps = {
            'url': constants['RECAP_URL'],
            'path': constants['RECAP_API_SEARCH_PATH'],
            'query': {
                "court": "dcd",
                "filed_after": "07/01/2022",
                "available_only": "on",
                "order_by": "dateFiled desc",
            }
        }
        url = self.url.build(url_params)

        response = requests.get(
            url,
            headers=self.url.headers(self.token)
        )

        return response.text
