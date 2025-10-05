from fastapi import FastAPI
from services.ai_service import generate_code
from services.git_service import init_repo, commit_code
from services.deploy_service import deploy_project

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Dev-AI API is running"}

@app.post("/chat")
def chat(prompt: str):
    code = generate_code(prompt)
    return {"generated_code": code}

@app.post("/repo/init")
def repo_init(name: str):
    path = init_repo(name)
    return {"repo_path": path}

@app.post("/repo/commit")
def repo_commit(name: str, code: str, message: str = "AI commit"):
    commit_hash = commit_code(name, code, message)
    return {"commit": commit_hash}

@app.post("/deploy")
def deploy(name: str):
    status = deploy_project(name)
    return {"deploy_status": status}
