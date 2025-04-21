# ehentai
[中文](./README.md)|[English](./README_en.md)   
this is a simple cli for view e-hentai.org

## Usage
### with cli
```
pip install ehentai

eh --help
```
### with python code
```
import ehentai
page=ehentai.get_popular()
for gl in page.gl_table:
    print(gl)
```

## TODO
- [ ] fetch torrent
- [ ] fetch top list
- [ ] login
- [x] SNI
- [ ] check download
- [ ] multi-threaded download
- [ ] More file packaging formats
  

## Thanks
[curl_cffi](https://github.com/lexiforest/curl_cffi/)     
[click](https://github.com/pallets/click)       
[bs4](https://pypi.org/project/beautifulsoup4/)     