import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json
import flask 
from flask import * 

app = Flask("_name_")


def create_plot():


    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


    data = [
        go.Bar(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


@app.route('/')
def index():

    bar = create_plot()
    return render_template('index1.html', plot=bar)

if __name__ == "__main__":
	app.run()