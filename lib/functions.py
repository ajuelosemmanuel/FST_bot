import re

def parser(file):
    """
    Parsing function for osu! maps links.
    
    Args:
        file (str): path to a text file that contains osu! maps links (one per line).

    Returns:
        list[int]: list of every map ID.
    """
    
    # If there is no path, returns an empty list.
    if file == "":
        return []
    res=[]
    f = open(file, 'r')
    # Parsing every link using regex
    for lines in f.readlines():
        res.append((re.findall("([^\/]+$)", lines))[0].strip())
    return res

def parser_pool(nm="", hd="", hr="", dt="", tb="", ez="", ht="", fl=""):
    """
    Parsing function for multiple osu! maps links.
    
    Args:
        nm (str, optional): path to a text file that contains osu! maps links for the nomod pool. Defaults to "".
        hd (str, optional): path to a text file that contains osu! maps links for the hidden pool. Defaults to "".
        hr (str, optional): path to a text file that contains osu! maps links for the hardrock pool. Defaults to "".
        dt (str, optional): path to a text file that contains osu! maps links for the doubletime pool. Defaults to "".
        tb (str, optional): path to a text file that contains osu! maps links for the tiebreaker pool. Defaults to "".
        ez (str, optional): path to a text file that contains osu! maps links for the easy pool. Defaults to "".
        ht (str, optional): path to a text file that contains osu! maps links for the halftime pool. Defaults to "".
        fl (str, optional): path to a text file that contains osu! maps links for the flashlight pool. Defaults to "".

    Returns:
        dict: dictionnary containing a key for each pool, a freemod pool which is the mix of the hidden and hardrock pools (Lexonox's decision), and the "AvailablePools".
        Values are lists of maps IDs, except for "AvailablePools" which contains the list of the available pools (obvious but still).
    """
    res = {
        "NM": parser(nm),
        "HD": parser(hd),
        "HR": parser(hr),
        "DT": parser(dt),
        "TB": parser(tb),
        "EZ": parser(ez),
        "HT": parser(ht),
        "FL": parser(fl)
    }
    res["FM"] = res["HD"] + res["HR"]
    av = [el for el in res.keys() if len(res[el])!=0]
    res["AvailablePools"] = av
    return res