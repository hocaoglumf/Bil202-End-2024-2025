'''
Python'da decorator (dekoratör), fonksiyonları veya sınıfları değiştirmeden onların işlevselliğini genişletmeye yarayan özel bir tasarım desenidir. Decorator, bir fonksiyonu argüman olarak alıp ona ek işlevsellik kazandıran ve yine bir fonksiyon döndüren bir fonksiyondur.
Decorator Şablonu
Genel decorator şablonu aşağıdaki gibidir:
'''

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        # Ekstra işlemler
        print(f"{original_function.__name__} fonksiyonu çağrıldı.")
        result = original_function(*args, **kwargs)  # Orijinal fonksiyon çalıştırılır
        # Ekstra işlemler
        print(f"{original_function.__name__} fonksiyonu tamamlandı.")
        return result  # Orijinal fonksiyonun çıktısını döndür
    return wrapper_function


@decorator_function
def example_function():
    print("Bu, orijinal fonksiyonun çalıştığını gösterir.")

example_function()
