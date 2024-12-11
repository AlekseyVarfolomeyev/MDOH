import whisper_at as whisper
import json

f = open("fragments.json")
fragments = json.load(f)
n = len(fragments)

audio_tagging_time_resolution = 0.4
model = whisper.load_model("large")

for i in range(0, n):
    print(i)
    result = model.transcribe("fragment"+str(i)+".wav", at_time_res=audio_tagging_time_resolution)
    audio_tag_result = whisper.parse_at_label(result, language='follow_asr', top_k=7, p_threshold=-7, include_class_list=list(range(16,22)))
    json_result = json.dumps(audio_tag_result)
    f = open("fragment"+str(i)+".json", "w")
    print(f.write(json_result))
    f.close()