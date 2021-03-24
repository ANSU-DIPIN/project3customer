# Importing essential libraries
#import numpy as np
import pandas as pd
import pickle
import warnings
warnings.filterwarnings("ignore")

# Loading the dataset
df_ = pd.read_excel('Retail-Ecommerce.xlsx', sheet_name='Online Retail') 
df1 = df_.copy()
df2 = df1.drop(df1[ (df1['CustomerID'].isna()) & (df1['UnitPrice']==0.0)].index)
# impute function
def impute_nan(cols):
    CustomerID = cols[0]
    Country = cols[1]
    if pd.isnull(CustomerID):
        if Country == 'United Kingdom':
            return 17841.0
        elif Country == 'EIRE':
            return 14911.0
        elif Country == 'Bahrain':
            return 12355.0
        elif Country == 'Israel':
            return 12688.0
        elif Country == 'Hong Kong':
            return 99999.0
        elif Country == 'Unspecified':
            return 12743.0
        elif Country == 'France':
            return 12681.0
        elif Country == 'Switzerland':
            return 12451.0
        elif Country == 'Portugal':
            return 12757.0
        else:
            return 0
    else:
        return CustomerID
df2['CustomerID'] = df2[['CustomerID','Country']].apply(impute_nan,axis=1)
df3 = df2.drop_duplicates()
df4= df3.drop(df3[(df3['Quantity'] >= 40000) | (df3['Quantity'] <= -60000)].index)
df5= df4.drop(df4[(df4['UnitPrice'] >= 11061) | (df4['UnitPrice'] <= -10000)].index)
df5a= df5.drop(df5[(df5['Quantity'] < 0) | (df5['InvoiceNo'].astype(str).str.contains('C'))].index)
TotalAmount = df5a['Quantity'] * df5a['UnitPrice']
df5a.insert(loc=5,column='TotalAmount',value=TotalAmount)
df6 = df5a[['CustomerID','InvoiceNo','StockCode','Description', 'Quantity', 'UnitPrice','TotalAmount','InvoiceDate','Country']]

df9 = df6.copy()

from datetime import datetime
df9['InvoiceDate'] = pd.to_datetime(df9['InvoiceDate'])

df_11m = df9.loc[(df9['InvoiceDate'] < datetime.strptime('2011,11,09', '%Y,%m,%d')) & (df9['InvoiceDate'] >= datetime.strptime('2010,12,1', '%Y,%m,%d'))].reset_index(drop=True)
df_next = df9.loc[(df9['InvoiceDate'] >= datetime.strptime('2011,11,09', '%Y,%m,%d')) & (df9['InvoiceDate'] < datetime.strptime('2011,12,9', '%Y,%m,%d'))].reset_index(drop=True)

df_user = pd.DataFrame(df_11m['CustomerID'].unique())
df_user.columns = ['CustomerID']

purchase1 = df_next.groupby('CustomerID').InvoiceDate.min().reset_index()
purchase1.columns = ['CustomerID','MinPurchaseDate']

purchase2 = df_11m.groupby('CustomerID').InvoiceDate.max().reset_index()
purchase2.columns = ['CustomerID','MaxPurchaseDate']

purchase = pd.merge(purchase2,purchase1,on='CustomerID',how='left')
purchase['DayDiff'] = (purchase['MinPurchaseDate'] - purchase['MaxPurchaseDate']).dt.days
df_user = pd.merge(df_user, purchase[['CustomerID','DayDiff']],on='CustomerID',how='left')
df_user = df_user.fillna(999)
#Recency
max_purchase = df_11m.groupby('CustomerID').InvoiceDate.max().reset_index()
max_purchase.columns = ['CustomerID','MaxPurchaseDate']
max_purchase['Recency'] = (max_purchase['MaxPurchaseDate'].max() - max_purchase['MaxPurchaseDate']).dt.days
df_user = pd.merge(df_user, max_purchase[['CustomerID','Recency']], on='CustomerID')

from sklearn.cluster import KMeans
#Recency Cluster
kmeans = KMeans(n_clusters=4) # select the number of clusters as 4 
kmeans.fit(df_user[['Recency']])
df_user['RecencyCluster'] = kmeans.predict(df_user[['Recency']])
def order_cluster(cluster_field_name, target_field_name,df,ascending):
    new_cluster_field_name = 'new_' + cluster_field_name
    df_new = df.groupby(cluster_field_name)[target_field_name].mean().reset_index()
    df_new = df_new.sort_values(by=target_field_name,ascending=ascending).reset_index(drop=True)
    df_new['index'] = df_new.index
    df_final = pd.merge(df,df_new[[cluster_field_name,'index']], on=cluster_field_name)
    df_final = df_final.drop([cluster_field_name],axis=1)
    df_final = df_final.rename(columns={"index":cluster_field_name})
    return df_final
