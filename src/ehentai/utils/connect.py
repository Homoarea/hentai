from bs4 import BeautifulSoup
import chardet
import requests

from ehentai.conf import CATS


def keyword(
    f_search: str = None,
    f_cats: int = None,
    advsearch: bool = None,
    f_sh: bool = None,
    f_sto: bool = None,
    f_spf: int = None,
    f_spt: int = None,
    f_srdd: int = None,
    f_sfl: bool = None,
    f_sfu: bool = None,
    f_sft: bool = None,
):

    return {
        # search_kw
        "f_search":f_search,
        # category
        "f_cats":f_cats,
        # advanced search
        # show advanced options
        "advsearch":1 if advsearch or f_sh or f_sto or f_spf or f_spt or f_srdd or f_sfl or f_sfu or f_sft else None,
        # show expunged galleries
        "f_sh":"on" if f_sh else None,
        # require Gallery torrent
        "f_sto":"on" if f_sto else None,
        # between {f_spf} and {f_spt} Pages
        "f_spf":f_spf,
        "f_spt":f_spt,
        # minimum_rating
        "f_srdd":f_srdd,
        # disable filter language
        "f_sfl":"on" if f_sfl else None,
        # disable filter uploader
        "f_sfu":"on" if f_sfu else None,
        # disable filter tags
        "f_sft":"on" if f_sft else None,
    }


def next_view(sp: BeautifulSoup):
    return sp.find('table',class_="ptt").find_all('td')[-1].find('a')

# url:target_URL
# parms:search_keyword
def get_sp(url: str,params=None,encoding=None):
    # set encoding
    respone=requests.get(url,headers=headers,params=params)
    if encoding:
        respone.encoding=encoding
    else:
        encoding=chardet.detect(respone.content)["encoding"]
        respone.encoding=encoding

    return BeautifulSoup(respone.text,"lxml")


# switch categories: doujinshi...
def get_f_cats(cat_code=0b0011111111,cats: list=None):
    res=0b1111111111
    if cats:
        for v in list(i.value for i in cats):
            res&=v
        return res
    
    for v in list(i.value for i in CATS):
        if cat_code&1:res&=v
        cat_code>>=1
    return res


URL="https://e-hentai.org/"

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Referer":"http://www.google.com",
}