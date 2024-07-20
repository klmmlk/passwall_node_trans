# *- coding: utf-8 -*-
import random
from bs4 import BeautifulSoup
from requests import get


def gen_config(node_type, data):
    if node_type == 'hysteria2':
        if ',' in data['server']:
            server = data['server'].split(',')[0].split(':')[0]
            port = data['server'].split(',')[1].split('-')
            config = f'hysteria2://{data["auth"]}@{server}:{random.randint(int(port[0]), int(port[1]))}/?insecure={1 if data["tls"]["insecure"] else 0}&sni={data["tls"]["sni"]}#动态hy{random.randint(1,10000)}'
            write_data(config)
def write_data(text):
    with open('data.txt', 'a', encoding='utf-8') as f:
        f.write(text)
        f.write('\n')


def from_dongtai():
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
            # 将node_text追加写入到data.txt中
            write_data(node_text)


def main():
    # 将data.txt文件内容清空
    with open('data.txt', 'w', encoding='utf-8') as f:
        f.write('')
    from_dongtai()
    from_web()




# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    main()
