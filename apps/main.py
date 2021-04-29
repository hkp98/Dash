import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import State, Input, Output
from dash.exceptions import PreventUpdate 
import dash_cytoscape as cyto

import pandas as pd
import os

from app import app


# app = dash.Dash(
#     __name__,
#     meta_tags=[
#         {
#             "name": "viewport",
#             "content": "width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no",
#         }
#     ],
# )
# server = app.server

# app.config["suppress_callback_exceptions"] = True

# Plotly mapbox token
# fig = go.Figure()
mapbox_access_token = "pk.eyJ1IjoiaGFyc2hwYXRlbDk4IiwiYSI6ImNrbXI0cXB0ejA0YnEydnJ5N2x2eWZkMjYifQ.X7UzQvxMuyQmdFE0SNgH5w"

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

data_dict = {}
it = 0
for state in state_list:
    p = os.getcwd().split(os.path.sep)
    csv_path = "Data//{}.csv".format(state)
    state_data = pd.read_csv(csv_path)
    data_dict[state] = state_data
    
init_region = data_dict[state_list[0]][
    "state_region"
].unique()

car_year=[2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000]

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
                                value=state_list[31],
                            ),
                        ],
                    ),
                    html.Div(
                        id="select-metric-outer",
                        children=[
                            html.Label("Choose the year of Vehicle"),
                            dcc.Dropdown(
                                id="car-year-select",
                                options=[{"label": i, "value": i} for i in car_year],
                                value=car_year[0],
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
                html.Label("Drag the Slider to Change the Price"),
                dcc.RangeSlider(
                id='price-select',
                min=0,
                max=50000,        
                value=[5000, 20000],
                marks={
                        0: {'label': '0'},
                        5000: {'label': '5000'},
                        10000: {'label': '10000'},
                        20000: {'label': '20000'},                        
                        50000: {'label': '50000'}}
                ),
                html.Div(id='output-container-price-slider')
            ]),
        ],
    )

def generate_geo_map(geo_data,region_select,car_year_select,price_select):
    car_year_select = [car_year_select]
    
    filtered_data = geo_data[
        geo_data["state_region"].isin(
            region_select)
    ]
    filtered_data = filtered_data[filtered_data["car_year"].isin(car_year_select)]
    filtered_data=filtered_data[filtered_data["price"]>= price_select[0]]
    filtered_data=filtered_data[filtered_data["price"]<= price_select[1]]

    # print(filtered_data)

    colors = ["#21c7ef", "#76f2ff", "#ff6969", "#ff1717"]

    hospitals = []
    # print(filtered_data)
    lat = filtered_data["latitude"].tolist()
    lon = filtered_data["longitude"].tolist()
    regions = filtered_data["state_region"].tolist()
    years = filtered_data["car_year"].tolist()
    models = filtered_data["model"].tolist()
    manufacturers = filtered_data["manufacturer"].tolist()
    prices= filtered_data["price"].tolist()
    x = 0
    if len(lat) > 1000:
        x = 1000
    else:
        x = len(lat) 
    for i in range(x):
        region = regions[i]
        year = years[i]
        model = models[i]
        manufacturer = manufacturers[i]
        price = prices[i]
        
        hospital = go.Scattermapbox(
            lat=[lat[i]],
            lon=[lon[i]],
            mode="markers",
            customdata=[(year,region)],
            hoverinfo="text",
            text =
             "<br>Manufacturer: "
            + manufacturer
            + "<br>Model: "
            + model
            + "<br>Region: "
            + region
            + "<br>Price: "
            + str(price),
        )
        hospitals.append(hospital)

    layout = go.Layout(
        margin=dict(l=10, r=10, t=20, b=10, pad=5),
        plot_bgcolor="#171b26",
        paper_bgcolor="#171b26",
        clickmode="event+select",
        hovermode="closest",
        showlegend=False,
        mapbox=go.layout.Mapbox(
            accesstoken=mapbox_access_token,
            bearing=10,
            center=go.layout.mapbox.Center(
                lat=filtered_data.latitude.mean(), lon=filtered_data.longitude.mean()
            ),
            pitch=5,
            zoom=5,
            style="mapbox://styles/plotlymapbox/cjvppq1jl1ips1co3j12b9hex",
        ),
    )

    return {"data": hospitals, "layout": layout}

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
        
                dcc.Link('Buyers & Sellers Perspective',className="menu_link", href='/apps/buyers'),
        
                dcc.Link('Go Electric',className="menu_link", href='/apps/apper'),
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
        html.H6("Word Cloud", style={'text-align': 'center'}),
        html.Div([
    dcc.Graph(id = "image",figure={})
              ]),
    ],
)

