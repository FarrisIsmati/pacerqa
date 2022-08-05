from recap_types import BuildBaseUrlProps
from urllib.parse import urlencode, urlunsplit


class Url:
    def headers(self, token: str):
        headers_token = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": token
        }
        return headers_token

    def build(self, props: BuildBaseUrlProps) -> str:
        url = props['url']
        query = props['query']
        path = props['path']
        scheme = 'http'
        netloc: str = url
        qs: str = urlencode(query)

        return urlunsplit((scheme, netloc, path, qs, ''))
