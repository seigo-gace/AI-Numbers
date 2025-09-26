import os
from git import Repo

# プロジェクト用の保存先ディレクトリ
BASE_DIR = "repos"

def init_repo(name: str) -> str:
    """指定された名前で新しいリポジトリを作成"""
    path = os.path.join(BASE_DIR, name)
    os.makedirs(path, exist_ok=True)
    if not os.path.exists(os.path.join(path, ".git")):
        Repo.init(path)
    return path

def commit_code(name: str, code: str, message: str):
    """指定リポジトリにコードを保存してコミット"""
    path = os.path.join(BASE_DIR, name)
    os.makedirs(path, exist_ok=True)
    file_path = os.path.join(path, "main.py")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)
    repo = Repo(path)
    repo.git.add(all=True)
    repo.index.commit(message)
    return repo.head.commit.hexsha
