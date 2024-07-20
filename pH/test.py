import pandas as pd

############ EXTRACT INFO ############

#Funçao ler ficheiro:
def ler_csv(file_path):
    tabela = pd.read_excel(file_path) 
    return tabela  

############ TRANSFORMER ############


####################################### Calculo #######################################
    
#FUNCTIONS ESPI's EQUALS#
def find_espi(meu_espi, tabela):
    my_espilist=[]
  
    for column,row in tabela.iterrows():
        my_dic={}
        if row["ESPI"] == meu_espi:
           my_dic['ESPI'] = int (row['ESPI'])
           my_dic['Initial volume'] = int (row['Initial volume'])
           my_dic['Initial PH'] = float (row['Initial PH'])
           my_dic['Base to add'] = int (row['Base to add'])
           my_dic['Acid to add'] = int (row['Acid to add'])
           my_dic['Final PH'] = float (row['Final PH'])
           my_espilist.append(my_dic)
    return my_espilist

#FUNCTIONS VOLUMES EQUALS#
def find_volume(volume, my_list):
    my_volumelist=[]
    for dic in my_list:
        my_dicvolume={}
        if dic ['Initial volume'] == volume:
            my_dicvolume['ESPI'] = int (dic['ESPI'])
            my_dicvolume['Initial volume'] = int (dic['Initial volume'])
            my_dicvolume['Initial PH'] = float (dic['Initial PH'])
            my_dicvolume['Base to add'] = int (dic['Base to add'])
            my_dicvolume['Acid to add'] = int (dic['Acid to add'])
            my_dicvolume['Final PH'] = float (dic['Final PH'])
            my_volumelist.append(my_dicvolume)
    return my_volumelist

#FUNCTIONS INIIAL pH EQUALS#
def find_initialph(phinicial, ):
    pass



################### START BUTTON ################## 
#READ FILE#
def main():
    df = ler_csv (r'Tec_ph_test.xlsx')
    print(df)

#QUESTIONS#
    meu_espi = int(input("Qual é o ESPI morcão?"))
    volume = int(input("Volume Inicial?"))
    phinicial = float(input("pH Inicial?"))

#FUNCTIONS#    
    #ESPI's EQUALS#
    linhas_iguais = find_espi(meu_espi, df)
    print(linhas_iguais)
    #VOLUMES EQUALS#
    volume_igual = find_volume(volume, linhas_iguais)
    print(volume_igual)
   
    #INIIAL pH EQUALS#
    initial_ph = find_initialph(phinicial, volume_igual)
    print(initial_ph)


main ()
