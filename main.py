import dash
import dash_core_components as dcc
import dash_html_components as html 
import mysql.connector
import pandas as pd
import plotly.express as plt 
import data_fetcher as fetch 

# app = dash.Dash()

# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd ="1234",
#    # auth_plugin='mysql_native_password',
#     database ="usedcars"
# )

# my_cursor = db.cursor()
# myresult = my_cursor.execute("select distinct latitude,longitude,car_year,manufacturer from used_cars_dashboard where car_year>2000")
# myresult = my_cursor.fetchall()

# headings = [i[0] for i in my_cursor.description]

# df = pd.DataFrame(myresult)
# df.sort_values(by= 2, ascending=False, inplace=True)

# fig = plt.scatter_mapbox(df, lat=0, lon=1, hover_name=2, hover_data=[3],
#                          zoom=4, height=600,animation_frame=2 ,color=3)
# fig.update_layout(mapbox_style="carto-darkmatter")
# fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})


# YEARS = [2000,2001,2002,2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015,2016,2017,2018,2019,2020]

# mapbox_access_token = "pk.eyJ1IjoicGxvdGx5bWFwYm94IiwiYSI6ImNrOWJqb2F4djBnMjEzbG50amg0dnJieG4ifQ.Zme1-Uzoi75IaFbieBDl3A"
# mapbox_style = "mapbox://styles/plotlymapbox/cjvprkf3t1kns1cqjxuxmwixz"

# app.layout = html.Div(
#     id="root",
#     children=[
#         html.Div(
#             id="header",
#             children=[
#                 html.Img(id="logo", src=app.get_asset_url("dash-logo.png")),
#                 html.H4(children="Rate of US Poison-Induced Deaths"),
#                 html.P(
#                     id="description",
#                     children="† Deaths are classified using the International Classification of Diseases, \
#                     Tenth Revision (ICD–10). Drug-poisoning deaths are defined as having ICD–10 underlying \
#                     cause-of-death codes X40–X44 (unintentional), X60–X64 (suicide), X85 (homicide), or Y10–Y14 \
#                     (undetermined intent).",
#                 ),
#             ],
#         ),
#         html.Div(
#             id="app-container",
#             children=[
#                 html.Div(
#                     id="left-column",
#                     children=[
#                         html.Div(
#                             id="slider-container",
#                             children=[
#                                 html.P(
#                                     id="slider-text",
#                                     children="Drag the slider to change the year:",
#                                 ),
#                                 dcc.Slider(
#                                     id="years-slider",
#                                     min=min(YEARS),
#                                     max=max(YEARS),
#                                     value=min(YEARS),
#                                     marks={
#                                         str(year): {
#                                             "label": str(year),
#                                             "style": {"color": "#7fafdf"},
#                                         }
#                                         for year in YEARS
#                                     },
#                                 ),
#                             ],
#                         ),
#                         html.Div(
#                             id="heatmap-container",
#                             children=[
#                                 html.P(
#                                     "Heatmap of age adjusted mortality rates \
#                             from poisonings in year {0}".format(
#                                         min(YEARS)
#                                     ),
#                                     id="heatmap-title",
#                                 ),
#                                 dcc.Graph(
#                                     id="county-choropleth",
#                                     figure=dict(
#                                         layout=dict(
#                                             mapbox=dict(
#                                                 layers=[],
#                                                 accesstoken=mapbox_access_token,
#                                                 style=mapbox_style,
#                                                 center=dict(
#                                                     lat=38.72490, lon=-95.61446
#                                                 ),
#                                                 pitch=0,
#                                                 zoom=3.5,
#                                             ),
#                                             autosize=True,
#                                         ),
#                                     ),
#                                 ),
#                             ],
#                         ),
#                     ],
#                 ),
#                 html.Div(
#                     id="graph-container",
#                     children=[
#                         html.P(id="chart-selector", children="Select chart:"),
#                         dcc.Dropdown(
#                             options=[
#                                 {
#                                     "label": "Histogram of total number of deaths (single year)",
#                                     "value": "show_absolute_deaths_single_year",
#                                 },
#                                 {
#                                     "label": "Histogram of total number of deaths (1999-2016)",
#                                     "value": "absolute_deaths_all_time",
#                                 },
#                                 {
#                                     "label": "Age-adjusted death rate (single year)",
#                                     "value": "show_death_rate_single_year",
#                                 },
#                                 {
#                                     "label": "Trends in age-adjusted death rate (1999-2016)",
#                                     "value": "death_rate_all_time",
#                                 },
#                             ],
#                             value="show_death_rate_single_year",
#                             id="chart-dropdown",
#                         ),
#                         dcc.Graph(
#                             id="selected-data",
#                             figure=dict(
#                                 data=[dict(x=0, y=0)],
#                                 layout=dict(
#                                     paper_bgcolor="#F4F4F8",
#                                     plot_bgcolor="#F4F4F8",
#                                     autofill=True,
#                                     margin=dict(t=75, r=50, b=100, l=50),
#                                 ),
#                             ),
#                         ),
#                     ],
#                 ),
#             ],
#         ),
#     ],
# )




# # def first_map():
# #     dff = df.copy()
# #     fig =  plt.scatter_mapbox( 
# #         dff,
# #         lat = 0, 
# #         lon = 1,
# #         hover_name = 2, 
# #         hover_data=[3],
# #         zoom=4,
# #         height=600,
# #         color_discrete_sequence=["fuchsia"],
# #         mapbox_style="open-street-map"
# #     )


# if __name__ == '__main__':
#     app.run_server()

# data = fetch.state('wy')
# print(data)

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

print(data_dict)