import keyboard
import time

keyboard.start_recording()
ksüre = int(input("Klavye kaydı kaç saniye sürsün--->"))
print("Kayıt başlatılıyor!")
print("3")
print("2")
print("1")
time.sleep(ksüre/4)

print("Geçen süre"+str(ksüre/4))
time.sleep(ksüre/4)
print("Geçen süre"+str(ksüre/3))
time.sleep(ksüre/4)
print("Geçen süre"+str(ksüre/2))
time.sleep(ksüre/4)
print("Geçen süre"+str(ksüre/1))
time.sleep(ksüre)
print("KAYIT TAMAMLANDI!")
time.sleep(1)
kayıtlar = keyboard.stop_recording()
print("KAYIT BAŞARILI! KAYIT BAŞLATILIYOR.")
keyboard.replay(kayıtlar)
