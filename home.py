import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from app import app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

layout = html.Div(
        className="container scalable",
    children=[
        html.Div(
            id="banner",
            className="banner",
            children=[
                html.H1("Used Cars Dashboard", style={'text-align': 'center'}),
                html.Img(src=app.get_asset_url("Used_Cars_Logo.png")),
                
            ],
        ),
        html.Div(id='app-1-display-value'),
                dcc.Link('Dashboard', href='/apps/main'),
        html.Div(id='app-2-display-value'),
                dcc.Link('Buyers', href='/apps/buyers'),

    
    html.Div(
            [
                dcc.Markdown(
                    """
            ### The Application
            Add something about used cars dashboard.
        """
                )
            ],
            className="home",
        )
])

# if __name__ == '__main__':
#     app.run_server(debug=True)