from gtts import gTTS
class ttsEX:
    def __init__(self):
        self.text = "초기화상태"
        self.FileName = "파일이름"
    def makeSound(self):
        tts = gTTS(text=self.text, lang='ko')
        tts.save(f"{self.FileName}.mp3")

if __name__ == '__main__':
    t = ttsEX()
    t.text = "3-1 tts 예제 입니다"
    t.FileName = "테스트1"
    t.makeSound()
