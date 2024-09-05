# simple-voicevox
a very simple Python script that talks with the voicevox API
install requests library
```python
pip install requests
```
example for using the function
```python
import voicevox

voicevox.handle("the voicevox ip", "the wav file name", "the text you want to enter in Japanese", "the character number")
#example for actual use
voicevox.handle("http://127.0.0.1:50021", "zanu", "よよだよ", 1)
```
