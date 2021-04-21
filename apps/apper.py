import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import State, Input, Output
from dash.exceptions import PreventUpdate 
import plotly.express as px
import pandas as pd

apper = dash.Dash(
    __name__,
    meta_tags=[
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no",
        }
    ],
)
server = apper.server

apper.config["suppress_callback_exceptions"] = True

# Plotly mapbox token
mapbox_access_token = "pk.eyJ1IjoicGxvdGx5bWFwYm94IiwiYSI6ImNrOWJqb2F4djBnMjEzbG50amg0dnJieG4ifQ.Zme1-Uzoi75IaFbieBDl3A"


df = pd.read_csv("Chloropleth_1.csv")
df1 = pd.read_csv("city3.csv")
df2 = pd.read_csv("Fuel_Stations.csv")

def func1():
    fig = px.scatter_mapbox(df2, lat="Latitude", lon="Longitude", hover_name="Station Name", hover_data=["State", "Fuel Type Code"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
    fig.update_layout(mapbox_style="open-street-map", mapbox_accesstoken=mapbox_access_token)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

apper.layout = html.Div(
        className="container scalable",
    children=[
            dcc.RadioItems(id='dpdn3', value = "ELEC",
                 options=[{'label': x, 'value': x} for x in
                          df.fuel_type.unique()], labelStyle={"display" : "inline-block"}),
        html.Div([
            dcc.Graph(id='chloropleth', figure={}),
            dcc.Graph(id='bar-graph',figure={}),
    ]),
    html.Div([  
        dcc.Graph(id ='map', figure=func1)
    ])
        
])

@apper.callback(
    Output(component_id='chloropleth', component_property='figure'),
    Input(component_id='dpdn3', component_property='value'),
)
def update_graph(fuel_chosen):
    dff = df[df.fuel_type.isin([fuel_chosen])]
    fig = px.choropleth(dff,locations ="state",locationmode="USA-states",color_continuous_scale="thermal",scope="usa", color='count')
    return fig

@apper.callback(
    Output(component_id='bar-graph', component_property='figure'),
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
    fig2 = px.bar(data_frame=dff2, x='city', y='count',title= f'Top 5 Cities in : {state_chosen}')
    return fig2


# def update_map():
#     dff3 = df2 
    
#     return fig 



if __name__ == '__main__':
    apper.run_server(debug=True)

