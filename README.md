# simple-voicevox
a very simple Python script that talks with the voicevox API
install requests library
```python
pip install requests
```
example for using the script
```python
import voicevox

voicevox.handle(text="おはよう！", speaker=1, name="output", voicevox="VOICEVOX URL")

#example for actual use
voicevox.handle( "おやすみ！", 1, "filename", "http://127.0.0.1:50021")
```