df_user = order_cluster('RecencyCluster', 'Recency',df_user,False)
#Frequency
df_frequency = df_11m.groupby('CustomerID').InvoiceDate.count().reset_index()
df_frequency.columns = ['CustomerID','Frequency']
df_user = pd.merge(df_user, df_frequency, on='CustomerID')

#Frequency cluster
kmeans = KMeans(n_clusters=4)
kmeans.fit(df_user[['Frequency']])
df_user['FrequencyCluster'] = kmeans.predict(df_user[['Frequency']])
df_user = order_cluster('FrequencyCluster', 'Frequency',df_user,True)
#monetary value
df_11m.rename(columns={"TotalAmount":"Revenue"},inplace=True)
df_revenue = df_11m.groupby('CustomerID').Revenue.sum().reset_index()
df_user = pd.merge(df_user, df_revenue, on='CustomerID')

#Revenue clusters 
kmeans = KMeans(n_clusters=4)
kmeans.fit(df_user[['Revenue']])
df_user['RevenueCluster'] = kmeans.predict(df_user[['Revenue']])
df_user = order_cluster('RevenueCluster', 'Revenue',df_user,True)
#building overall segmentation
df_user['OverallScore'] = df_user['RecencyCluster'] + df_user['FrequencyCluster'] + df_user['RevenueCluster']
#assign segment names
df_user['Segment'] = 1
df_user.loc[df_user['OverallScore']>2,'Segment'] = 2 
df_user.loc[df_user['OverallScore']>4,'Segment'] = 3
 
df_day_order = df_11m[['CustomerID','InvoiceDate']]
df_day_order['InvoiceDay'] = df_11m['InvoiceDate'].dt.date
df_day_order = df_day_order.sort_values(['CustomerID','InvoiceDate'])
df_day_order = df_day_order.drop_duplicates(subset=['CustomerID','InvoiceDay'],keep='first')

df_day_order['PrevInvoiceDate'] = df_day_order.groupby('CustomerID')['InvoiceDay'].shift(1)
df_day_order['T2InvoiceDate'] = df_day_order.groupby('CustomerID')['InvoiceDay'].shift(2)
df_day_order['T3InvoiceDate'] = df_day_order.groupby('CustomerID')['InvoiceDay'].shift(3)

df_day_order['DayDiff1'] = (df_day_order['InvoiceDay'] - df_day_order['PrevInvoiceDate']).dt.days
df_day_order['DayDiff2'] = (df_day_order['InvoiceDay'] - df_day_order['T2InvoiceDate']).dt.days
df_day_order['DayDiff3'] = (df_day_order['InvoiceDay'] - df_day_order['T3InvoiceDate']).dt.days

df_day_diff = df_day_order.groupby('CustomerID').agg({'DayDiff1': ['mean','std']}).reset_index()
df_day_diff.columns = ['CustomerID', 'DayDiffMean','DayDiffStd']
df_day_order_last = df_day_order.drop_duplicates(subset=['CustomerID'],keep='last')

df_day_order_last = df_day_order_last.dropna()
df_day_order_last = pd.merge(df_day_order_last, df_day_diff, on='CustomerID')
df_user = pd.merge(df_user, df_day_order_last[['CustomerID','DayDiff1','DayDiff2','DayDiff3','DayDiffMean','DayDiffStd']], on='CustomerID')

df_class = df_user.copy()
#df_class = pd.get_dummies(df_class)
df_class['NextPurchaseDayRange'] = 0
df_class.loc[df_class.DayDiff<=31,'NextPurchaseDayRange'] = 1

df_class.to_csv('newdf.csv') 
df = pd.read_csv('newdf.csv', index_col=[0])
df_copy = df.copy(deep=True)
df_copy.drop('CustomerID',axis=1, inplace=True)

# Model Building
from sklearn.model_selection import train_test_split
X = df_copy.drop(columns='NextPurchaseDayRange')
y = df_copy['NextPurchaseDayRange']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)
# Creating the Model

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, y_train)
# Creating a pickle file for the classifier
filename = 'customerpredictionLogRegmodel.pkl'
pickle.dump(classifier, open(filename, 'wb'))