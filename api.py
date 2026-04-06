from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator

from src.crew import run_post_generator
from src.chains.profile_chain import run_profile_analyzer
from src.chains.repurpose_chain import run_repurpose

app = FastAPI(
    title="LinkedIn AI Copilot",
    description="API para geração e otimização de conteúdo para o LinkedIn",
    version="1.0.0"
)

# ──────────────────────────────────────────
# Models
# ──────────────────────────────────────────
class PostRequest(BaseModel):
    topic: str
    tone: str

    @field_validator("tone")
    def validate_tone(cls, value):
        allowed_tones = ["educativo", "storytelling", "técnico"]
        if value.lower() not in allowed_tones:
            raise ValueError(f"Tom deve ser um dos seguintes: {', '.join(allowed_tones)}")
        return value.lower()


class ProfileRequest(BaseModel):
    profile_text: str


class RepurposeRequest(BaseModel):
    readme_text: str
    tone: str

    @field_validator("tone")
    def validate_tone(cls, value):
        allowed_tones = ["educativo", "storytelling", "técnico"]
        if value.lower() not in allowed_tones:
            raise ValueError(f"Tom deve ser um dos seguintes: {', '.join(allowed_tones)}")
        return value.lower()


# ──────────────────────────────────────────
# Routes
# ──────────────────────────────────────────
@app.get("/health")
async def health():
    return {"status": "ok", "version": "1.0.0"}


@app.post("/generate-post")
async def generate_post(request: PostRequest):
    try:
        result = run_post_generator(topic=request.topic, tone=request.tone)
        return {"post": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/analyze-profile")
async def analyze_profile(request: ProfileRequest):
    try:
        result = run_profile_analyzer(profile_text=request.profile_text)
        return {"analysis": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/repurpose-readme")
async def repurpose_readme(request: RepurposeRequest):
    try:
        result = run_repurpose(readme_text=request.readme_text, tone=request.tone)
        return {"post": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))