@app.callback(
    [
        Output("region-select", "value"),
        Output("region-select", "options"),
        Output("map-title", "children"),
    ],
    [Input("region-select-all", "value"), Input("state-select","value"),],
)
def update_region_dropdown(select_all, state_select):
    state_raw_data = data_dict[state_select]
    regions = state_raw_data["state_region"].unique()
    options = [{"label": i, "value": i} for i in regions]

    ctx = dash.callback_context
    if ctx.triggered[0]["prop_id"].split(".")[0] == "region-select-all":
        if select_all == ["All"]:
            value = [i["value"] for i in options]
        else:
            value = dash.no_update
    else:
        value = regions[:4]
    return (
        value,
        options,
        "Used Cars listings in the State of {}".format(
            state_map[state_select]),
    )

@app.callback(
    Output("checklist-container", "children"),
    [Input("region-select", "value")],
    [State("region-select", "options"), State("region-select-all", "value")],
)
def update_checklist(selected, select_options, checked):
    if len(selected) < len(select_options) and len(checked) == 0:
        raise PreventUpdate()

    elif len(selected) < len(select_options) and len(checked) == 1:
        return dcc.Checklist(
            id="region-select-all",
            options=[{"label": "Select All Regions", "value": "All"}],
            value=[],
        )

    elif len(selected) == len(select_options) and len(checked) == 1:
        raise PreventUpdate()

    return dcc.Checklist(
        id="region-select-all",
        options=[{"label": "Select All Regions", "value": "All"}],
        value=["All"],
    )

@app.callback(
    Output("geo-map", "figure"),
    [
        Input("state-select", "value"),
        Input("region-select", "value"),
        Input("car-year-select", "value"),
        Input("price-select", "value"),
        
    ],
)
def update_geo_map(state_select,region_select,car_year_select,price_select):
    # generate geo map from state-select, procedure-select
    # print(region_select)
    # print(car_year_select)
    state_agg_data = data_dict[state_select]
    return generate_geo_map(state_agg_data,region_select,car_year_select,price_select)

@app.callback(
    Output("image", "figure"),
    Input("state-select", "value"),
)

def update_iamge(state_select):
    img_width = 1400
    img_height = 800
    scale_factor = 0.50
    fig = go.Figure()
    # Add invisible scatter trace.
    # This trace is added to help the autoresize logic work.
    fig.add_trace(
        go.Scatter(
            x=[0, img_width * scale_factor],
            y=[0, img_height * scale_factor],
            mode="markers",
            marker_opacity=0
        )
    )

    # Configure axes
    fig.update_xaxes(
        visible=False,
        range=[0, 2*img_width * scale_factor]
    )

    fig.update_yaxes(
        visible=False,
        range=[0, img_height * scale_factor],
        # the scaleanchor attribute ensures that the aspect ratio stays constant
        scaleanchor="x"
    )
    # Add image
    fig.add_layout_image(
        dict(
            x=0,
            sizex= 2*img_width * scale_factor,
            y=img_height * scale_factor,
            sizey=img_height * scale_factor,
            xref="x",
            yref="y",
            opacity=1.0,
            layer="below",
            sizing="stretch",
            source=app.get_asset_url("{}.png".format(state_select)))
    )

    # Configure other layout
    fig.update_layout(
        width=2*img_width * scale_factor,
        height=img_height * scale_factor,
        margin={"l": 0, "r": 0, "t": 0, "b": 0},
    )
    return fig


# if __name__ == "__main__":
#     app.run_server(debug=True)