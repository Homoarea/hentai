# ehentai
this is a simple cli for view e-hentai.org

## Quickstart
### use cli
```
pip install ehentai

eh --help
```
### python code
```
import ehentai
page=ehentai.get_popular()
for gl in page.gl_table:
    print(gl)
```

## TODO
- [ ] fetch torrent
- [ ] login
- [x] SNI
- [ ] multi-threaded download
- [ ] More file packaging formats
  

## Using
[curl_cffi](https://github.com/lexiforest/curl_cffi/)     
[click](https://github.com/pallets/click)       
[bs4](https://pypi.org/project/beautifulsoup4/)     