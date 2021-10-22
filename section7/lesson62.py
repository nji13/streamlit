import os
from google.cloud import texttospeech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'secret.json'

client = texttospeech.TextToSpeechClient()

synthesis_input = texttospeech.SynthesisInput(text="こんにちは、私は長谷川です。")

voice = texttospeech.VoiceSelectionParams(
    language_code="ja-JP", ssml_gender=texttospeech.SsmlVoiceGender.MALE
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

filename = "output.mp3" 
with open(filename, "wb") as out:
    out.write(response.audio_content)
    print(f'音声データは{filename}ファイルに書き出しました')