import os
from dotenv import load_dotenv
from youtube_comment_adapter import YoutubeCommentAdapter
from openai_adapter import OpenAIAdapter
from voicevox_adapter import VoivevoxAdapter
from obs_adapter import OBSAdapter
from play_sound_adapter import PlaySoundAdapter
load_dotenv()

class AITuberSystem:
    def __init__(self):
        self.video_id = os.getenv("LIVE_VIDEO_ID")
        self.youtube_adapter = YoutubeCommentAdapter(self.video_id)
        self.openai_adapter = OpenAIAdapter()
        self.voicevox_adapter = VoivevoxAdapter()
        self.obs_adapter = OBSAdapter()
        self.play_sound_adapter = PlaySoundAdapter(output_device_name="VB-Cable")
        pass
    
    def talk_with_comment(self) -> bool:
        print("コメントを取得中です..")
        
        # Youtube最新コメントを取得する
        recent_comment = self.youtube_adapter.get_comment()
        
        if recent_comment is None:
          self.obs_adapter.set_text_source("Status", "コメントしてね！")
          return False

        # obsに「アヤナイちゃんは考え中...」と表示する
        self.obs_adapter.set_text_source("Status", "アヤナイちゃんは考え中...")

        # gptに引き渡して回答テキストを生成する
        answer_text = self.openai_adapter._create_chat(recent_comment)

        # 回答テキストで音声合成を行う
        data, rate = self.voicevox_adapter.get_voice(text=answer_text, speaker_id=14)

        # obsのキャプチャに反映する
        self.obs_adapter.set_text_source("Question", recent_comment)
        self.obs_adapter.set_text_source("Answer", answer_text)
        # 音声を再生する
        self.play_sound_adapter.play_sound(data, rate)
        # obsのステータスをクリアする
        self.obs_adapter.set_text_source("Status", "")
        return True

