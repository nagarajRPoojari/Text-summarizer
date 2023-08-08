from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse

from textSummarizer.pipeline.prediction import PredictionPipeline

app = FastAPI()
predictor = PredictionPipeline()

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload/")
async def upload_text(data: dict):
    try:
        
        pdf_text = data.get("text", "")
        print(pdf_text)
        summary = predictor.predict(pdf_text)
        print(summary)
        
        # Process the extracted text as needed
        
        return  JSONResponse(content={"message": summary})
    except Exception as e:
        return JSONResponse(content={"message": "An error occurred"}, status_code=500)






@app.post("/")
async def process_chat(request: Request, data: dict):
    name = data.get("name")
    if name is not None:
        # Perform any processing or summarization on the name
        summary = predictor.predict(name)
        return JSONResponse(content={"chat_summary": summary})
    else:
        return JSONResponse(content={"chat_summary": "Invalid data"}, status_code=400)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
