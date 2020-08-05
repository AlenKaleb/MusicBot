import musics


def action_handler(action, parameters, return_var):
    return_values = {}
    if action == 'lancamento' or action == 'genero':
        return_values = get_recommends(parameters, return_var)
    elif action == 'search':
        return_values = search_musics(parameters, return_var)
    return {
            'skills': {
                'main skill': {
                    'user_defined': return_values
                }
            }
        }

def get_recommends(parameters, return_var):
    music_titles = musics.get_launch_and_genre(parameters)

    # tratando retorno das musicas
    music_string = '\n\n'
    for music in music_titles:
        music_string += music + ',\n'
    music_string = music_string[:-2]
    return {
        return_var: music_string
    }

def search_musics(parameters, return_var):
    query = parameters['termo']
    music_titles = musics.search_musics(query)

    # tratando retorno das musicas
    music_string = '\n\n'
    for music in music_titles:
        music_string += music + ',\n'
    music_string = music_string[:-2]
    return {
        return_var: music_string
    }


