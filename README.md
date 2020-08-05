# MusicBot

Chatbot de consulta de musicas no telegram. Utiliza o Watson Assistant como gerenciador e a API do Spotify para consultas.

## Configurações

Precisa-se que se configure o arquivo de configuração config.ini com as configuraçõe de cada
api utilizada no projeto.

A seguir as variáveis que devem ser configuradas no arquivo config.ini:

* IAM_TOKEN: token IAM do Watson Assistant
* WATSON_ASSISTANT_URL: URL do Watson Assistant
* ASSISTANT_ID: ID do Assistant criado no Watson Assistant
* S2T_TOKEN: token IAM da API Watson SpeechToText
* S2T_URL: URL da API Watson SpeechToText
* T2S_TOKEN: token IAM da API Watson TextToSpeech
* T2S_URL: URL da API Watson TExtToSpeech
* BOT_TOKEN: token do bot criado no Telegram
* SPOTIFY_KEY: chave da API do SPOTIFY
* CLIENT_ID: client_id adquirido na criação do APP no Spotify Developer
* CLIENT_SECRET=client_secret adquirido na criação do APP no Spotify Developer
* TOKEN_URL=https://accounts.spotify.com/api/token

## Bibliotecas necessárias

* pip install ibm-watson
* pip install oauthlib
* pip install requests-oauthlib
* pip install requests
* pip install ibm-cloud-sdk-core
* pip install logging42
* pip install configparser2
* pip install python-telegram-bot