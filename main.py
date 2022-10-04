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

def main():
    """
    """


df = create_dataset()
print(df)
