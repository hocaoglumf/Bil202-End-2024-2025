class Music:
    @staticmethod
    def play():
        print("*playing music*")

    def stop(self):
        print("stop playing")

    @classmethod
    def Pause(cls):
        print("Music paused ")

n=Music()
Music.play()
Music.Pause()
n.stop()