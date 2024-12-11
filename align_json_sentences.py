import json
from pydub import AudioSegment
sound = AudioSegment.from_file("audio_record.wav", format="wav")
full_t=len(sound) # full time of audio in ms
delta_t=10
threshold_of_silence=500
f = open("json_sentences_raw.json")
sentences = json.load(f)
n = len(sentences)

onsets=list()

for t in range(0, full_t, delta_t):
	if sound[t:t+delta_t].max<threshold_of_silence and sound[t+delta_t:t+2*delta_t].max>=threshold_of_silence:
		onsets.append(t)

for i in range(0, n):
	start_sentence=sentences[i][1]
	j=start_sentence
	while j not in onsets and j>0:
		j=j-1
	if(j in onsets):
		left_start=j
	else:
		left_start=-1
	j=start_sentence
	while j not in onsets and j<full_t:
		j=j+1
	if(j in onsets):
		right_start=j
	else:
		right_start=full_t+1
	if(left_start==-1):
		new_start=right_start
	elif(right_start==full_t+1):
		new_start=left_start
	else:
		if(start_sentence-left_start > right_start-start_sentence):
			new_start=right_start
		else:
			new_start=left_start
	sentences[i][1]=new_start
	if(i>0):
		sentences[i-1][2]=new_start

json_string = json.dumps(sentences)
with open('json_sentences_aligned.json', 'w') as f:
    f.write(json_string)
new_string = json_string.replace("'", "\\'")
str="json_sentences='"+new_string+"'"
with open('json_sentences_aligned.js', 'w') as f:
    f.write(str)
		
	