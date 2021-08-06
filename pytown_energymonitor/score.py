
import os
import pandas as pd

def init():
    # Runs when the pipeline step is initialized
    global model


def get_classification(df_pred, col_energy, col_prediction):
    df_pred['difference'] = df_pred[col_energy] - df_pred[col_prediction]
    df_pred['class'] = 0 # add a class column with 0 as low charge (1 is middle charge  and 2 is normal charge)
    df_pred.loc[df_pred['difference'] > 0, 'class'] = 1 
    df_pred.loc[df_pred['difference'] > 5000, 'class'] = 2 
    return df_pred

def run(mini_batch):
    # mini_batch is the pandas dataframe    
  
    #calculate naive forecast
    prediction_df = (
        mini_batch
        .set_index('data_index_')
        .groupby('dayofweek')
        .load_actuals_mw
        .rolling(3, closed = 'left')
        .mean()
        .reset_index()
    ).rename(columns ={'load_actuals_mw' : 'load_pred_mw'})

    df_complete = (
        pd.merge(prediction_df, mini_batch, on='data_index_')
        .drop('dayofweek_y', axis=1)
        .sort_values(by='data_index_')
        .set_index('data_index_')
    )

    return get_classification(df_complete, 'total_gen', 'load_pred_mw')

