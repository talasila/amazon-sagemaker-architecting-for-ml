import pandas as pd
from sklearn.utils import shuffle

def main(f_name):
    
    df = pd.read_csv(f_name, index_col = "ID")
    paysim_df = pd.read_csv(f_name)
    
    # Reduce number of columns
    # dropping nameDest and nameOrig
    
    paysim_df_reduced=paysim_df.drop(columns=['nameDest','nameOrig'])

    #shuffle the data 
    paysim_df_shuffled=shuffle(paysim_df_reduced)


    types_of_payments = ["CASH_OUT", "PAYMENT", "CASH_IN", "TRANSFER", "DEBIT"]

    #Create a dicitionary for payments type
    payment_dict = get_payment_dict(types_of_payments)   
    

    hot_encoded_df = replace_type_with_id(paysim_df_shuffled, payment_dict)
    final_df = hot_encoded_df.drop(['type'], axis=1)


    
    # write to disk
    final_df.to_csv("../paysim_shuffled_hotencoded.csv")


def get_payment_dict(payment_list):
    rt = {}
    for idx, payment in enumerate(payment_list):
        rt[payment] = idx
    return rt

def replace_type_with_id(df, payment_dict):
    
    df["typeMap"] = [0 for i in range(df.shape[0])]
    
    for idx, row in df.iterrows():
        c = row["type"]
        c_id = payment_dict[c]
        df.at[idx, "typeMap"] = c_id        
    return df

if __name__ == "__main__":

    main("./../testdata/test.csv")   

