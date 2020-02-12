'''
Created on 12 Oct 2018

@author: juan
'''



def calculate_daily_pay(daily_hours, hourly_wages):
    if 0 <= daily_hours <= 8:
        paivapalkka = daily_hours * float(hourly_wages)
    if 8 < daily_hours <= 10:
        paivapalkka = float((8.0 * float(hourly_wages)) + ((daily_hours - 8.0) * float(hourly_wages)) * 1.5)
    if daily_hours > 10:
        paivapalkka = ((daily_hours - 10.0) * float(hourly_wages) * 2.0) + (8.0 * float(hourly_wages)) + (10.0 - 8.0) * float(hourly_wages) * 1.5 
    return paivapalkka

    
    
def read_hours():
    lista = []
    print("Enter the working hours. Stop by giving a negative value.")
    daily_hours = float(input("Enter the working hours of the 1st worker:\n"))
    if daily_hours >= 0:
        lista.append(daily_hours)
    else:
        return False
    while daily_hours >= 0:
        daily_hours = float(input("Enter the working hours of the next worker:\n"))
        if daily_hours >= 0:
            lista.append(daily_hours)
    return lista
    
    
def calculate_wages(hours, hourly_wages):
    i = 0
    lista2 = []
    h = len(hours)
    while i < h:
        daily_hours =hours[i]
        paivapalkka = calculate_daily_pay(daily_hours, hourly_wages)
        lista2.append(paivapalkka)
        i += 1
    return lista2

    

def calculate_average(wages_list):
    p = len(wages_list)
    average1 = sum(wages_list) / p
    return average1
    
    
    
def wages_out_of_interval(wages_list, lower_limit, upper_limit):
    z = 0
    for paivapalkka in wages_list:
        if lower_limit > paivapalkka or paivapalkka > upper_limit:
            z += 1
    return z
            
    
    
def output_wages(wages_list):
    print("Wages:")
    for paivapalkka in wages_list:
        print("{:.2f} eur".format(paivapalkka))
    
    
def main():
    hourly_wages = float(input("Enter the hourly wages in euros:\n"))
    hours = read_hours()
    if hours == False:
        print("No working hours were entered.")
    else:
        wages_list = calculate_wages(hours, hourly_wages)
        output_wages(wages_list)
        average1 = calculate_average(wages_list)
        print("The average wage is {:.2f} eur.".format(average1))
        min1 = average1 * 0.75
        max1 = average1 * 1.25
        ulk= wages_out_of_interval(wages_list, min1, max1)
        print("The number of the wages that differs over 25 % from the average is {:d}.".format(ulk))
    
    
    
    
    
    
    
    
    
    
    
    
    
main()