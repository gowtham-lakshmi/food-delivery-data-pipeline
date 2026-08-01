import pandas as pd
df = pd.read_csv('raw_food_delivery_data.csv')
print(df)
print(df.shape)
print(df.isnull().sum())
df['city']=df['city'].fillna('unknown')
print(df['city'].isnull().sum())
df['payment_method']=df['payment_method'].fillna('unknown')
print(df['payment_method'].isnull().sum())
df['customer_rating']=df['customer_rating'].fillna(df['customer_rating'].median())
print(df['customer_rating'].isnull().sum())
print(df.isnull().sum())

df=df.drop_duplicates()
print(df.shape)

df['city']=df['city'].str.strip().str.title()
df['cuisine_type']=df['cuisine_type'].str.strip().str.title()
df['delivery_status']=df['delivery_status'].str.strip().str.title()

print(df['city'].unique())
print(df['cuisine_type'].unique())
print(df['delivery_status'].unique())

df.to_csv('cleaned_food_delivery_data.csv', index=False)