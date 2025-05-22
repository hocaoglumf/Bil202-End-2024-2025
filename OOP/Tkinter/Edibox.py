import tkinter as tk

# Verilen liste
veri_listesi = ["Elma", "Armut", "Muz", "Kiraz", "Karpuz"]

# Ana pencereyi oluştur
pencere = tk.Tk()
pencere.title("EditBox'larda Liste Öğeleri")

# Listedeki her bir öğe için bir Entry (editbox) oluştur ve yerleştir
for oge in veri_listesi:
    entry = tk.Entry(pencere, width=50)
    entry.pack(padx=10, pady=5)
    entry.insert(0, oge)  # Entry içine veri yerleştir

# Pencereyi çalıştır
pencere.mainloop()
