from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/{something}")
def hello_world(something: str, response: Response, status_code=200):
    if "aa" in something:
        response.status_code = 400
    else:
        return {"Hello": "World"}
