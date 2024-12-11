import json

f = open("json_whisper.json")
myobj = json.load(f)
symb_of_end = [".","!","?"]
json_words = list()
for x in myobj['segments']:
	for y in x['words']:
		begin_of_word = int(y['start']*1000)
		end_of_word = int(y['end']*1000)
		word = y['word']
		n = len(word)
		last_symb = word[n-1]
		end_of_sentence = 0
		if(last_symb in symb_of_end):
			end_of_sentence = 1
		a = [word, begin_of_word, end_of_word, end_of_sentence]
		json_words.append(a)
json_string = json.dumps(json_words)
with open('json_words.json', 'w') as f:
    f.write(json_string)
new_string = json_string.replace("'", "\\'")
str="json_words='"+new_string+"'"
with open('json_words.js', 'w') as f:
    f.write(str)
	
json_sentences = list()	
s = ""
k = 0	
for z in json_words:
	if(s==""):
		start=z[1]
	if(z[3]==0):
		s=s+z[0]
		k=k+1
	if(z[3]==1):
		s=s+z[0]
		k=k+1
		end=z[2]
		b = [s, start, end, k]
		json_sentences.append(b)
		s=""
		k=0

json_string = json.dumps(json_sentences)

with open('json_sentences_raw.json', 'w') as f:
    f.write(json_string)

