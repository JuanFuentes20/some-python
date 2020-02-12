'''
Created on 12 Nov 2018

@author: juan
'''
def sanakoe(nimi):
    matriisi = []

    try:
        tiedot = open(nimi, "r")
        for rivi in tiedot:
            lista = []
            rivi = rivi.rstrip()
            parts = rivi.split(":")
            
            try:
                parts2 = parts[1].split("/")
                parts2 = [parts[0], parts2]
                for arvot in parts2:
                    if arvot != "":
                        lista.append(arvot)
                        #print(lista)
                
            except AttributeError:
                if len(rivi) == 2:
                    for arvot in rivi:
                        lista.append(arvot)
                
            except IndexError:
                pass
            for info in lista:
                if info == ['']:
                    lista = 0
                for arvot in info:
                    if arvot == "":
                        lista = 0
            if lista == [] or lista == 0:
                print("ERROR in line:", rivi)
                
            else:
                matriisi.append(lista)
        tiedot.close()
        return matriisi
                    
    except OSError:
        return 0

def sana_koe(testi):
    p = len(testi)
    uusilista = []
    sanakirja = {}
    i = 0
    while i < p:
        sanakirja[testi[i][0]] = testi[i][1]
        merkkijono = str(testi[i][1][0])
        merkkijono1 = merkkijono.lower()
        print(testi[i][0])
        print(testi[i][1])
        kaannos = str(input())
        kaannos2 = kaannos.lower()
        if kaannos2 in merkkijono1 and len(kaannos) == len(merkkijono1) or kaannos in testi[i][1]:
            print("Correct!")
        else:
            print("Incorrect, try again!")
            kaannos3 = str(input())
            kaannos4 = kaannos3.lower()
            uusilista.append(testi[i])
            if kaannos4 in merkkijono1 and len(kaannos3) == len(merkkijono1) or kaannos3 in testi[i][1]:
                print("That was correct.")
                
                
            else:
                print("Incorrect again, the correct answer is", testi[i][1][0])
                
        i += 1  
    
    return uusilista

def main():
    print("This is a vocabulary quiz.")
    nimi = input("Enter the name of the file used.\n")
    testi = sanakoe(nimi)
    if testi == 0:
        print("ERROR in reading the file. The program terminates.")
    else:
        print("Enter the following words in English:")
        uusinta = sana_koe(testi)
        while uusinta != []:
            print("Repeat the words which were incorrect:")
            uusinta = sana_koe(uusinta)

        print("Well done! The quiz terminates.")
    
main()