import json
from pydub import AudioSegment
sound = AudioSegment.from_file("audio_record.wav", format="wav")
full_t=len(sound) # full time of audio in ms
f = open("json_sentences_aligned.json")
sentences = json.load(f)
n = len(sentences)
step=30
k=0
fragments=list()
for i in range(0, n, step):
    start_fragment=sentences[i][1]
    if(i+step<n):
        end_fragment=sentences[i+step][1]
    else:
        end_fragment=full_t
    sound[start_fragment:end_fragment].export("fragment"+str(k)+".wav", format="wav")
    a = [k, start_fragment, end_fragment]
    fragments.append(a)
    k=k+1
json_string = json.dumps(fragments)
with open('fragments.json', 'w') as f:
    f.write(json_string)
    