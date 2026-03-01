from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
import json
import time
from app.config import Settings

router = APIRouter(prefix="/behavior", tags=["behavior"])
settings = Settings()

# Multi-provider Logic
def get_llm():
    from openai import AsyncOpenAI
    if settings.ollama_base_url:
        print(f"[BEHAVIOR] Using Ollama at {settings.ollama_base_url}")
        return AsyncOpenAI(
            api_key="ollama", 
            base_url=settings.ollama_base_url
        ), settings.ollama_model
    elif settings.perplexity_api_key:
        return AsyncOpenAI(
            api_key=settings.perplexity_api_key,
            base_url="https://api.perplexity.ai"
        ), "sonar"
    else:
        return AsyncOpenAI(
            api_key=settings.openai_api_key,
            base_url=settings.llm_base_url
        ), "gpt-4o-mini"

class BehaviorLog(BaseModel):
    site_id: str
    type: str # hover, scroll, click
    metadata: str
    url: str

@router.post("/analyze")
async def analyze_behavior(log: BehaviorLog):
    """
    Analyzes user behavior and returns a natural language commentary.
    """
    req_start = time.time()
    print(f"[BEHAVIOR] Request received. Analyzing: {log.type} - {log.metadata}")
    
    llm, model_name = get_llm()
    print(f"[BEHAVIOR] Using model: {model_name}")
    
    prompt = f"""
    You are a calm, human-friendly guide on a website. Your role is to gently reflect what is visible on the page, without judging or narrating the person's actions.
    
    ACTION: {log.type}
    CONTENT: {log.metadata}
    URL: {log.url}
    
    TONE RULES:
    1. Reflect only what is visible in the present moment (e.g., "Viewing mortgage plans.").
    2. NEVER talk ABOUT the person (Do NOT say "The user is...", "You seem...", "We detected...").
    3. NEVER describe system actions (Do NOT say "Analyzing...", "Processing...").
    4. DO NOT assume intent or emotions (Do NOT say "Trying to decide", "Confused").
    5. Use short, neutral, human statements.
    6. FORBIDDEN PHRASES: "the user is", "we detected", "analyzing", "intent", "struggling", "trying to decide".
    
    Return ONLY a raw JSON object (no markdown): {{"commentary": "..."}}
    """
    
    start_time = time.time()
    try:
        # LLM Logic - No strict timeout here, letting the remote LLM take its time
        print(f"[BEHAVIOR] Calling remote LLM...")
        
        response = await llm.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"} if "sonar" not in model_name and "llama" not in model_name.lower() else None
        )
        
        duration = time.time() - start_time
        print(f"[BEHAVIOR] LLM responded in {duration:.2f}s")
        content = response.choices[0].message.content
        
        # Cleanup content
        content = content.replace("```json", "").replace("```", "").strip()

        data = json.loads(content)
        return data
    except Exception as e:
        duration = time.time() - start_time
        print(f"[BEHAVIOR] LLM Call Failed after {duration:.2f}s: {e}")
        # Always return a generic dynamic-looking message instead of nothing, 
        # but keep it neutral to see it's trying.
        return {"commentary": "Reflecting on your journey..."}
