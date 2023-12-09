from openai_adapter import OpenAIAdapter
from voicevox_adapter import VoivevoxAdapter
from play_sound import PlaySound
import sounddevice as sd
import inquirer


openai_adapter = OpenAIAdapter()
answer_text = openai_adapter._create_chat(input("話かけてみてね:"))
voicevox = VoivevoxAdapter()

devices = sd.query_devices()
device_names = [device["name"] for device in devices]
questions = [inquirer.List(name="device", message="出力デバイスを選択してください", choices=device_names)]
answers = inquirer.prompt(questions)
output_device = answers["device"]
playsound = PlaySound(output_device_name=output_device, output_device_host_api=0)
data, rate = voicevox.get_voice(text=answer_text, speaker_id=14)
playsound.play_sound(data, rate)
