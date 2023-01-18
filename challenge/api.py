"""API endpoints of the hiring challenge."""

from io import BytesIO

import pandas as pd
from fastapi.applications import FastAPI
from fastapi.param_functions import File

app = FastAPI()


@app.post("/genres/train")
def train(file: bytes = File(...)) -> None:
    """Train a predictive model to rank movie genres based on their synopsis."""
    df = pd.read_csv(BytesIO(file))
    print(df)

    # TODO:
    #  - Create a model
    #  - Train the model on the received data
    #  - Save the model
    raise NotImplementedError


# TODO:
#  - Create a '/genres/predict' endpoint (POST)
#  - Load in the previously trained model
#  - Make predictions on the received data (ranked by likelihood)
#  - Return your predictions as a dictionary of the following format:
#       {
#           <movie_id>: {
#               0: <first-prediction>,
#               1: <second-prediction>,
#               2: <third-prediction>,
#               3: <fourth-prediction>,
#               4: <fifth-prediction>,
#           },
#           ...
#       }
