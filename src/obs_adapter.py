import obsws_python as obs
import os
from dotenv import load_dotenv

class OBSAdapter: 
    def __init__(self) -> None:
        load_dotenv()
        password = os.getenv("OBS_WS_PASSWORD")
        host = os.getenv("OBS_WS_HOST")
        port = os.getenv("OBS_WS_PORT")
        if (password == None or host == None or port == None):
            raise Exception("OBSの設定がされていません。")
        self.ws = obs.ReqClient(host=host, port=port, password=password)

    def set_question(self, text: str):
        self.ws.set_input_settings(name="Question", settings={"text": text}, overlay=True)

    def set_answer(self, text: str):
        self.ws.set_input_settings(name="Answer", settings={"text": text}, overlay=True)


if __name__ == "__main__":
    obs = OBSAdapter()
    question = input("質問を入力してください: ")
    obs.set_question(question)
    answer = input("回答を入力してください: ")
    obs.set_answer(answer)
