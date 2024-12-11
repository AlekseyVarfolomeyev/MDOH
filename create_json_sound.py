import json
from pydub import AudioSegment
sound = AudioSegment.from_file("audio_record.mp3", format="mp3")
full_t=len(sound) # full time of audio in ms
delta_t=10
json_sound=list()
for i in range(0, full_t, delta_t):
	json_sound.append([i, sound[i:i+delta_t].max])
json_string = json.dumps(json_sound)
str="json_sound='"+json_string+"'"
with open('json_sound.js', 'w') as f:
    f.write(str)

