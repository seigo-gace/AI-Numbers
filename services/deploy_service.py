import os
import subprocess

BASE_DIR = "repos"

def deploy_project(name: str) -> str:
    """指定リポジトリの main.py を実行してデプロイ"""
    path = os.path.join(BASE_DIR, name)
    file_path = os.path.join(path, "main.py")

    if not os.path.exists(file_path):
        return f"Deploy failed: {file_path} not found"

    try:
        subprocess.run(["python", file_path], check=True)
        return "Deployed successfully"
    except Exception as e:
        return f"Deploy failed: {str(e)}"
