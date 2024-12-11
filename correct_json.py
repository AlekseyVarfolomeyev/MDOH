import json
from pydub import AudioSegment
sound = AudioSegment.from_file("EngConv32_1.wav", format="wav")
full_t=len(sound) # full time of audio in ms
delta_t=10
threshold_of_silence=2000
f = open("EngConv32_1_fw1.json")
myobj = json.load(f)
json_words = list()
for x in myobj['segments']:
	id_of_segment = x['id']
	k = 0
	for y in x['words']:
		begin_of_word = int(y['start']*1000)
		end_of_word = int(y['end']*1000)
		a = [id_of_segment, k, y['word'], begin_of_word, end_of_word]
		json_words.append(a)
		k = k+1
#print(json_words)
begin=list()
end=list()
for i in range(0, full_t, delta_t):
	#print(i, sound[i:i+delta_t].max)
	if sound[i:i+delta_t].max<threshold_of_silence and sound[i+delta_t:i+2*delta_t].max>=threshold_of_silence:
		begin.append(int(i+0.5*delta_t))
	if sound[i:i+delta_t].max>=threshold_of_silence and sound[i+delta_t:i+2*delta_t].max<threshold_of_silence:
		end.append(int(i+1.5*delta_t))
#print('begins: ', len(begin))
#print('ends: ', len(end))
for j in range(0,min(len(begin),len(end))):
	if(end[j]-begin[j]<50 and sound[begin[j]:end[j]].max<4000):
		begin[j]=full_t+1
		end[j]=full_t+1
begin= [x for x in begin if x != full_t+1]
end= [x for x in end if x != full_t+1]
print('begins: ', len(begin))
print('ends: ', len(end))
found_words = list()
for j in range(0,min(len(begin),len(end))):
	for m in range(0,len(json_words)):
		#print(begin[j],json_words[m][3],end[j],json_words[m][4])
		#print(max(begin[j],json_words[m][3]),min(end[j],json_words[m][4]))
		if(max(begin[j],json_words[m][3])<min(end[j],json_words[m][4])):
			#print('found',m,' in',j)
			found_words.append([j,json_words[m]])
for j in range(0,min(len(begin),len(end))):
	for k in range(0,len(found_words)):
		if(found_words[k][0]==j):
			print(j,begin[j], end[j], end[j]-begin[j], sound[begin[j]:end[j]].max, found_words[k][1])