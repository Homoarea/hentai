# ehentai
[中文](./README.md)|[English](./README_en.md)   
这是一个爬取 e-hentai.org 的命令行程序

## 使用
### 命令行
```
pip install ehentai
eh --help
```
### 在 python 脚本中
```
import ehentai
page=ehentai.get_popular()
for gl in page.gl_table:
    print(gl)
```

## TODO
- [ ] 爬取 torrent 种子
- [ ] 爬取排行榜
- [ ] 登陆系统(Cookie)
- [x] SNI
- [ ] 检查下载文件
- [ ] 多线程爬取
- [ ] 更多文件打包格式(便于分享)
  

## 感谢
[curl_cffi](https://github.com/lexiforest/curl_cffi/)     
[click](https://github.com/pallets/click)       
[bs4](https://pypi.org/project/beautifulsoup4/)     