# get_domain_ip

>这个脚本主要是用来查询(单或多)域名解析

## 1.环境

- windows/linux
- python >= 3.7

## 2.安装

```
git clone https://github.com/1derian/get_domain_ip.git
cd get_domain_ip
pip3 install -r requirements.txt
```

## 3.使用

**查看帮助**

```python
D:\project\get_domain_ip>python3 get_domain_ip.py -h

                         _                       _
                      __| | ___  _ __ ___   __ _(_)_ __     __ _ _   _  ___ _ __ _   _
                     / _` |/ _ \| '_ ` _ \ / _` | | '_ \   / _` | | | |/ _ \ '__| | | |
                    | (_| | (_) | | | | | | (_| | | | | | | (_| | |_| |  __/ |  | |_| |
                     \__,_|\___/|_| |_| |_|\__,_|_|_| |_|  \__, |\__,_|\___|_|   \__, |
                                                              |_|                |___/
                                                                        version: 0.0.1
                                                                        author : mhx

usage: get_domain_ip.py [-h] [-d DOMAIN [DOMAIN ...]] [-df DOMAIN_FILE] [-o OUTPUT]

This is a good domain resolution tool

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN [DOMAIN ...], --domain DOMAIN [DOMAIN ...]
                        Query single or multiple domain name resolution.
  -df DOMAIN_FILE, --domain_file DOMAIN_FILE
                        Query multiple domain name resolutions as files.
  -o OUTPUT, --output OUTPUT
                        Domain name resolutions save in file.

example:
        python3 get_domain_ip -d www.baidu.com
```

**获取单个域名的解析**

```
python3 get_domain_ip.py -d www.baidu.com
```

![image-20221017103808254](https://i0.hdslb.com/bfs/album/9c15d93642c1a77d4b4c209f6852c9a876894447.png)

**获取多个域名的解析**

``` py
python3 get_domain_ip.py -d www.baidu.com www.mi.com
```

![image-20221017103646670](https://i0.hdslb.com/bfs/album/9422d9c5e5e568a62b64134644ff8105f4e0793e.png)

**从文件读取域名列表进行域名解析查询并保存到指定文件**

默认保存在 result.txt 

```
python3 get_domain_ip.py -df domain.txt -o res.txt
```

![image-20221017104640265](https://i0.hdslb.com/bfs/album/28c5c360259b2a3f637d01dbe2edb1838daac3aa.png)

## 4.免责声明🧐

本工具仅面向合法授权的企业安全建设行为，如您需要测试本工具的可用性，请自行搭建测试环境。

在使用本工具进行检测时，您应确保该行为符合当地的法律法规，并且已经取得了足够的授权。请勿对非授权目标进行扫描。

如您在使用本工具的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。
