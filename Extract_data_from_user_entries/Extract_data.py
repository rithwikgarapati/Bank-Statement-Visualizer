import pandas as pd
import re

def process_description(description: str):
    """
        - This function extracts 
            1. City
            2. State 
            3. Main keywords of description
        
        - Returns (city, state, cleaned_desc)
    """
    description = description.split(' ')[4 : ]
    description = [item.strip() for item in description if item.strip()]
    
    city = description[-2]
    state = description[-1]
    
    if len(state) > 2:
        city += state[:-2]
        state = state[-2:]
    
    description = (' '.join(description[ : -2]))

    # Remove un-necessary prefixes.
    cleaned = re.sub(r'^(SQ \*|BYT\*|TST\*|POS|CARD|ATM)\s*', '', description)
    
    return (city, state, cleaned)
    
    

def read_csv( file_name ):
    """
        - Read the csv file of credit card statements
          and extract necessary data.
    """
    transactions = []

    df = pd.read_csv(file_name)

    for _, row in df.iterrows():
        description = row['Extended Description']
        amount = row['Amount']
        
        city, state, main_desc = process_description(description)
        
        trans = {
            'description' : main_desc,
            'amount' : amount,
            'city' : city,
            'state' : state,
            'type' : 'spending' if amount < 0 else 'earning'
        }

        transactions.append(trans)
    
    return transactions


def main():
    transactions = read_csv('Get_Data/credit_card_transactions.csv')

    for trans in transactions:
        print(trans)

if __name__ == '__main__':
    main()




    