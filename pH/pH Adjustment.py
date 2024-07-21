import pandas as pd

############################################# EXTRACT INFO ##############################################


def ler_csv(file_path:str)->pd.DataFrame:
    """
    This funtion is responsible to read the file and return the data in a DataFrame format.
    To that the function receives the file path in string format and returns the data.
    Args:
        file_path (str): path to the excel file

    Returns:
        pd.Dataframe: complete dataframe with the data
    """

    data = pd.read_excel(file_path) 
    return data  


def generate_table(data:list[dict])->pd.DataFrame:
    """
    Function responsible to generate a table with the data present in a given list of dictionaries.
    Args:
        data (list[dict]): given data

    Returns:
        pd.DataFrame: data in a dataframe format
    """
    return pd.DataFrame(data)

def get_espi():
    try:
        #QUESTIONS#
        my_espi = int(input("\nQual é o ESPI? (int)"))
    except ValueError:
        print("#### !!!Invalid input for espi morcão, put a int value!!! ####")
        exit(1)
    return my_espi

def get_volume():
    try:
        #QUESTIONS#
        my_volume = int(input("\nVolume Initial? (int)"))
    except ValueError:
        print("#### !!!Invalid input for volume morcão, put a int value!!! ####")
        exit(1)
    return my_volume

def get_ph():
    try:
        #QUESTIONS#
        my_phinitial = float(input("\npH Initial? (float)"))
    except ValueError:
        print("#### !!!Invalid input for PH morcão, put a float value!!! ####")
        exit(1)
    return my_phinitial

####################################### FUNCTIONS DATA PROCESSING #######################################
    

def find_espi(my_espi:int, data:pd.DataFrame):
    """
    Funtion responsible to get a given ESPI and return the data related to it in a list of dictionaries.
    Args:
        my_espi (int): given ESPI 
        data (pd.DataFrame): data extracted from the excel file

    Returns:
        list: list of dictionaries with the data related to the given ESPI
    """
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
    
    if my_espilist == []:
        return False
    else:
        return my_espilist

#FUNCTION VOLUMES EQUALS#
def find_volume(my_volume:int, my_list:list[dict]):
    """
    Funtion responsible to get a given volume and return the data related to it in a list of dictionaries.
    Args:
        my_volume (int): given Volume to filter data
        my_list (list[dict]):  list of dictionaries with the data related filtered by ESPI

    Returns:
        list[dict]: list of dictionaries with the data filtered by ESPI and  Volume
    """
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
    if my_volumelist == []:
        return False
    else:
        return my_volumelist

#FUNCTION INITIAL pH EQUALS#
def find_initialph(my_phinitial:float, my_list:list[dict]):
    """
    Funtion responsible to get a given initial PH and return the data related to it in a list of dictionaries.
    Args:
        my_phinitial (int): given Initial PH to filter data
        my_list (list[dict]):  list of dictionaries with the data related filtered by ESPI and Volume

    Returns:
        list[dict]: list of dictionaries with the data filtered by ESPI, Volume and Initial PH
    """
    my_phinitiallist=[]
    for dic in my_list:
        my_dicphinitial={}
        if dic ['Initial PH'] == my_phinitial:
            my_dicphinitial['ESPI'] = int (dic['ESPI'])
            my_dicphinitial['Initial volume'] = int (dic['Initial volume'])
            my_dicphinitial['Initial PH'] = float (dic['Initial PH'])
            my_dicphinitial['Base to add'] = int (dic['Base to add'])
            my_dicphinitial['Acid to add'] = int (dic['Acid to add'])
            my_dicphinitial['Final PH'] = float (dic['Final PH'])
            my_phinitiallist.append(my_dicphinitial)
    
    if my_phinitiallist == []:
        return False
    else:
        return my_phinitiallist
    




def handle_pipeline(df:pd.DataFrame):
    #ESPI EQUALS#
    my_espi = get_espi()
    espi = find_espi(my_espi, df)

    if espi:
        staging_table = generate_table(espi)
        my_volume = get_volume()
        #VOLUMES EQUALS#
        volume_igual = find_volume(my_volume, espi)
        if volume_igual:
            my_phinitial = get_ph()
            #INIIAL pH EQUALS#
            staging_table = generate_table(volume_igual)
            initial_ph = find_initialph(my_phinitial, volume_igual)
            if initial_ph:
                staging_table = generate_table(initial_ph)
            else:
                print("Initial pH not found, ending search and" 
                      "presenting results for ESPI and Volume")
                
        else:
            print("----------------------------------------"
              "\nVolume not found, searching for Initial PH")
            my_phinitial = get_ph()
            initial_ph = find_initialph(my_phinitial, espi)
            if initial_ph:
                staging_table = generate_table(initial_ph)
            else:
                print("\nInitial pH not found ending search and" 
                      "presenting results for ESPI")

        return staging_table
    
    else:
        print("----------------------------------------"
              "\nESPI not found morcão, try another one")
        exit(1)


########################################## START BUTTON ##############################################

def main():
    """
    Main function responsible to start the program
    """
    df = ler_csv (r'pH/Tec_ph_test.xlsx')
    print(df.head(10))
    
    
    #PIPELINE#
    result = handle_pipeline(df)

    print(f"\nThis are the Results: \n{result}")
    
        



if __name__ == "__main__":
    main()