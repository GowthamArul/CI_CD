import uvicorn
import warnings

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware


warnings.filterwarnings("ignore", category=DeprecationWarning)

app = FastAPI()


app = FastAPI(
    title='Patient Data Management',
    description="The PDM application will help maintain patients' historical medication records and allow doctors to chat with an LLM model to gain insights about the drugs.",
    version= "1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    """
    Welcome message on the application startup
    """
    return {"Welcome to the Chatbot Application": "This application allows you to chat with an LLM model and maintain patient data."}




if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)