def safe_get(data, path, default_value = None):
    """ 
        object: could be a dictionary or an array
        path: has to be an string .-splited or []-splited 

        ToDo: better parse of path using regex
    """
    path = path.replace("[", ".").replace("[", ".").replace("..", ".")
    if(path[-1] == "."):
        path = path[:-1]
    tracks = path.split('.')
    def getFromArray(data, idx):
        return data[idx]
    def getFromDict(data, key):
        return data.get(key, None)
    try:
        aux = data
        for track in tracks:
            if(type(aux) is dict):
                aux = getFromDict(aux, track)
            elif(type(aux) is list):
                aux = getFromArray(aux, track)
            elif(type(aux) is tuple):
                aux = getFromDict(aux, track)
            else:
                raise KeyError('Sorry, but {} is not a valid route in a variable type {}'.format(track, type(aux)))
        return aux
    except:
        return default_value