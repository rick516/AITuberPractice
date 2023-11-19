import sounddevice as sd

f = open("list_souddevice.txt", "w", encoding="utf-8")
f.write(str(sd.query_devices()))
f.close()