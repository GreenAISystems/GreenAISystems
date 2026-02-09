from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Green AI Systems API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # plus simple au début
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "API FastAPI opérationnelle 🚀"}

@app.get("/health")
def health():
    return {"ok": True}