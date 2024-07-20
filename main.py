from fastapi import FastAPI

app = FastAPI()

def get_text():
    with open("data.txt", "r") as file:
        return file.read().rstrip("\n")
@app.get("/")
def send_text():
    return get_text()




if __name__ == '__main__':

    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)