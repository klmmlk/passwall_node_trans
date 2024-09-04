# *- coding: utf-8 -*-
import base64
import json
import os
import random
import re
import logging
from urllib import parse

from bs4 import BeautifulSoup
from requests import get
from apscheduler.schedulers.blocking import BlockingScheduler

logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


def moistr():
    url1 = "https://moistr.freenods.sbs/sub?host=tun.sub.jokerin.icu&uuid=1f263db4-31e0-4a91-9eeb-6c89d8bbadf5&path=/?proxyip=proxyip.oracle.fxxk.dedyn.io"
    rep = get(url1)
    if rep.status_code == 200:
        # print(rep.text)

        node = base64.b64decode(rep.text)
        node_str = str(node, 'utf-8')
        node_str_decode = parse.unquote(node_str)
        list_node = node_str_decode.split('\n')
        last_node = "this is a test text,don't delete!!!"
        new_node_list = []
        for i in list_node:
            now_node = i
            if now_node[-20:] == last_node[-20:]:
                now_node = now_node + str(random.randint(1, 500))
            new_node_list.append(now_node)
            last_node = i
        if new_node_list:
            write_data("\n".join(new_node_list))


def gen_config(node_type, data):
    if node_type == 'hysteria2':
        try:
            if ',' in data['server']:
                server = data['server'].split(',')[0].split(':')[0]
                port = data['server'].split(',')[1].split('-')
                config = f'hysteria2://{data["auth"]}@{server}:{random.randint(int(port[0]), int(port[1]))}/?insecure={1 if data["tls"]["insecure"] else 0}&sni={data["tls"]["sni"]}#动态hy{random.randint(1, 10000)}'
            else:
                server = data['server']
                config = f'hysteria2://{data["auth"]}@{server}/?insecure={1 if data["tls"]["insecure"] else 0}&sni={data["tls"]["sni"]}#动态hy{random.randint(1, 10000)}'
        except Exception as e:
            logging.error(f'生成hysteria2配置失败: {e}')
            return
        else:
            write_data(config)


def write_data(text):
    _path = os.path.join(os.path.dirname(__file__), 'data.txt')
    with open(_path, 'a', encoding='utf-8') as f:
        f.write(text)
        f.write('\n')


def from_dongtai():
    logging.info("from_dongtai函数开始执行")
    url_list = [
        {"url": 'https://gitlab.com/free9999/ipupdate/-/raw/master/hysteria2/config.json', "type": 'hysteria2'},
        {"url": 'https://fastly.jsdelivr.net/gh/Alvin9999/pac2@latest/hysteria2/config.json', "type": 'hysteria2'},
        {"url": 'https://gitlab.com/free9999/ipupdate/-/raw/master/hysteria/2/config.json', "type": 'hysteria2'},
        {"url": 'https://fastly.jsdelivr.net/gh/Alvin9999/pac2@latest/hysteria/2/config.json', "type": 'hysteria2'},
    ]
    for each_url in url_list:
        response = get(each_url['url'])
        if response.status_code == 200:
            req_data = response.json()
        else:
            print('Error:', response.status_code)
            continue
        gen_config(each_url['type'], req_data)


def from_web():
    logging.info("from_web函数开始执行")
    url = 'https://banyunxiaoxi.icu/category/vpn%e8%8a%82%e7%82%b9/'
    UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    headers = {'User-Agent': UA}
    req_data = get(url, headers=headers)
    if req_data.status_code == 200:
        soup = BeautifulSoup(req_data.text, 'lxml')
        pass
        # 获取第一个class为"bookmark-item"的a标签的href属性值
        new_url = soup.select_one('.bookmark-item')['href']
        # 访问新链接
        req_data = get(new_url, headers=headers)
        if req_data.status_code == 200:
            soup = BeautifulSoup(req_data.text, 'lxml')
            node_text = soup.select_one('.content blockquote p').text
            node_list = node_text.split('\n')
            for index, node in enumerate(node_list):
                if 'vmess://' in node:
                    line = node.split('vmess://')[1]
                    decode_line = base64.b64decode(line).decode('utf-8')
                    line_json = eval(decode_line)
                    line_json['ps'] = re.search(r"[A-Z]{2}_\d{2,3}", line_json['ps']).group()
                    node_list[index] = (
                            'vmess://' + base64.b64encode(str(json.dumps(line_json)).encode('utf-8')).decode(
                        'utf-8'))

            # 将node_text追加写入到data.txt中
            node_srt = '\n'.join(node_list)
            write_data(node_srt)
    else:
        from_web()


def main():
    logging.info('main函数开始执行')
    # 将data.txt文件内容清空
    with open('data.txt', 'w', encoding='utf-8') as f:
        f.write('')
    from_dongtai()
    from_web()
    moistr()


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(main, 'interval', hours=4)
    scheduler.start()
