# -*- coding: utf-8 -*-
"""Download image assets for SunLion Energy website (demo)."""
import os
import urllib.request

DEST = r"C:\Users\Dell\DoubaoWork\chats\2026-09-26\new-chat\sunlion-energy\assets"

IMAGES = [
    ("hero-skyline.jpg", "https://aka.doubaocdn.com/s/ST0zU79xhM"),
    ("aerial-city.jpg", "https://aka.doubaocdn.com/s/KU6xg2aNzU"),
    ("home-dusk.jpg", "https://aka.doubaocdn.com/s/flnAYIggcX"),
    ("industrial-aerial.jpg", "https://aka.doubaocdn.com/s/xweNDTVt76"),
    ("home-modern.jpg", "https://aka.doubaocdn.com/s/AtXs29nhGh"),
    ("hdb-rooftop.jpg", "https://aka.doubaocdn.com/s/xweRBy8iIs"),
    ("technician.jpg", "https://aka.doubaocdn.com/s/nTyFZCUZtZ"),
    ("technician-wiring.jpg", "https://aka.doubaocdn.com/s/hDb99HME0K"),
]

os.makedirs(DEST, exist_ok=True)

for name, url in IMAGES:
    path = os.path.join(DEST, name)
    if os.path.exists(path) and os.path.getsize(path) > 10000:
        print("skip", name)
        continue
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
        with open(path, "wb") as f:
            f.write(data)
        print("ok  ", name, len(data))
    except Exception as e:
        print("FAIL", name, repr(e))
