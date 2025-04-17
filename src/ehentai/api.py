from ehentai.fetch import *


def get_Page(url: str=URL,params=None,encoding: str=None)->Page:
    """
    Args:
        url (str, optional): ehentai has the galleries. Defaults to URL.
        params (fetch.keyword, optional): using this to search. Defaults to None.
        encoding (str, optional): using this when encoding is wrong. Defaults to None.

    Returns:
        Page:
            attr:gl_table,rangebar,search_text
    """
    return Page(get_sp(url,params,encoding))

def search(search_context,cats,rating,sh_removed,torrent)->Page:
    
    return get_Page(URL,keyword(f_search=search_context,))
    pass