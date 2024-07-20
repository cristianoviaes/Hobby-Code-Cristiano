import pandas as pd

############################################# EXTRACT INFO ##############################################

#READ FILE:
def ler_csv(file_path):
    data = pd.read_excel(file_path) 
    return data  

####################################### FUNCTIONS DATA PROCESSING #######################################
    
#FUNCTION ESPI's EQUALS#
def find_espi(my_espi, data):
    my_espilist=[]
  
    for column,row in data.iterrows():
        my_dic={}
        if row["ESPI"] == my_espi:
           my_dic['ESPI'] = int (row['ESPI'])
           my_dic['Initial volume'] = int (row['Initial volume'])
           my_dic['Initial PH'] = float (row['Initial PH'])
           my_dic['Base to add'] = int (row['Base to add'])
           my_dic['Acid to add'] = int (row['Acid to add'])
           my_dic['Final PH'] = float (row['Final PH'])
           my_espilist.append(my_dic)
    return my_espilist

#FUNCTION VOLUMES EQUALS#
def find_volume(my_volume, my_list):
    my_volumelist=[]
    for dic in my_list:
        my_dicvolume={}
        if dic ['Initial volume'] == my_volume:
            my_dicvolume['ESPI'] = int (dic['ESPI'])
            my_dicvolume['Initial volume'] = int (dic['Initial volume'])
            my_dicvolume['Initial PH'] = float (dic['Initial PH'])
            my_dicvolume['Base to add'] = int (dic['Base to add'])
            my_dicvolume['Acid to add'] = int (dic['Acid to add'])
            my_dicvolume['Final PH'] = float (dic['Final PH'])
            my_volumelist.append(my_dicvolume)
    return my_volumelist

#FUNCTION INITIAL pH EQUALS#
def find_initialph(my_phinitial, my_list):
    my_phinitiallist=[]
    for dic in my_list:
        my_dicphinitial={}
        if dic ['Initial volume'] == my_phinitial:
            my_dicphinitial['ESPI'] = int (dic['ESPI'])
            my_dicphinitial['Initial volume'] = int (dic['Initial volume'])
            my_dicphinitial['Initial PH'] = float (dic['Initial PH'])
            my_dicphinitial['Base to add'] = int (dic['Base to add'])
            my_dicphinitial['Acid to add'] = int (dic['Acid to add'])
            my_dicphinitial['Final PH'] = float (dic['Final PH'])
            my_phinitiallist.append(my_dicphinitial)
    return my_phinitiallist

########################################## START BUTTON ##############################################
#READ FILE#
def main():
    df = ler_csv (r'Tec_ph_test.xlsx')
    print(df)

#QUESTIONS#
    my_espi = int(input("Qual é o ESPI?"))
    my_volume = int(input("Volume Initial?"))
    my_phinitial = float(input("pH Initial?"))

#FUNCTIONS#    
    #ESPI's EQUALS#
    espi = find_espi(my_espi, df)
    print(espi)

    #VOLUMES EQUALS#
    volume_igual = find_volume(my_volume, espi)
    print(volume_igual)

    #INIIAL pH EQUALS#
    initial_ph = find_initialph(my_phinitial, volume_igual)
    print(initial_ph)


main ()