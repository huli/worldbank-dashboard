from worldbankapp import app
import json, plotly
from flask import render_template
from wrangling_scripts.wrangle_data import load_figures

@app.route('/')
@app.route('/index')
def index():

    figures = load_figures()

    # Plot ids for the id tag
    ids = ['fig-{}'.format(i) for i, _ in enumerate(figures)]

    # Convert the plotly figures to JSON
    figures_json = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

    # Render template and include figures
    return render_template('/index.html',
                ids=ids,
                figures_json=figures_json) 