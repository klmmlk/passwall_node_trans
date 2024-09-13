from fastapi import FastAPI,Response
import base64
app = FastAPI()


def get_text(web, tun, moistr,dongtai):
    if web:
        with open("data/web.txt", "r") as file:
            web_text = file.read().rstrip("\n")
    else:
        web_text = ""
    if tun:
        with open("data/tun.txt", "r") as file:
            tun_text = file.read().rstrip("\n")
    else:
        tun_text = ""
    if moistr:
        with open("data/moistr.txt", "r") as file:
            moistr_text = file.read().rstrip("\n")
    else:
        moistr_text = ""
    if dongtai:
        with open("data/dongtai.txt", "r") as file:
            dongtai_text = file.read().rstrip("\n")
    else:
        dongtai_text = ""
    return web_text + tun_text + moistr_text + dongtai_text



@app.get("/get_node_text")
def send_text(web: bool = False, tun: bool = False, moistr: bool = False, dongtai: bool = False):
    return Response(base64.b64encode(get_text(web, tun, moistr, dongtai).encode("utf-8")),media_type="text/plain")


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8000)
