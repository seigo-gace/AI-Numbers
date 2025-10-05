import openai

# OpenAI APIキーを設定（環境変数から読み込むのが安全）
openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_code(prompt: str) -> str:
    """ユーザーの指示からコードを生成する関数"""
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Generate Python code for: {prompt}",
        max_tokens=300
    )
    return response.choices[0].text.strip()
