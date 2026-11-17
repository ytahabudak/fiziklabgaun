# Sunucuda klasör listeleme kapalıysa, dersler yüklendikten sonra bu dosya çalıştırılır:  python liste-olustur.py
import os, json
b = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dersler")
isd = lambda *p: os.path.isdir(os.path.join(b, *p))
d = {k: sorted(x for x in os.listdir(os.path.join(b, k)) if isd(k, x)) for k in sorted(os.listdir(b)) if isd(k)}
json.dump(d, open(os.path.join(b, "liste.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(d), "ders listelendi.")
