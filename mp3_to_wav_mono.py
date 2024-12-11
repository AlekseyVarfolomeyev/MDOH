from pydub import AudioSegment
sound = AudioSegment.from_file("audio_record.mp3", format="mp3")
sound_mono = sound.split_to_mono()

sound_mono[0].export("audio_record.wav", format="wav")