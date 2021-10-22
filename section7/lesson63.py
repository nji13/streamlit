import os
from google.cloud import texttospeech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'secret.json'

def synthesize_speech(text, lang='日本語', gender='default'):
    gender_type = {
        'default': texttospeech.SsmlVoiceGender.SSML_VOICE_GENDER_UNSPECIFIED,
        'male': texttospeech.SsmlVoiceGender.MALE,
        'female': texttospeech.SsmlVoiceGender.FEMALE,
        'neutral': texttospeech.SsmlVoiceGender.NEUTRAL,
    }
    lang_code = {
        '英語': 'en-US',
        '日本語': 'ja-JP'
    }

    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code=lang_code[lang], ssml_gender=gender_type[gender]
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    return response

gender = 'default'
lang = '英語'
text = "This is a sample text for using cloud text-to-speech."

aaa = synthesize_speech(text, lang, gender='male')
filename = "output.mp3" 
with open(filename, "wb") as out:
    out.write(aaa.audio_content)
    print(f'音声データは{filename}ファイルに書き出しました')
