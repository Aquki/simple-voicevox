import sys
import requests as re

#a simple Python script that handles the Local VOICEVOX API and returns a wav output

def main(text="こんばんわ", speaker=1, name="output", voicevox="http://127.0.0.1:50021"):
    handle(text, speaker, name, voicevox)


#the main handle function that contains all information
def handle(text=None, speaker=1, name="output", voicevox="http://127.0.0.1:50021"):
    #check if the host is working and set values and launch the send function with the values
    try:
        check_response = re.get(voicevox)

        if check_response.status_code == 404: #check if the host is ON with 404 status code
            print("VOICEVOX is up!")
            print("Sending the request...")
            query = f"{voicevox}/audio_query"
            synthesis = f"{voicevox}/synthesis"
            send(query, synthesis, text, speaker, name)

    except re.exceptions.RequestException as error:
        print("VOICEVOX maybe not running or the API URL is not right")
        print(error)
        sys.exit()
        
#the function that will send the request to VoiceVox API and return it and save it
def send(query, synthesis, text, speaker, name):

    query_para = {"text": text, "speaker": speaker}
    synthesis_para = {"speaker": speaker}

    try:
        json_request = re.post(query, params=query_para)
        result = re.post(synthesis, json=json_request.json(), params=synthesis_para)
        save(name, result)
        
    except re.exceptions.RequestException as error:
        print("VOICEVOX maybe not running or the API URL is not right")
        print(error)
        sys.exit()
        


#simple save function to save the wav file from the request
def save(name, result):
        with open(f"{name}.wav", "wb") as w:
          w.write(result.content)
        print(f"file saved to {name}.wav")

if __name__ == "__main__":
    main()
