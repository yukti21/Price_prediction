import pickle
from tkinter import *
import numpy as np
import pandas as pd
from tkinter import messagebox
import sqlite3
con = sqlite3.connect('predidb1.db')
cur = con.cursor()
f = ('Times', 14)
f1 = ('Times', 19)
f2 = ('Times', 11)
import pandas as pd
import sqlite3
import sqlalchemy
ws = Tk()
ws.title('User Input')
ws.geometry('300x300')
ws.config(bg='#097969')
from sklearn.preprocessing import StandardScaler


# Creating function for scaling
def standard_scaler(df, col_names):
    features = df[col_names]
    scaler = StandardScaler().fit(features.values)
    features = scaler.transform(features.values)
    df[col_names] = features
    return df


col_names = ['Total Volume', '4046', '4225', '4770', 'Total Bags']

def predict(Total_Volume, small, medium, large, Total_Bags, Type, year, month, region):
    data = [Total_Volume, small, medium, large, Total_Bags, Type, year, month]
    regions = ['region_Albany',
               'region_Atlanta', 'region_BaltimoreWashington', 'region_Boise',
               'region_Boston', 'region_BuffaloRochester', 'region_California',
               'region_Charlotte', 'region_Chicago', 'region_CincinnatiDayton',
               'region_Columbus', 'region_DallasFtWorth', 'region_Denver',
               'region_Detroit', 'region_GrandRapids', 'region_GreatLakes',
               'region_HarrisburgScranton', 'region_HartfordSpringfield',
               'region_Houston', 'region_Indianapolis', 'region_Jacksonville',
               'region_LasVegas', 'region_LosAngeles', 'region_Louisville',
               'region_MiamiFtLauderdale', 'region_Midsouth', 'region_Nashville',
               'region_NewOrleansMobile', 'region_NewYork', 'region_Northeast',
               'region_NorthernNewEngland', 'region_Orlando', 'region_Philadelphia',
               'region_PhoenixTucson', 'region_Pittsburgh', 'region_Plains',
               'region_Portland', 'region_RaleighGreensboro', 'region_RichmondNorfolk',
               'region_Roanoke', 'region_Sacramento', 'region_SanDiego',
               'region_SanFrancisco', 'region_Seattle', 'region_SouthCarolina',
               'region_SouthCentral', 'region_Southeast', 'region_Spokane',
               'region_StLouis', 'region_Syracuse', 'region_Tampa', 'region_TotalUS',
               'region_West', 'region_WestTexNewMexico']
    print(month)
    if (month == 8):
        print(8)
    if (month == 3 or 4 or 5):
        data.extend([1, 0, 0, 0])
    elif (month == 6 or 7 or 8):
        print('True')
        data.extend([0, 1, 0, 0])
    elif (month == 9 or 10 or 11):
        data.extend([0, 0, 1, 0])
    elif (month == 12 or 1 or 2):
        data.extend([0, 0, 0, 1])
    index = 0
    arr = np.zeros(54)
    for i in range(len(regions)):
        if (regions[i][7:] == region):
            index = i
            break
    arr[index] = 1
    l = arr.tolist()
    data.extend(l)
    print(data)
    df = pd.DataFrame(data=[data], columns=['Total Volume', '4046', '4225', '4770', 'Total Bags', 'type', 'year',
                                            'month', 'Spring', 'Summer', 'Fall', 'Winter', 'region_Albany',
                                            'region_Atlanta', 'region_BaltimoreWashington', 'region_Boise',
                                            'region_Boston', 'region_BuffaloRochester', 'region_California',
                                            'region_Charlotte', 'region_Chicago', 'region_CincinnatiDayton',
                                            'region_Columbus', 'region_DallasFtWorth', 'region_Denver',
                                            'region_Detroit', 'region_GrandRapids', 'region_GreatLakes',
                                            'region_HarrisburgScranton', 'region_HartfordSpringfield',
                                            'region_Houston', 'region_Indianapolis', 'region_Jacksonville',
                                            'region_LasVegas', 'region_LosAngeles', 'region_Louisville',
                                            'region_MiamiFtLauderdale', 'region_Midsouth', 'region_Nashville',
                                            'region_NewOrleansMobile', 'region_NewYork', 'region_Northeast',
                                            'region_NorthernNewEngland', 'region_Orlando', 'region_Philadelphia',
                                            'region_PhoenixTucson', 'region_Pittsburgh', 'region_Plains',
                                            'region_Portland', 'region_RaleighGreensboro', 'region_RichmondNorfolk',
                                            'region_Roanoke', 'region_Sacramento', 'region_SanDiego',
                                            'region_SanFrancisco', 'region_Seattle', 'region_SouthCarolina',
                                            'region_SouthCentral', 'region_Southeast', 'region_Spokane',
                                            'region_StLouis', 'region_Syracuse', 'region_Tampa', 'region_TotalUS',
                                            'region_West', 'region_WestTexNewMexico'])
    df = standard_scaler(df, col_names)
    model = pickle.load(open('model_xgboost.pkl', 'rb'))
    print(df)
    prediction = model.predict(df)

    return prediction

def predict_comand():
    try:
        conn = sqlite3.connect(r'predidb1.db')
    except Exception as e:
        print(e)

    # Now in order to read in pandas dataframe we need to know table name
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(f"Table Name : {cursor.fetchall()}")

    df = pd.read_sql_query('SELECT * FROM Record', conn)
    conn.close()
    i = len(df) - 1
    Total_Volume = df.iat[i, 0]
    small = df.iat[i, 1]
    medium = df.iat[i, 2]
    large = df.iat[i, 3]
    Total_Bags = df.iat[i,4]
    Type = df.iat[i,5]
    year = df.iat[i, 6]
    month = df.iat[i, 7]
    region = df.iat[i,8]
    x = predict(Total_Volume, small, medium, large, Total_Bags, Type, year, month, region)
    return x

ans = predict_comand()
right_frame = Frame(
    ws,
    bd=2,
    bg='#AFE1AF',
    relief=SOLID,
    padx=10,
    pady=10
)
Label(
    right_frame,
    text="Avacado price prediction",
    bg='#AFE1AF',
    font=f1
).grid(row=0, column=0, pady=10)

Label(
    right_frame,
    text="The price of avacado for given data is:",
    bg='#AFE1AF',
    font=f2
).grid(row=1, column=0, pady=10)



Label(
    right_frame,
    text=ans[0],
    bg='#AFE1AF',
    font=f1
).grid(row=3, column=0, rowspan=2, pady=10)
right_frame.place(x=12, y=50, )

ws.mainloop()