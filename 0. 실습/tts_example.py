from gtts import gTTS
from playsound import playsound
class ttsEX:
    def __init__(self):
        self.text = "초기화상태"
        self.FileName = "파일이름"
    def makeSound(self):
        tts = gTTS(text=self.text, lang='ko')
        tts.save(f"{self.FileName}.mp3")

if __name__ == '__main__':
    t = ttsEX()
    t.FileName = input("제목 입력: ")
    t.text = input("Sound 텍스트 입력: ")
    t.makeSound()

    playsound(f"{t.FileName}.mp3")

