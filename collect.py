import os
import json
from dotenv import load_dotenv
from recap_api import RecapApi

load_dotenv()


class Collect:
    documents = []  # todo define type

    def __init__(self) -> None:
        recap_token: str = os.environ['RECAP_TOKEN']
        self.recap = RecapApi(recap_token)

    def get_range(self, court: str, filed_before: str, filed_after: str):
        response = self.recap.search(court, filed_before, filed_after)
        url1 = response['results'][0]['absolute_url']
        print(url1)


collect = Collect()
range = collect.get_range('dcd', '07/01/22', '08/01/22')

# Notes it's been a while huh?
# Figure out what type of documents are you downloading
# What are their types
# How can you uniquely identify a document
# How can you get identifies that will match up from other PACER sources, should you move beyond RECAP
# Searching by casename is fuzzy do not reccomend


# Work on updating search to handle pagination
# store all documents in documents on search (mimic what data you need grabbed once a document has been searched and downloaded)
