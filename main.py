import pandas as pd

data_dict = {
	'CareerYear': ['2008', '2009', '2010', '2011', '2012', '2013'],
	'FirstPlace': ['Quinn Leila', 'Zeke Goodwin', 'Perce Mercy', 'Alf Edythe', 'Marley Gemma', 'Bob Estella'],
	'SecondPlace': ['Aric Jarvis', 'Abbi Emalee', 'Abbi Emalee', 'Pauline Arline', 'Zeke Goodwin', 'Ethelbert Kairo'],
	'ThirdPlace': ['Myron Calanthia', 'Aric Jarvis', 'Zeke Goodwin', 'Ethelbert Kairo', 'Bob Estella', 'Marley Gemma']
}

def create_dataset():
    """
    """
    df = pd.DataFrame(data_dict)
    return df

def main(df):
    """
    """
    final_df = pd.DataFrame()
    final_df[['First','Second','Third']] = df[['FirstPlace', 'SecondPlace', 'ThirdPlace']].apply(pd.Series.value_counts).fillna(0).astype(int)
    return final_df

df = create_dataset()
final_df = main(df)
print(df)
print(final_df)
