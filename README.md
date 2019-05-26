# Analiza registra vozil z povdarkom na razlikah med spoloma
### Vmesno poročilo
## Simon Zajc, 63140292, 2.4.2019

### Uvod
Nisem zagovornik enakosti spolov. Prosim, tega ne pomešati z enakopravnostjo. Sem velik zagovornik enakopravnosti, enakih možnosti in pravic vendar to ne pomeni, da sta spola enaka. Razlike med povprečnim moškim in povprečno žensko obstajajo in ne le da niso problem, so lepe in nujno potrebne. <br>
Ta "problematika" me že od zmeraj zanima, tako da sem hotel raziskovati nekaj v tej smeri. Pregledal sem kar nekaj različnih zbirk podatkov (Slovenskih, saj mi je ljub rek: "Najprej pospravi pred svojim pragom, potem pa glej drugam!") na koncu pa sem se vrnil k zbirki podatkov "Prvič registrirana vozila, po mesecih" iz slovenskega statističnega urada (https://podatki.gov.si/dataset/prvic-registrirana-vozila-po-mesecih). 
#### Zaradi polne odkritosti bi rad povedal, da sem projekt z to zbirko podatkov že delal pred dvemi leti ravno pri tem predmetu (PR) vendar sem se vsega, vključno z obdelavo podatkov lotil popolnoma od začetka. Sošolec, z katerim sva projekt opravljala, je tisto leto zaključil predmet (Pri projektu sem sodeloval do konca).

### Podatki
Sta 2 glavna razloga, da sem se odločil za to zbirko podatkov in ne kakšno drugo.<br>
- Podatkov je v tej zbirki ogromno in se dejansko da opravljati dobre analize.<br>
- Z to zbirko sem se že srečal, tako da sem se delno spominjal problemov pri sami pripravi podatkov (ti problemi so vzeli daleč od zanemarljivega dela časa izdelave prvega projekta, pa tudi tokrat ni bilo mačji kašelj).<br>
Podatki ze leti 2012 in 2013 sta v eni CSV datoteki. Ker je večina (leta od 2014 - 2018) v po 12 csv datotekah (ena za vsak mesec) sem se odločil da tudi da tudi leti 2012 in 2013 razdelim na 12 delov. Sproti sem še odstranil slabe vrstice (v datotekah so vrstice z milo rečeno mankajočimi stolpci).

```
    for line in original:
        splt = line.split(";")
        if len(splt) < 54:
            continue
        dt = splt[2].split(".")
        if dt[1] == "1":
            if written < 1:
                new1.write(firstLine)
                written += 1
            new1.write(line)
        if dt[1] == "2":
            ...

```
Po tem sem vse datoteke poimenoval na isti način (v originalu so imele zelo različna imena, tudi v istem letu) po ključu XXX_YY (LETO_MESEC) ter jih shranil v poddirektorij mojega projekta.

Ko sem se lotil analize podatkov sem naletel še na mnogo problemov pri samem formatu datotek. Da naštejem nekaj od njih ter rešitve:
- python ni zaznal kodiranja (Opredelil sem kodiranje (latin-1))
- še vedno problemi z posebnimi znaki č, š, ž (ročno sem v vseh datotekah zamenjal vse znake z C. Ni idealno a za nadaljno analizo zadostuje)
- Razlika med stolpci ter njihovimi imeni v različnih datotekah (napisal sem različne rešitve za različne datoteke (vse v isti kodi))
- ...

### Koda
Programska koda, uporabljena za dosedanjo analizo je v datoteki main.py na tem repozitoriju.

### Vprasanje
Bolj kot točno določeno vprašanje me zanima celoten pregled razlik med spoloma pri vozilih v osebni lasti (fizične osebe). Vendar vseeno zastavimo nekaj hipotez, vendar se tekom projekta ne bom omejeval le na tukaj zastavljene hipoteze:
- Hipoteza 1: Moški imajo v povprečju močnejše avtomobile kot ženske.
- Hipoteza 2: Razlika med spoloma v povprečni moči avtomobilov se povečuje.
- Hipoteza 3: Pri občutno višjih konskih močeh (npr. 200+ konjskih moči se odstotek moških lastnikov močno poviša (vendar z leti zmanjšuje))
- Hipoteza 4: Spola težita k različnim barvam, znamkam, tipom itd. vozil.
- Hipoteza 5: Moški registrirajo več novih vozil.
- Hipoteza 6: Z leti se razlika pri številu vozil v lasti/uporabi med spoloma zmanjšuje.
- ...
Odgovori na ta vprašanja so lahko več kot le zanimivost, trendi, ki jih bomo tekom projekta zaznali in raziskali lahko pridejo prav na različnih področjih kot so naprimer marketing, izobraževanje,...

### Odgovori
Hipoteza 1 in 2:<br>
Glej graf 1 in graf 2. Hipoteza je ne-trdno potrjena. Ugotovitev, da so določeni meseci/leta kjer imajo ženske v povprečju močnejše avtomobile (po novih registracijah) me je šokirala, še toliko bolj ker sem gledal po uporavniku in ne po lastniku, kjer bi to razliko po moji logiki lažje upravičil. Moč z leti počasi a gotovo raste, razlika med moškim in žensko pa se načeloma zelo počasi povečuje (leto 2017 hudo odstopa, tako da ga, dokler vzroka bolje ne raziščem, ignoriram).
Hipoteza 3:<br>
Glej graf 3. Hipoteza potrjena. Moški pri močnejših motorjih močno prevladujejo.
Hipoteza 4:<br>
Odgovarjanje še v teku.
Hipoteza 5:<br>
Glej graf 4. Hipoteza potrjena, moški res registrirajo več vozil.
Hipoteza 6:<br>
Glej graf 4. Hipoteza ovržena. Zadnjih 7 let se razlika počasi a konstantno celo povečuje. To me je presenetilo in mislim da bi bilo smiselno iskati razloge na različnih mestih, mogoče novi zakoni ali kaj podobnega.

### Priponke
![alt text](https://user-images.githubusercontent.com/12514564/55438064-e4026000-55a0-11e9-8789-3e37f8869a15.jpeg)

graf 1

![alt text](https://user-images.githubusercontent.com/12514564/55438065-e49af680-55a0-11e9-800e-3bc56df7f9e2.jpeg)

graf 2

![alt text](https://user-images.githubusercontent.com/12514564/55438066-e49af680-55a0-11e9-976e-e794c6f33a99.jpeg)

graf 3

![alt text](https://user-images.githubusercontent.com/12514564/55438067-e49af680-55a0-11e9-84ba-e34fefb2ca6c.jpeg)

graf 4
