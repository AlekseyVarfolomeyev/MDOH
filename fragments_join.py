import json

f = open("fragments.json")
fragments = json.load(f)
n = len(fragments)

result=list()
result_laugh=list()

for i in range(0, n):
    shift = fragments[i][1]
    f = open("fragment"+str(i)+".json")
    fragment = json.load(f)
    for x in fragment:
        y = x["time"]
        A = int(y["start"]*1000 + shift)
        B = int(y["end"]*1000 + shift)
        y["start"] = A
        y["end"] = B
        result.append(x)
        z = x["audio tags"]
        if(len(z)>0):
            res_str=""
            for u in z:
                res_str=res_str+str(u[0][:2])+","
            result_laugh.append([A,B,res_str[:-1]])

json_string = json.dumps(result)
with open('whisper_at.json', 'w') as f:
    f.write(json_string)
js_string = json.dumps(result_laugh)
js_string="laugh='"+js_string+"'"
with open('laugh.js', 'w') as f:
    f.write(js_string)