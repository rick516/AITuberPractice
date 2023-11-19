import requests
import json

url = "http://localhost:50021/"
text = "こんにちは"
speaker_id = 14

item_data = {
    "text": text,
		"speaker": speaker_id
}

res = requests.post(url + 'audio_query', params=item_data)

res_json = res.json()
query_data = res_json
print(query_data)

a_params = {
    "speaker": speaker_id,
}

res = requests.post(url + 'synthesis', params=a_params, data=json.dumps(query_data))

print(res.content)
