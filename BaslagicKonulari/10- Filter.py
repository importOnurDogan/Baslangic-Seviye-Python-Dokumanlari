import pandas as pd
import seaborn as sns
import numpy as np
df = pd.DataFrame({"gruplar":["a","b","c","a","b","c"],
                   "degisken1":[90,85,80,95,75,70],
                   "degisken2":[100,200,900,800,700,600]},
                  columns = ["gruplar","degisken1","degisken2"])

"kendi kişisel fonksyonlarımızı bir filtreleme aracı olarak değişkenler" \
"üzerinde sorgulama yapılacak"

def filter_func(x):
    return x["degisken1"].std()>5
print(df.groupby("gruplar").filter(filter_func))
