import os
import json
from typing import List
from dotenv import load_dotenv
from recap_api import RecapApi
from recap_types import RecapSearchResultResponseProps

load_dotenv()


class Collect:
    documents = []  # todo define type

    def __init__(self) -> None:
        recap_token: str = os.environ['RECAP_TOKEN']
        self.recap = RecapApi(recap_token)

    def create_name_from_record(self, record: RecapSearchResultResponseProps):
        return f"{record['court_id']}-_-{record['caseName']}-_-{record['entry_date_filed']}.pdf"

    def get_all_paginated_records(self, court: str, filed_before: str, filed_after: str):
       return self.recap.search_paginated(court, filed_before, filed_after)

    def download_records(self, records: List[RecapSearchResultResponseProps]):
        records = records[0:5]
        for record in records:
            self.recap.download(self.create_name_from_record(record), record['filepath_local'])


collect = Collect()
records = collect.get_all_paginated_records('dcd', '07/01/22', '08/01/22')
collect.download_records(records)
# Notes it's been a while huh?
# Figure out what type of documents are you downloading
# What are their types
# How can you uniquely identify a document
# How can you get identifies that will match up from other PACER sources, should you move beyond RECAP
# Searching by casename is fuzzy do not reccomend


# Work on updating search to handle pagination
# store all documents in documents on search (mimic what data you need grabbed once a document has been searched and downloaded)
