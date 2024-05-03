from random import choice

class Verseny:
    def __init__(self, row:str) -> None:
        v:list[str] = row.strip().split(';')
        self.ev:int = int(v[0])
        self.orszag:str = v[1]
        self.varos:str = v[2]
        self.arany:int = int(v[3])
        self.ezust:int = int(v[4])
        self.bronz:int = int(v[5])

cicanevek:list[str] = ['Áfonya', 'Apolló', 'Apacs', 'Babett', 'Britney', 'Borsó', 'Crazy', 'Csipesz', 'Doris', 'Espresso', 'Elektra', 'Falánk', 'Gomez', 'Hópihe', 'Hilton', 'Írisz', 'Kása', 'Lidérc', 'Love', 'Lucifer', 'Masni', 'Misa', 'Mugli', 'Nárcisz', 'Nelson', 'Pocok', 'Picur', 'Rubin', 'Szurok', 'Szüttyő', 'Tigris', 'Tepsi', 'Úrfi', 'Vanília', 'Yoda', 'Zselé', 'Zakó', 'Zeusz']

def f01() -> None:
    a:int = int(input('"a" értéke:= '))
    b:int = int(input('"b" értéke:= '))
    e:int = abs(a - b)
    print(f'a két szák különbségének abszolút értéke: {e}')
    if e % 3 == 0: print('osztható 3-al')
    else: print('NEM osztható 3-al')

def f02() -> None:
    rcn:str = choice(cicanevek)
    e:int = 0
    for c in rcn.lower():
        if c == 'e': e += 1 
    print(f'valasztott cicavev: {rcn}; e betuk szama: {e}')
    while input('tetszik a nev?: ') != 'igen':
        print(f'uj javaslat: {choice(cicanevek)}')
    print('cg, bye!')

