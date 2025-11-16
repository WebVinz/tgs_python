# nested = bersarang
# di dalam if/elif/else ada conditional

# cerita horror
print("Malam itu hujan deras di depan sekolah TKR.")
print("Kamu sendirian; ada suara langkah dari belakang gudang.")
print("1. Pergi lihat suara")
print("2. Mengunci diri dan menunggu")
print("3. Lari ke ruang kelas terdekat")

try:
    choice = int(input("Pilih (1/2/3): "))
except ValueError:
    choice = 0

ending = "jokes" 
note = ""

if choice == 1:
    print("Kamu mengintip dari celah pintu gudang.")
    print("Di dalam ada bayangan memegang boneka.")
    print("1. Panggil dengan suara keras")
    print("2. Mendekat pelan untuk melihat wajahnya")
    sub = input("Pilih (1/2): ").strip()
    if sub == "1":
        ending = "bad"
        note = "Bayangan itu adalah reginang dan menoleh dengan mata kosong, kamu dikejar rasa takut selamanya."
    elif sub == "2":
        ending = "true"
        note = "Kamu melihat wajahmu sendiri di boneka, kamu ternyata adalah reginang."
    else:
        ending = "jokes"
        note = "Karena kamu ga milih , kamu pun di ubah jadi rendang."

elif choice == 2:
    print("Kamu mengunci diri di dalam container, menahan napas.")
    print("Dari celah terlihat sepasang mata menatap.")
    print("1. Nyalakan senter")
    print("2. Tetap diam sampai pagi")
    sub = input("Pilih (1/2): ").strip()
    if sub == "1":
        ending = "bad"
        note = "Senter memantul ke jam tua, jarum mundur dan kamu terjebak selamanya."
    elif sub == "2":
        ending = "happy"
        note = "Pagi datang, tidak ada yang menakutkan, ternyata hanya prank (selamat kamu kena prank)."
    else:
        ending = "jokes"
        note = "Karena kamu ga milih , kamu pun di ubah jadi rendang"

elif choice == 3:
    print("Kamu lari ke ruang kelas. Papan tulis menulis pesan: 'TANYA NAMA AKU'")
    print("1. Menjawab papan tulis")
    print("2. Menghapus pesan dan keluar mencari petugas")
    sub = input("Pilih (1/2): ").strip()
    if sub == "1":
        ending = "bad"
        note = "Papan menulis balik dan menukar hidupmu dengan reginang."
    elif sub == "2":
        ending = "happy"
        note = "Petugas datang, cek CCTV, semuanya aman. Kamu selamat."
    else:
        ending = "jokes"
        note = "Karena kamu ga milih , kamu pun di ubah jadi rendang."

else:
    ending = "jokes"
    note = "Kamu pulang."

print("--- PENUTUP ---")
if ending == "bad":
    print("Bad Ending")
    print("Main yang bener dek,", note)
elif ending == "happy":
    print("Happy Ending")
    print("Kamu selamat dan semuanya kembali normal,", note)
elif ending == "true":
    print("True Ending")
    print("Kebenaran terungkap,", note)
else:
    print("Jokes Ending")
    print("Cupu,", note)

print("Terima kasih sudah bermain, semoga kalian bisa makan rendang")
