import csv as csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as p
import sys

df = pd.read_csv\
('C:\Users\Alper\Desktop\BIdatachallenge\data_recruiting_bi_data_challenge.csv')

#df['clicks'].plot()

null_click = df['clicks'].isnull()
null_price = df['avg_price_hotel'].isnull()
null_rating = df['rating'].isnull()
null_partners = df['nmbr_partners_index'].isnull()
null_saving = df['avg_rel_saving'].isnull()
null_rank = df['avg_rank'].isnull()

#getting rid of null data in each and every column to prepare
#data for training

train_raw = df[(null_click | null_price | null_rating | \
         null_partners | null_saving | null_rank) == False]




#clicks = df[['clicks']]

#print pd.DataFrame(train_raw)


    
