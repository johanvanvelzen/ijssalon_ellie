from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    korting = prijs*(1-korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro"
    return uitvoer
print(aanbieding_1("aardbei",4,0.1)) 

def inkomsten_totaal(inkomsten,btw):
    inkomsten= sum(inkomsten)
    btw=inkomsten * 0.09
    return f"Het totaal van alle inkomsten deze week is {inkomsten} euro, waarover {btw} euro btw betaald dient te worden"  
inkomsten_lijst= [220,430,125,160,205,90,345]
btw_percentage= 0.09
resultaat=inkomsten_totaal(inkomsten_lijst,btw_percentage)
print(resultaat)

def laag_en_hoog(mijn_lijst):
    laagste_inkomst = min(mijn_lijst)
    hoogste_inkomst = max(mijn_lijst)
    return laagste_inkomst,hoogste_inkomst
resultaat=laag_en_hoog(inkomsten_lijst)
print(resultaat)

def gemiddelde(mijn_lijst):
    som=sum(mijn_lijst)
    gem=som/len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gem} euro"
resultaat=gemiddelde(inkomsten_lijst)
print(resultaat)

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
getallen_lijst=[10,5,3,2,1,2,9]
resultaat=meervoudig(getallen_lijst)
print(resultaat)

def combinatie(invoer_lijst_2):
    korte_lijst=laag_en_hoog(invoer_lijst_2)
    uitvoer=mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer