import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import State, Input, Output
from dash.exceptions import PreventUpdate 
import plotly.express as px
import pandas as pd
from app import app

# apper = dash.Dash(
#     __name__,
#     meta_tags=[
#         {
#             "name": "viewport",
#             "content": "width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no",
#         }
#     ],
# )
# server = apper.server

# apper.config["suppress_callback_exceptions"] = True

# Plotly mapbox token
mapbox_access_token = "pk.eyJ1IjoicGxvdGx5bWFwYm94IiwiYSI6ImNrOWJqb2F4djBnMjEzbG50amg0dnJieG4ifQ.Zme1-Uzoi75IaFbieBDl3A"


df = pd.read_csv("Data//Chloropleth_1.csv")
df1 = pd.read_csv("Data//city3.csv")
df2 = pd.read_csv("Data//Fuel_Stations.csv")

fig = px.scatter_mapbox(df2, lat="Latitude", lon="Longitude", hover_name="Station Name", hover_data=["State", "Fuel Type Code"],
                                    color = 'State', zoom=3, height=200)
fig.update_layout(mapbox_style="open-street-map", mapbox_accesstoken=mapbox_access_token)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.update_layout(
    geo_scope='usa',
)
                

layout = html.Div(
        className="container scalable",
    children=[
        html.Div(
            id="banner",
            className="banner",
            children=[
                html.Img(src=app.get_asset_url("Used_Cars_Logo.png")),
                html.H1("Used Cars Dashboard", style={'text-align': 'center'}),
                
                
            ],
        ),

                dcc.Link('Home',className="menu_link", href='home'),
        
                dcc.Link('Dashboard',className="menu_link", href='/apps/main'),
        
                dcc.Link('Buyers & Sellers Perspective',className="menu_link", href='/apps/buyers'),
            dcc.RadioItems(id='dpdn3', value = "ELEC",
                 options=[{'label': x, 'value': x} for x in
                          df.fuel_type.unique()], labelStyle={"display" : "inline-block"}),
        html.Div([
            dcc.Graph(id='chloropleth', figure={}),
            dcc.Graph(id='bar-graph-top',figure={}),
    ]),
    html.H6( 'Electric Charging Stations in US',style = {'text-align': 'center'}),
    html.Div([  
        dcc.Graph(id ='map', figure=fig)
    ])
        
])

@app.callback(
    Output(component_id='chloropleth', component_property='figure'),
    Input(component_id='dpdn3', component_property='value'),
)
def update_graph(fuel_chosen):
    dff = df[df.fuel_type.isin([fuel_chosen])]
    fig = px.choropleth(dff,locations ="state",locationmode="USA-states",color_continuous_scale="thermal",scope="usa", color='count')
    fig.update_layout(
    title={
        'text': "Choropleth Map Showing the count of each type of Charging Station State-wise ",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
    return fig

@app.callback(
    Output(component_id='bar-graph-top', component_property='figure'),
    Input(component_id='chloropleth', component_property='clickData'),
    Input(component_id='dpdn3', component_property='value')
)
def update_side_graph(state_chosen,fuel):
    if state_chosen is None:
        state_chosen ='CA'
    else:
        state_chosen = state_chosen['points'][0]['location']
    dff2 = df1[df1.state.isin([state_chosen])]
    dff2 = dff2[dff2.fuel_type.isin([fuel])]
    fig2 = px.bar(data_frame=dff2, x='city', y='count')
    fig2.update_layout(
    title={
        'text': f'Top 5 Cities in : {state_chosen}',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
    return fig2


# def update_map():
#     dff3 = df2 
    
#     return fig 



# if __name__ == '__main__':
#     apper.run_server(debug=True)

