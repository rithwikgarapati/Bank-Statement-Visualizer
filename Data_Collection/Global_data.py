import pandas as pd


def add_category(df, category):
    df['category'] = category
    return df


def select_columns(df, column_names):
    new_df = df.loc[:, column_names]
    return new_df

def process_grocery(file_name):
    df = pd.read_csv(file_name)
    df2 = df.drop_duplicates('name')
    column_names = ['name']
    new_df = select_columns(df2, column_names)
    new_df = add_category(new_df, 'Groceries & Essentials')
    new_df.to_csv('Processed_Data/Grocery_data.csv', index=False)


def main():
    process_grocery('Data_Collection/food_retailers.csv')
    
    

main()