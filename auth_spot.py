from oauthlib.oauth2 import LegacyApplicationClient
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session


def get_token(client_id,client_secret, token_url):
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=token_url, client_id=client_id, client_secret=client_secret)
    return token

