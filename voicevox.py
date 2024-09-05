import sys
import requests as re



#the main handle function that contain all inforamtion
def handle(voicevox, name, text, speaker):
    #check if the url work and set values and launch other function with thos values
    try:
        check = re.get(voicevox)
        if check.status_code == 404:
            query = f"{voicevox}/audio_query"
            synthesis = f"{voicevox}/synthesis"
            send(query, synthesis, name, text, speaker)

    except re.exceptions.RequestException:
        print("There is error druing the connection in the URL or VOICEVOX is not running")
        sys.exit()

#the function that will send the request to VoiceVox api and return it and save it
def send(query, synthesis, name, text, speaker):
    
    query_para = {"text": text, "speaker": speaker}
    synthesis_para = {"speaker": speaker}

    try:
        ob = re.post(query, params=query_para)
        result = re.post(synthesis, json=ob.json(), params=synthesis_para)

        save(name, result)
    except re.exceptions.RequestException:
        print("VoiceVox maybe not running or the API is not right")
        sys.exit()
#simple save function
def save(name, result):
        with open(f"{name}.wav", "wb") as w:
          w.write(result.content)


