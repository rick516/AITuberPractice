import requests
import json
import io
import soundfile

class VoivevoxAdapter:
    def __init__(self, url: str = "http://localhost:50021/") -> None:
        self.url = url
        
    def __create_audio_query(self, text: str, speaker_id: int) -> json:
        item_data = {
            "text": text,
 		    "speaker": speaker_id,
        }
        res = requests.post(self.url + "audio_query", params=item_data)
        return res.json()
    
    def __create_audio(self, query_data: json, speaker_id: int) -> bytes:
        audio_params = {
            "speaker": speaker_id
        }
        headers = {
            "accept": "audio/wav", 
            "Content-Type": "application/json"
        }
        res = requests.post(self.url + "synthesis", params=audio_params, data=json.dumps(query_data), headers=headers)
        print("status_code:" + str(res.status_code))
        return res.content

    def get_voice(self, text: str, speaker_id: int):
        query_data = self.__create_audio_query(text, speaker_id)
        audio_bytes = self.__create_audio(query_data=query_data, speaker_id=speaker_id)
        audio_stream = io.BytesIO(audio_bytes)
        data, sample_rate = soundfile.read(audio_stream)
        return data, sample_rate
    

if __name__ == "__main__":
    voicevox = VoivevoxAdapter()
    text = input("テキストを入力してください: ")
    data, sample_rate = voicevox.get_voice(text=text, speaker_id=14)
    print(sample_rate)
