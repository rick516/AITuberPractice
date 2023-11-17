# 依存関係をimport
import os
import openai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# openaiのアダプタークラスを作成
class OpenAIAdapter:
    def __init__(self):
        with open("src/assets/system_prompt.txt", "r", encoding="utf-8") as f:
            self.system_prompt = f.read()
            
    # メッセージ作成
    def _create_message(self, role, message):
        if role not in ["system", "user"]:
            raise ValueError("Invalid role")
        return {
            "role": role,
            "content": message
        }
    
    # チャットの作成
    def _create_chat(self, question):
        if not question:
            raise ValueError("Question must not be empty")
        system_message = self._create_message("system", self.system_prompt)
        user_message = self._create_message("user", question)
        
        messages = [system_message, user_message]
        
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return res.choices[0].message.content

def main():
    adapter = OpenAIAdapter()
    res = adapter._create_chat(input("コメント:"))
    print(res)

# もし直接実行された実行する
if __name__ == "__main__":
		main()