import tkinter as tk

# Verilen liste
veri_listesi = ["Elma", "Armut", "Muz", "Kiraz", "Karpuz"]

# Ana pencereyi oluştur
pencere = tk.Tk()
pencere.title("Liste Görüntüleyici")

# Listbox oluştur
liste_kutusu = tk.Listbox(pencere, width=30, height=10)
liste_kutusu.pack(padx=10, pady=10)

# Verileri Listbox'a ekle
for oge in veri_listesi:
    liste_kutusu.insert(tk.END, oge)

# Pencereyi çalıştır
pencere.mainloop()
