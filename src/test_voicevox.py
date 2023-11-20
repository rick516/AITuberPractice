from voicevox_adapter import VoicevoxAdapter
from play_sound import PlaySound

input_text = input("入力してつかあさい: ")
voicevox_adapter = VoicevoxAdapter()
play_sound = PlaySound("スピーカー")
data, rate = voicevox_adapter.get_voice(input_text)
play_sound.play_sound(data, rate)
