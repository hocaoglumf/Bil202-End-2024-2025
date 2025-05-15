import tkinter as tk

# Başlangıç listesi
veri_listesi = ["Elma", "Armut", "Muz", "Kiraz", "Karpuz"]

# Ana pencere
pencere = tk.Tk()
pencere.title("EditBox Listesi Güncelleme")

# Entry kutularını tutacak liste
entry_kutulari = []

# Entry kutularını oluştur ve liste öğelerini yerleştir
for oge in veri_listesi:
    entry = tk.Entry(pencere, width=30)
    entry.insert(0, oge)
    entry.pack(padx=10, pady=5)
    entry_kutulari.append(entry)

# Güncelleme fonksiyonu
def listeyi_guncelle():
    global veri_listesi
    veri_listesi = [entry.get() for entry in entry_kutulari]
    print("Güncellenmiş liste:", veri_listesi)

# Güncelle butonu
guncelle_butonu = tk.Button(pencere, text="Güncelle", command=listeyi_guncelle)
guncelle_butonu.pack(pady=10)

# Pencereyi çalıştır
pencere.mainloop()
