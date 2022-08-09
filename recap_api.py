import os
import requests
import urllib.request
import shutil
from url import Url
from constants import constants
from recap_types import BuildBaseUrlProps
from dotenv import load_dotenv
import json

load_dotenv()


class RecapApi:
    url = Url()

    def __init__(self, token: str) -> None:
        self.token: str = token

    def search(self):
        url_params: BuildBaseUrlProps = {
            'url': constants['RECAP_URL'],
            'path': constants['RECAP_API_SEARCH_PATH'],
            'query': {
                "order_by": "dateFiled asc",
                "available_only": "on",
                "type": "r",
                "filed_after": "08/08/2022",
                # "filed_before": "06/02/2022",
                "court": "dcd",
            }
        }
        url = self.url.build(url_params)
        print(url)
        response = requests.get(
            url,
            headers=self.url.headers(self.token)
        )
        print(response.text)
        return response.json()

    def download(self, path: str):
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
        with urllib.request.urlopen(url) as response, open('filio2.pdf', 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

    # Paginated searching method


recap = RecapApi(os.environ['RECAP_TOKEN'])
res = recap.search()
res_count = res['count']
first_name = res['results'][0]['caseName']
print('Count', res_count)
print('First name', first_name)

# Notes it's been a while huh?
# Main issue is trying to see if the data matches up with the Website API
# Then determine what is really the source of truth
# If that cannot be figured out
# Figure out what type of documents are you downloading
# What are their types
# How can you uniquely identify a document
# How can you get identifies that will match up from other PACER sources, should you move beyond RECAP
# I believe dateFiled is not date doc was issued in court but when it was updated by RECAP
# Searching by casename is fuzzy do not reccomend
# DISREGARD ALL, I passed in type=r which matches the search API that returns Document-oriented results from the RECAP Archive


# print(json.dumps(res))

# try:
# res_count = res['count']
# res1 = res['results'][0]
# res2 = res['results'][1]
# res3 = res['results'][2]
# local_path = res1['local_path']
# local_path2 = res2['local_path']

# print(json.dumps(res))
# print(json.dumps(res2))
# print(json.dumps(res3))
# except AttributeError:
#     raise TypeError("You fucked up there's no response")

# recap.download(local_path2)
