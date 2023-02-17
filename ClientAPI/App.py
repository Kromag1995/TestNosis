from flask import Flask
from math import floor

import pandas as pd

app = Flask(__name__)


@app.route("/<int:nro_cliente>")
def client(nro_cliente):
    data = {"Resultado": []}
    df = pd.read_excel("./CSV.xltx")
    result_row = df[df.NroCliente == nro_cliente]
    if result_row.empty:
        return data
    data["Resultado"].append({
        "NroCliente": int(result_row.NroCliente.values[0]),
        "Score": float(result_row.Score.values[0]),
        "Score_50": int(50 * floor(result_row.Score.values[0] / 50))
    })
    return data
