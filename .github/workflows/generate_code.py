import os
import google.generativeai as genai

# GitHub Secretsから読み込んだAPIキーを使ってGeminiを使えるようにする
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# モデルを指定（現時点では gemini-pro）
model = genai.GenerativeModel("gemini-pro")

# 指示内容：FizzBuzzを書いて
prompt = "PythonでFizzBuzzを出力するコードを書いてください"

# 指示を送信し、応答を受け取る
response = model.generate_content(prompt)

# 結果を表示する
print(response.text)
