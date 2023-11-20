import sounddevice as sd
from typing import TypedDict

class PlaySound:
    def __init__(self, input_device_id: int = 0, output_device_name: str = "MacBook Proのスピーカー") -> None:
        # インプットは今回使わないのでデフォルト0
        self.input_device_id = input_device_id
        self.output_device_id = self._search_output_device_id(output_device_name)
        # デフォルトデバイスの設定
        sd.default.device = [self.input_device_id, self.output_device_id]

    # デバイスIDの検索
    def _search_output_device_id(self, output_device_name: str, output_device_host_api: int = 0) -> int:
        output_devices = sd.query_devices()
        output_device_id = None
        for device in output_devices:
            is_output_device_name = device["name"] == output_device_name
            is_output_device_host_api = device["hostapi"] == output_device_host_api
            if is_output_device_name and is_output_device_host_api:
                output_device_id = device["index"]
                break
        
        if output_device_id is None:
            print("デバイスが見つかりませんでした。")
            exit()

        return output_device_id
            
    # 音声を再生
    def play_sound(self, data, rate) -> bool:
        sd.play(data, rate)
        # 終了まで待つ
        sd.wait()
        return True