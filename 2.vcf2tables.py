import pandas as pd
import os, os.path
import datetime 
import numpy as np
import warnings

warnings.filterwarnings('ignore')#mutes pandas fragmentation warning

def create_table(name,date,pos_list):#function to create table with number of polymorphisms each day
        column = dataframe[name].tolist()
        for index in range(len(column)):
            if column[index] > 0:
              pos = pos_list[index]
              table.at[pos,date] += 1
        table.to_pickle(f"tables/{date}.pickle")

def validate(date_text):#function to check if date has the correct format
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
            return True
        except ValueError:
            return False

def samples_per_day(date):#function to count number of samples each day
    if os.path.exists("tables/samples.pickle"):
        dates_table = pd.read_pickle("tables/samples.pickle")
        if date in dates_table:
            dates_table[date] += 1
        else:
            dates_table[date] = 1
        dates_table.to_pickle("tables/samples.pickle")
    else:
       dates_table = pd.DataFrame(1, index=["n_samples"], columns=[date])
       dates_table.to_pickle("tables/samples.pickle")

def sort_by_date(table):#function to sort table with samples number by date
    dates_table = pd.read_pickle(table)
    dates_table_t = dates_table.transpose()
    dates_table_t.index = pd.to_datetime(dates_table_t.index)
    dates_table_t = dates_table_t.sort_index()
    dates_table = dates_table_t.transpose()
    return dates_table

os.system("mkdir -p tables")#creates tables folder to put inside the variation tables of each day
for vcf in os.listdir("vcf"):#for loop to apply the above functions and create the tables with the number of polymorphisms for each day
    with open(f"vcf/{vcf}") as f:
        for i in range(3):
            f.readline()
        header = f.readline().replace("\n","")
    header = header.replace("#","").split("\t")

    dataframe = pd.read_csv(f"vcf/{vcf}",comment='#',sep="\t",header=None,names=header)
    pos_list = dataframe["POS"].tolist()
    names = header[10:]
    dataframe = dataframe.iloc[:,10:]
    for name in names:
        date = name.split("|")[2]
        if validate(date):
            samples_per_day(date)
            if os.path.exists(f"tables/{date}.pickle"):
              table = pd.read_pickle(f"tables/{date}.pickle")
              create_table(name,date,pos_list) 
            else:
              table = pd.DataFrame(0, np.arange(1,29904), columns=[date])
              create_table(name,date,pos_list)

dates_list = sort_by_date("tables/samples.pickle").iloc[0])#sorts sample table by date and creates a list of it

days = [x.replace(".pickle","") for x in os.listdir("tables")]
days.remove("samples")
sorteddates = sorted(days, key=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
table = pd.DataFrame(0, index=np.arange(1,29904), columns=["to_remove"])
for day in sorteddates:
    pickle = pd.read_pickle(f"tables/{day}.pickle")
    table = pd.concat([table,pickle],axis=1)#enwnei oles tis hmeromhnies se mia
table = table.iloc[: , 1:]#vgazei thn to_remove

norm_table = table/dates_list
norm_table.to_csv("total_variant_norm.csv")