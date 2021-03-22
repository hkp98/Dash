import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import State, Input, Output
from dash.exceptions import PreventUpdate
import data_fetcher as fetch 

import pandas as pd
import os

app = dash.Dash(
    __name__,
    meta_tags=[
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no",
        }
    ],
)
server = app.server

app.config["suppress_callback_exceptions"] = True

# Plotly mapbox token
mapbox_access_token = "pk.eyJ1IjoicGxvdGx5bWFwYm94IiwiYSI6ImNrOWJqb2F4djBnMjEzbG50amg0dnJieG4ifQ.Zme1-Uzoi75IaFbieBDl3A"

state_map = {
    "AK": "ak",
    "AL": "al",
    "AR": "ar",
    "AZ": "az",
    "CA": "ca",
    "CO": "co",
    "CT": "ct",
    "DC": "dc",
    "DE": "de",
    "FL": "fl",
    "GA": "ga",
    "HI": "hi",
    "IA": "ia",
    "ID": "id",
    "IL": "il",
    "IN": "in",
    "KS": "ks",
    "KY": "ky",
    "LA": "la",
    "MA": "ma",
    "MD": "md",
    "ME": "me",
    "MI": "mi",
    "MN": "mn",
    "MO": "mo",
    "MS": "ms",
    "MT": "mt",
    "NC": "nc",
    "ND": "nd",
    "NE": "ne",
    "NH": "nh",
    "NJ": "nj",
    "NM": "nm",
    "NV": "nv",
    "NY": "ny",
    "OH": "oh",
    "OK": "ok",
    "OR": "or",
    "PA": "pa",
    "RI": "ri",
    "SC": "sc",
    "SD": "sd",
    "TN": "tn",
    "TX": "tx",
    "UT": "ut",
    "VA": "va",
    "VT": "vt",
    "WA": "wa",
    "WI": "wi",
    "WV": "wv",
    "WY": "wy",
}

state_list = list(state_map.values())

data_dict = {}
for state in state_list:
    state_data = fetch.query_state(state)
    data_dict[state] = state_data

car_fuel=["Gas","Diesel","Electric","Hybrid"]

def build_upper_left_panel():
    return html.Div(
        id="upper-left",
        className="six columns",
        children=[
            html.P(
                className="section-title",
                children="Choose car listings on the map",
            ),
            html.Div(
                className="control-row-1",
                children=[
                    html.Div(
                        id="state-select-outer",
                        children=[
                            html.Label("Select a State"),
                            dcc.Dropdown(
                                id="state-select",
                                options=[{"label": i, "value": i} for i in state_list],
                                value=state_list[1],
                            ),
                        ],
                    ),
                    html.Div(
                        id="select-metric-outer",
                        children=[
                            html.Label("Choose the fuel-type of Vehicle"),
                            dcc.Dropdown(
                                id="car_fuel-select",
                                options=[{"label": i, "value": i} for i in car_fuel],
                                value=car_fuel[0],
                            ),
                        ],
                    ),
                ],
            ),
            html.Div(
                id="region-select-outer",
                className="control-row-2",
                children=[
                    html.Label("Pick a Region"),
                    html.Div(
                        id="checklist-container",
                        children=dcc.Checklist(
                            id="region-select-all",
                            options=[{"label": "Select All Regions", "value": "All"}],
                            value=[],
                        ),
                    ),
                    html.Div(
                        id="region-select-dropdown-outer",
                        children=dcc.Dropdown(
                            id="region-select", multi=True, searchable=True,
                        ),
                    ),
                ],
            ),
             html.Div([
                html.Label("Drag the Slider to Change the Year"),
                dcc.RangeSlider(
                id='year-slider',
                min=2000,
                max=2020,
                step=1.0,
                value=[2010, 2015],
                marks={
                        2000: {'label': '2000'},
                        2001: {'label': '2001'},
                        2002: {'label': '2002'},
                        2003: {'label': '2003'},
                        2004: {'label': '2004'},
                        2005: {'label': '2005'},
                        2006: {'label': '2006'},
                        2007: {'label': '2007'},
                        2008: {'label': '2008'},
                        2009: {'label': '2009'},
                        2010: {'label': '2010'},
                        2011: {'label': '2011'},
                        2012: {'label': '2012'},
                        2013: {'label': '2013'},
                        2014: {'label': '2014'},
                        2015: {'label': '2015'},
                        2016: {'label': '2016'},
                        2017: {'label': '2017'},
                        2018: {'label': '2018'},
                        2019: {'label': '2019'},
                        2020: {'label': '2020'}}
    
                ),
                html.Div(id='output-container-year-slider')
            ]),
            html.Div(
                id="table-container",
                className="table-container",
                children=[
                    html.Div(
                        id="table-lower",
                        children=[
                            html.P("Procedure Charges Summary"),
                            dcc.Loading(
                                children=html.Div(id="procedure-stats-container")
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )
app.layout = html.Div(
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
        html.Div(
            id="upper-container",
            className="row",
            children=[
                build_upper_left_panel(),
                html.Div(
                    id="geo-map-outer",
                    className="six columns",
                    children=[
                        html.P(
                            id="map-title",
                            children="Car listings in the State of {}".format(
                                state_map[state_list[0]]
                            ),
                        ),
                        html.Div(
                            id="geo-map-loading-outer",
                            children=[
                                dcc.Loading(
                                    id="loading",
                                    children=dcc.Graph(
                                        id="geo-map",
                                        figure={
                                            "data": [],
                                            "layout": dict(
                                                plot_bgcolor="#171b26",
                                                paper_bgcolor="#171b26",
                                            ),
                                        },
                                    ),
                                )
                            ],
                        ),
                    ],
                ),
            ],
        ),
        
    ],
)


if __name__ == "__main__":
    app.run_server(debug=True)