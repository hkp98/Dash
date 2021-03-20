import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import State, Input, Output
from dash.exceptions import PreventUpdate

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
    "AK": "Alaska",
    "AL": "Alabama",
    "AR": "Arkansas",
    "AZ": "Arizona",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DC": "District of Columbia",
    "DE": "Delaware",
    "FL": "Florida",
    "GA": "Georgia",
    "HI": "Hawaii",
    "IA": "Iowa",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "MA": "Massachusetts",
    "MD": "Maryland",
    "ME": "Maine",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MO": "Missouri",
    "MS": "Mississippi",
    "MT": "Montana",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "NE": "Nebraska",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NV": "Nevada",
    "NY": "New York",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VA": "Virginia",
    "VT": "Vermont",
    "WA": "Washington",
    "WI": "Wisconsin",
    "WV": "West Virginia",
    "WY": "Wyoming",
}


state_list = list(state_map.keys())

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
                html.H1("Used Cars Dashboard"),
                
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
                            children="Medicare Provider Charges in the State of {}".format(
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