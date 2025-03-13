class LogDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"{self.func.__name__} çağrıldı.")
        return self.func(*args, **kwargs)

@LogDecorator
def selam_ver():
    print("Merhaba!")

selam_ver()
