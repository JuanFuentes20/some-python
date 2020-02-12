'''
Created on 27 Oct 2018

@author: juan
'''
def read_names():
    print("Input the names of the participants.")
    print("Stop by entering an empty line.")
    nimikirja = {}
    rivi = input()
    while len(rivi) > 0:
        nimi = rivi
        nimikirja[nimi] = 0.0
        rivi = input("")
    return nimikirja

def add_costs(cost_statistics):
    print("Next, the information about costs are added.")
    print("Stop by entering an empty line as a name.")
    print("Enter the name of the participant.\n")
    nimi = input()
    while len(nimi) > 0:
        if nimi in cost_statistics:
            print("Enter the amount to be added.")
            raha = float(input(""))
            if raha < 0:
                print("Negative amounts are not added.")
                print("Enter the name of the participant.\n")
                nimi = input("")
            else:
                cost_statistics[nimi] += raha
                print("Enter the name of the participant.\n")
                nimi = input("")
        else:
            print("This name is not among the participants.")
            print("Enter the name of the participant.\n")
            nimi = input("")
        
    print("Information about costs stored.")  
    return cost_statistics

def calculate_average(cost_statistics):
    summa = 0
    p = len(cost_statistics)
    tyhja = 0.0
    if p > 0:
        for nimi in cost_statistics:
            summa += cost_statistics[nimi]
        keskiarvo = summa / p
        return keskiarvo
    else:
        return tyhja

def list_totals(cost_statistics):
    print("Total sums paid:")
    for nimi in sorted(cost_statistics):
        print("{:15s} {:.2f} eur.".format(nimi, cost_statistics[nimi]))
        
def list_debts(cost_statistics):
    keskiarvo = float(calculate_average(cost_statistics))
    for nimi in sorted(cost_statistics):
        if cost_statistics[nimi] < keskiarvo:
            maksettava = keskiarvo - cost_statistics[nimi]
            print("{:s} should pay {:.2f} eur.".format(nimi, maksettava))
        elif cost_statistics[nimi] > keskiarvo:
            saatava = cost_statistics[nimi] - keskiarvo
            print("{:s} should receive {:.2f} eur.".format(nimi, saatava))
        elif cost_statistics[nimi] == keskiarvo:
            tasa = 0.00
            print("{:s} should receive {:.2f} eur.".format(nimi, tasa))
            


def main():
    print("Hello again!\n")
    cost_statistics = read_names()
    add_costs(cost_statistics)
    print("\n")
    calculate_average(cost_statistics)
    list_totals(cost_statistics)
    print("\n")
    list_debts(cost_statistics)
    print("The program ends.")

main()
        
        
        
