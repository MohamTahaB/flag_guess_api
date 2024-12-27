from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, List
from session.session import Session
from pydantic import BaseModel


class render_response(BaseModel):
    render: str
    resemblance: float
    prior_guesses: List[str]


class session_id_response(BaseModel):
    id: str


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)


SESSION_DICT: Dict[str, Session] = dict()


@app.get("/")
async def root():
    return {"message": "all good !"}


@app.post("/session", response_model=session_id_response)
async def start_session():
    session: Session = Session()
    SESSION_DICT[session.id] = session
    return session_id_response(id=SESSION_DICT[session.id].id)


@app.put("/session", response_model=render_response)
async def update_session(session_id: str, country: str) -> render_response:
    if session_id not in SESSION_DICT:
        raise HTTPException(status_code=404, detail="id not found")

    SESSION_DICT[session_id].add_guess(country)
    return render_response(render=SESSION_DICT[session_id].render_base64, resemblance=SESSION_DICT[session_id].resemblance, prior_guesses=SESSION_DICT[session_id].flag.prior_guesses)


@app.delete("/session")
async def delete_session(session_id: str):
    try:
        SESSION_DICT.pop(session_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="id not found")
