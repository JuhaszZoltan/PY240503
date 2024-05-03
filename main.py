from module import *

versenyek:list[Verseny] = []
file = open('paralimpia.txt', 'r', encoding='utf-8')
for r in file: versenyek.append(Verseny(r))

print(f'eddig {len(versenyek)} alkalommal kerult megrendezesre')

print(f'eloszor {versenyek[0].orszag} rendezett paralimpiat')

oe:int = 0
for v in versenyek:
    oe += (v.arany + v.ezust + v.bronz)
print(f'a magyarok osszesen {oe} ermet szereztek')

va:int = 0
for v in versenyek:
    if v.arany > 0:
        va += 1
print(f'a magyarok {va} versenyen szereztek egalabb egy aranyat')

mi:int = 0
for i in range(1, len(versenyek)):
    if versenyek[i].arany > versenyek[mi].arany:
        mi = i
print(f'az {versenyek[mi].varos}i paralimian szereztek a magyarok legtobb aranyat')

ke:int = int(input('irj be egy evszamot: '))
for v in versenyek:
    if v.ev == ke:
        print(f'a {v.ev}ban/ben a paralimpiat {v.orszag} szervezte')
        break
else: print(f'{ke} évben nem volt paralimpia')

evek:list[int] = []
for v in versenyek:
    if v.arany == 0 and v.ezust == 0 and v.bronz == 0:
        evek.append(v.ev)
print(f'a kovetkezo evekben nem volt egyetlen magyar dobogos helyezes sem:')
print(evek)