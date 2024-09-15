import pandas as pd

def read_csv( file_name ):
    """
        - Read the csv file of credit card statements
          and extract necessary data.
    """
    transactions = []

    df = pd.read_csv(file_name)
    df.columns = df.columns.str.replace(' ', '_')

    for row in df.itertuples():
        description = row.Extended_Description
        amount = row.Amount

        description = description.split(' ')[4 : ]
        description = ' '.join(description)

        trans = {
            'description' : description,
            'amount' : amount,
        }

        transactions.append(trans)
    
    return transactions


def main():
    transactions = read_csv('Get_Data/credit_card_transactions.csv')

    for trans in transactions:
        print(trans)

if __name__ == '__main__':
    main()




    