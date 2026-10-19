#!/usr/bin/env python3
# Abartılı Sabah Alarm Makinesi
# Sizi uyandırmak için evreni seferber eder.

import time
import random

nutuklar = [
    "UYAN! Güneş doğdu, sen de doğmalısın. Aksi halde gün batacak ve sen hâlâ yatakta olacaksın. Kabul edilemez!",
    "Kalk ayağa! Hayat bir maraton, sen ise yastığınla evlenmişsin. Boşan artık!",
    "Uyandın mı? Hayır mı? O zaman ben yine konuşacağım. Evren sabırsız.",
    "Bu alarm çalıyor çünkü sen önemli birisin. En azından şimdi. Kalk ve önemli ol."
]

def alarm_cal():
    print("\n" + "="*50)
    print("ALARM ÇALIYOR!!!")
    print("="*50)
    for _ in range(3):
        print(random.choice(nutuklar))
        time.sleep(1.5)
        print("Bip bip bip... (yazılı bip)")
        time.sleep(0.5)
    print("\nTamam, yeter. Uyanmış olmanı umuyorum. Yoksa tekrar çalarım.")

if __name__ == "__main__":
    print("Sabah alarmı kuruluyor...")
    input("Hazır olduğunda Enter'a bas (gerçek hayatta bu saat alarmı olurdu): ")
    alarm_cal()

# Gizli siyasi not: Alarmlar da seçim gibi, erken basan kazanır.
