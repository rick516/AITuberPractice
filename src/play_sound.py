import sounddevice as sd
from typing import TypedDict

class PlaySound:
    def __init__(self, input_device_id: int = 0, output_device_name: str = "功一郎のAirPods Pro", output_device_host_api: int = 0) -> None:
        # インプットは今回使わないのでデフォルト0
        self.input_device_id = input_device_id
        self.output_device_name = output_device_name
        self.output_device_host_api = output_device_host_api
        self.output_device_id = self.__search_output_device_id(self.output_device_name, self.output_device_host_api)
        # デフォルトデバイスの設定
        sd.default.device = [self.input_device_id, self.output_device_id]

    # デバイスIDの検索
    def __search_output_device_id(self, output_device_name: str, output_device_host_api: int) -> int:
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

        return output_device_id

    # 音声を再生
    def play_sound(self, data, rate) -> bool:
        sd.play(data=data, samplerate=rate)
        # 終了まで待つ
        sd.wait()
        return True