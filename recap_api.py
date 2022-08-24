import os
from typing import List, cast
import requests
import urllib.request
import shutil
import moment
from url import Url
from constants import constants
from recap_types import BuildBaseUrlProps, RecapSearchResponseProps, RecapSearchResultResponseProps
from dotenv import load_dotenv
import json

load_dotenv()


class RecapApi:
    url = Url()

    def __init__(self, token: str) -> None:
        self.token: str = token


    def search(self, court: str, filed_after: str, filed_before: str) -> RecapSearchResponseProps:
        url_params: BuildBaseUrlProps = {
            'url': constants['RECAP_URL'],
            'path': constants['RECAP_API_SEARCH_PATH'],
            'query': {
                "order_by": "dateFiled asc",
                "available_only": "on",
                "type": "r",
                "filed_after": filed_after,
                "filed_before": filed_before,
                "court": court,
            }
        }
        url = self.url.build(url_params)
        response = requests.get(
            url,
            headers=self.url.headers(self.token)
        )

        return response.json()

    def search_paginated(self, court: str, filed_after: str, filed_before: str) -> List[RecapSearchResultResponseProps]:
        all_records: List[RecapSearchResultResponseProps] = []
        cur_res = self.search(court, filed_after, filed_before)
        is_more = cur_res['next'] != None
        all_records = [*all_records, *cur_res['results']]

        while is_more:
            next_url = cast(str, cur_res['next'])
            if is_more:
                res = requests.get(
                    next_url,
                    headers=self.url.headers(self.token)
                )
                cur_res = res.json()
                is_more = cur_res['next'] != None
                all_records = [*all_records, *cur_res['results']]
                
        return all_records

    def download(self, name: str, path: str):
        url_params: BuildBaseUrlProps = {
            'url': constants['RECAP_DOWNLOAD_URL'],
            'path': path,
            'query': None
        }
        url = self.url.build(url_params)

        response = requests.get(
            url,
            headers=self.url.headers(self.token)
        )
        with urllib.request.urlopen(url) as response, open(f'pacer/pdfs/{name}', 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
