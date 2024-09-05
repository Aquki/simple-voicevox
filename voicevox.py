import sys
import requests as re



#the main handle function that contains all information
def handle(voicevox, name, text, speaker):
    #check if the URL works and set values and launch other functions with those values
    try:
        check = re.get(voicevox)
        if check.status_code == 404:
            query = f"{voicevox}/audio_query"
            synthesis = f"{voicevox}/synthesis"
            send(query, synthesis, name, text, speaker)

    except re.exceptions.RequestException:
        print("There is error during the connection in the URL or VOICEVOX is not running")
        sys.exit()

#the function that will send the request to VoiceVox API and return it and save it
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


