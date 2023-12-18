from fastapi import FastAPI, HTTPException
import requests
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/send_prompt/")
async def send_prompt(body: dict):
    try:
        response = requests.post(
            url = "http://194.233.83.197:5892/generate_response",
            json= {
                "prompt": body['prompt'],
            }
        )
        return {"message": response.json()}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    uvicorn.run()
    pass