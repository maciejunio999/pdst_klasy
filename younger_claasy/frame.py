# jakis niedokończony projekt
# zupełnie nie pmiętam o co tu chodziło

import pandas as pd
from klasy import Person

maciek = Person("Maciek", 21)
mama = Person("Joanna", 43)
ala = Person("Alicja", 16, mama)
lena = Person("Lena", 8, mama)

df = pd.Series({
    "Person": [maciek, mama, ala, lena]
    }
)

print(df)
