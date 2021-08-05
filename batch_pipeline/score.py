# windows users
# %%writefile $experiment_folder\score.py

import os
from io import StringIO

import joblib
import numpy as np
from azureml.core import Model


def init():
    # Runs when the pipeline step is initialized
    global model

    # load the model
    # model_path = Model.get_model_path('naive_model')
    # model = joblib.load(model_path)


def run(mini_batch):
    # This runs for each batch
    resultList = []

    # process each file in the batch
    for f in mini_batch:
        # Read comma-delimited data into an array
        data = pd.read_csv(f, delimiter=",")
        # Reshape into a 2-dimensional array for model input
        prediction = (
            data.groupby("dayofweek")
            .rolling(3, closed="left")
            .mean()
            .reset_index()
            .sort_values(by="data_index_")
            .set_index("data_index_")
        ).rename(columns={"load_actuals_mw": "load_pred_mw"})
        # Append prediction to results
        resultList.append(
            "{}: {}".format(os.path.basename(f), prediction["load_pred_mw"].iloc[-7:])
        )
    return resultList
