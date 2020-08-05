import requests
import auth_spot
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

base_url = 'https://api.spotify.com/v1'
client_id = config['SPOTIFY']['CLIENT_ID']
client_secret = config['SPOTIFY']['CLIENT_SECRET']
token_url = config['SPOTIFY']['TOKEN_URL']

def get_token():
    # token de acesso ao spotify
    # client_id, cliente_secret de uma conta criada no spotify
    token = auth_spot.get_token(client_id,client_secret,token_url)
    return token

def get_launch_and_genre(params):
    endpoint = ''
    if 'seed_genres' in params:
        endpoint = '/recommendations'
    else:
        endpoint = '/browse/new-releases'

    token = get_token()['access_token']
    final_url = base_url + endpoint + '?' + 'access_token=' + token +'&offset=0&limit=10'
    if 'seed_genres' in params:
        final_url = final_url+'&seed_genres='+params['seed_genres']

    response = requests.get(final_url).json()
    if 'seed_genres' in params:
        return ['Album: '+music['album']['name']+' - '+music['album']['external_urls']['spotify'] for music in response['tracks']]
    elif 'lancamento' in params:
        return ['Album: '+music['name']+' - '+music['external_urls']['spotify'] for music in response['albums']['items']]

def search_musics(query):
    endpoint = '/search'
    token = get_token()['access_token']
    parameters = '?q=' + query + '&type=track&offset=0&limit=10' + '&access_token=' + token
    final_url = base_url + endpoint + parameters
    response = requests.get(final_url).json()
    return ['Música: '+music['name']+' - '+music['external_urls']['spotify'] for music in response['tracks']['items']]

