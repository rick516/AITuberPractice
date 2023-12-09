import sounddevice as sd

with open("src/assets/list_souddevice.txt", "w", encoding="utf-8") as f:
    f.write(str(sd.query_devices()))
