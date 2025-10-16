from diaries.DiarySample import DiarySample
from diaries.OguraDiary import OguraDiary
from diaries.NatsumeDiary import NatsumeDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(), 
    OguraDiary(), 
    NatsumeDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
