from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from agent import run_agent, clear_memory, close_agent


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await close_agent()


app = FastAPI(
    title="MCP Travel Agent",
    description="AI Travel Agent powered by Playwright MCP and Groq",
    version="1.0.0",
    lifespan=lifespan,
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
async def root():
    return {
        "status": "online",
        "service": "MCP Travel Agent"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }


@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = await run_agent(request.message)

        return {
            "response": response
        }

    except Exception as e:
        import traceback

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.post("/clear")
async def clear():
    try:
        await clear_memory()

        return {
            "status": "memory cleared"
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )