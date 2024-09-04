from fastapi import FastAPI, Response
import base64
from random import randint, shuffle
import random
from requests import get
from urllib import parse

def moistr():
    url1 = "https://moistr.freenods.sbs/sub?host=tun.sub.jokerin.icu&uuid=1f263db4-31e0-4a91-9eeb-6c89d8bbadf5&path=/?proxyip=proxyip.oracle.fxxk.dedyn.io"
    rep = get(url1)
    if rep.status_code == 200:
        # print(rep.text)

        node= base64.b64decode(rep.text)
        node_str = str(node, 'utf-8')
        node_str_decode = parse.unquote(node_str)
        list_node = node_str_decode.split('\n')
        last_node  = "this is a test text,don't delete!!!"
        new_node_list = []
        for i in list_node:
            now_node = i
            if now_node[-20:] == last_node[-20:]:
                now_node = now_node + str(random.randint(1,500))
            new_node_list.append(now_node)
            last_node = i
        if new_node_list:
            return "\n".join(new_node_list)
app = FastAPI()
IP_TANK = {
    "hk": "HK.txt",
    "jp": "JP.txt",
    "us": "US.txt",
    "cf": "CF_SITE.txt",
}


def ip_get(region):
    with open(f"IP_DATA/{IP_TANK[region]}", "r", encoding="utf-8") as f:
        ips = f.read().split("\n")
        shuffle(ips)
        return ips[-10:]


def get_text():
    node_tank = []
    for each in ip_get('hk'):
        simple_node = f"vless://1f263db4-31e0-4a91-9eeb-6c89d8bbadf5@{each}:443?encryption=none&security=tls&sni=tun.sub.jokerin.icu&fp=random&type=ws&host=tun.sub.jokerin.icu&path=%2F#CF-香港-{randint(1, 500)}"
        node_tank.append(simple_node)
    for each in ip_get('jp'):
        simple_node = f"vless://1f263db4-31e0-4a91-9eeb-6c89d8bbadf5@{each}:443?encryption=none&security=tls&sni=tun.sub.jokerin.icu&fp=random&type=ws&host=tun.sub.jokerin.icu&path=%2F#CF-日本-{randint(1, 500)}"
        node_tank.append(simple_node)
    for each in ip_get('us'):
        simple_node = f"vless://1f263db4-31e0-4a91-9eeb-6c89d8bbadf5@{each}:443?encryption=none&security=tls&sni=tun.sub.jokerin.icu&fp=random&type=ws&host=tun.sub.jokerin.icu&path=%2F#CF-美国-{randint(1, 500)}"
        node_tank.append(simple_node)
    for each in ip_get('cf'):
        simple_node = f"vless://1f263db4-31e0-4a91-9eeb-6c89d8bbadf5@{each}:443?encryption=none&security=tls&sni=tun.sub.jokerin.icu&fp=random&type=ws&host=tun.sub.jokerin.icu&path=%2F#CF-油管专用-{randint(1, 500)}"
        node_tank.append(simple_node)
    node_txt = "\n".join(node_tank)

    return node_txt



@app.get("/get_node_text")
def send_text():
    text_bytes = base64.b64encode((get_text()+moistr()).encode("utf-8"))
    response = Response(content=text_bytes, media_type="application/octet-stream")
    # response.headers["Content-Disposition"] = "inline"
    response.headers["Content-Type"] = "text/plain; charset=utf-8"
    return response


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8000)
    # print(base64.b64encode(get_text().encode("utf-8")).decode("utf-8"))
