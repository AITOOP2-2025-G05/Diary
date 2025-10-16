from diaries.DiarySample import DiarySample
from diaries.OguraDiary import OguraDiary
from diaries.NatsumeDiary import NatsumeDiary
from diaries.KuwabaraDiary import KuwabaraDiary
from diaries.KanbeDiary import KanbeDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(), 
    OguraDiary(), 
    NatsumeDiary(), 
    KuwabaraDiary(), 
    KanbeDiary(),
]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
