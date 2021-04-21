import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from app import app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


import dash_bootstrap_components as dbc




header = dbc.Row(
    dbc.Col(
        html.Div([
            html.H2(children='Used Cars Dashboard'),
            html.H3(children='Data Visualization and Analytics of Used Cars data')])
        ),className='banner')

content = html.Div([
    dcc.Location(id='url'),
    html.Div(id='page-content')
])

container = dbc.Container([
    header,
    content,
])

layout = html.Div(
        className="container scalable",
    children=[
        html.Div(
            id="banner",
            className="banner",
            children=[
                html.H1("Used Cars Dashboard", style={'text-align': 'center'}),
                html.Img(src=app.get_asset_url("Used_Cars_Logo.png"), 
                
                ),
                
            ],
        ),
        html.Div([
            #html.H2(children='Used Cars Dashboard'),
            html.H3(children='A Simplified Interface for the Buyer and Seller to make a right decision')])
        ,

        html.Div(id='app-1-display-value'),
                dcc.Link('Dashboard', href='/apps/main'),
        html.Div(id='app-2-display-value'),
                dcc.Link('Buyers', href='/apps/buyers'),

    
    html.Div(
            [
                dcc.Markdown(
                    '''
            
             ** In the United States every man is entitled to life, liberty and a car in which to pursue happiness.  -- *EVAN ESAR* **
    
            
            
            ### The Applicaiton
            The Used Cars Dashboard is an interactive platform having database with information of 500K used cars across the United
            States of America which covers car listings since 2020,January. Using the information extracted from Kaggle.com, as part of the course
            CS526: Data Interaction and Visualization, we have designed and developed an interactive dashboard which explores the data set in
            depth. In addition to summarizing the listings and plotting them interactively over the locations, the dashboard provides means to view
            important statistics of an buying a used car in a particular state. Such understanding of the data can be serve as a guide in the decision
            making process of a buyer and can also provide some meaningful insights to the seller as well.


            ### Data
            The data-set is from Kaggle and is the world's largest collection of used vehicles for sale from Craigslist. The data
            is scraped every few months, it contains all the relevant information on car sales including columns like price, condition, manufacturer longitude, latitude, year, color, model, VIN,
            titlestatus, etc.
            
            
           
        '''
                )
            ],
            className="home",
        )
])



# if __name__ == '__main__':
#     app.run_server(debug=True)