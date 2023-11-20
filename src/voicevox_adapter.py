import requests
import json
import io
import soundfile as sf

class VoicevoxAdapter:
  URL = 'http://127.0.0.1:50021/'
  def __init__(self) -> None:
    pass
  
  def __create_audio_query(self, text: str, speaker_id: int) -> json:
    """
    音声合成のリクエストデータを作成する
    Parameters
    ----------
    text : str
				音声合成するテキスト
		speaker_id : int
				話者ID
		
    Returns
    -------
    json
				音声合成のリクエストデータ
    """
    
    item_data={
      "text": text,
			"speaker": speaker_id
		}
    response = requests.post(self.URL + 'audio_query', params=item_data)
    return response.json()
  
  def __create_request_audio(self, query_data, speaker_id: int) -> bytes:
    """
    音声合成をリクエストする
    Parameters
    ----------
    query_data : json
				音声合成のリクエストデータ
		speaker_id : int
				話者ID
		Returns
		-------
		bytes
				音声データ (wav) のバイナリ
		"""
    
    a_params = {
      "speaker": speaker_id,
		}
    headers = {
      "accept": "audio/wav", "Content-Type": "application/json",
		}
    
    res = requests.post(
        self.URL + 'synthesis',
        params=a_params,
        data=json.dumps(query_data),
        headers=headers
			)
    print(res.status_code)
    return res.content
      
  def get_voice(self, text: str, speaker_id: int = 14) -> bytes:
      """
		音声を出力する
		Parameters
		----------
		text : str
				音声合成するテキスト
		speaker_id : int, optional
				話者ID, by default 14
		Returns
		-------
		bytes
				音声データ (wav) のバイナリ + サンプリングレート（録音精度の指標）
		"""
      speaker_id = speaker_id
      query_data = self.__create_audio_query(text=text, speaker_id=speaker_id)
      audio_bytes = self.__create_request_audio(query_data=query_data, speaker_id=speaker_id)
      audio_stream = io.BytesIO(audio_bytes)
      data, sample_rate = sf.read(audio_stream)
      return data, sample_rate
  
if __name__ == "__main__":
    voicevox = VoicevoxAdapter()
    data, sample_rate = voicevox.get_voice("こんにちは")
    print(sample_rate)
