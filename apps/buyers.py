import dash  # use Dash version 1.16.0 or higher for this app to work
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
from numpy.core.shape_base import stack
import plotly.express as px
import pandas as pd 
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from app import app

df = pd.read_csv("Data//page2.csv")
df_1 = pd.read_csv("Data//bar_plot.csv")
df_2 = pd.read_csv("Data//condition_plots.csv")
df_3 = pd.read_csv("Data//drive_plots.csv")
df_4 = pd.read_csv("Data//fuel.csv")
df = df.groupby(["car_year","state"]).mean()
df = df.add_suffix('_Average').reset_index()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

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
        
                dcc.Link('Go Electric',className="menu_link", href='/apps/apper'),
            dcc.Dropdown(id='dpdn2', value=['NJ','NY'], multi=True,
                 options=[{'label': x, 'value': x} for x in
                          df.state.unique()]),
        html.Div([
            dcc.Graph(id='pie-graph', figure={}, className='six columns'),
            dcc.Graph(id='my-graph', figure={}, clickData=None, hoverData=None, # I assigned None for tutorial purposes. By defualt, these are None, unless you specify otherwise.
                  config={
                      'staticPlot': False,     # True, False
                      'scrollZoom': True,      # True, False
                      'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                      'showTips': False,       # True, False
                      'displayModeBar': True,  # True, False, 'hover'
                      'watermark': True,
                      # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                        },
                  className='six columns'
                  ),
        dcc.Graph(id='bar-graph',figure={},className='six columns'),
        dcc.Graph(id='bar-graph1',figure={},className='six columns'),
        dcc.Graph(id='bar-graph2',figure={},className='six columns'),
        dcc.Graph(id='bar-graph3',figure={},className='six columns')
    ])
])


@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='dpdn2', component_property='value'),
)
def update_graph(state_chosen):
    dff = df[df.state.isin(state_chosen)]
    fig = px.line(data_frame=dff, x='car_year', y='price_Average', color='state',
                  custom_data=['state', 'car_year', 'price_Average','odometer_Average'])
    fig.update_traces(mode='lines+markers')
    fig.update_layout(
    title={
        'text': " Line Chart showing Increase in prices yearly  ",
        'y':0.92,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
    return fig


# Dash version 1.16.0 or higher
@app.callback(
    Output(component_id='pie-graph', component_property='figure'),
    Input(component_id='my-graph', component_property='hoverData'),
    Input(component_id='my-graph', component_property='clickData'),
    Input(component_id='my-graph', component_property='selectedData'),
    Input(component_id='dpdn2', component_property='value')
)

def update_side_graph(hov_data, clk_data, slct_data, state_chosen):
    if hov_data is None:
        dff2 = df[df.state.isin(state_chosen)]
        dff2 = dff2[dff2.car_year == 2000]
        # print(dff2)
        fig2 = px.pie(data_frame=dff2, values='price_Average', names='state',
                      )
        fig2.update_layout(
         title={
        'text': ' Average Odometer Comparison for 2000 ',
        'y':0.92,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
        return fig2
    else:
        # print(f'hover data: {hov_data}')
        # print(hov_data['points'][0]['customdata'][0])
        # print(f'click data: {clk_data}')
        # print(f'selected data: {slct_data}')
        dff2 = df[df.state.isin(state_chosen)]
        hov_year = hov_data['points'][0]['x']
        dff2 = dff2[dff2.car_year == hov_year]
        fig2 = px.pie(data_frame=dff2, values='odometer_Average', names='state', title=f'Average Odometer Comparison: {hov_year}')
        return fig2

@app.callback(
    Output(component_id='bar-graph', component_property='figure'),
    Input(component_id='dpdn2', component_property='value'),
    
)
def update_graph_bottom(state_chosen):
    dff = df_1[df_1.state.isin(state_chosen)]
    # fig3 = px.bar(data_frame=dff, x='manufacturer', y='count_manufacturer', color='state',barmode="stack",orientation='v')
    fig5 = px.sunburst(dff, path=['state','manufacturer','count_manufacturer'],
                  color='manufacturer',maxdepth=2,branchvalues='remainder')
    fig5.update_layout(
         title={
        'text': ' Sunburst plot for Top 5 Manufacturer State-wise ',
        'y':0.92,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
    return fig5

@app.callback(
    Output(component_id='bar-graph1', component_property='figure'),
    Input(component_id='dpdn2', component_property='value'),   
)
def update_graph_bottom(state_chosen):
    dff = df_2[df_2.state.isin(state_chosen)]
    # fig3 = px.bar(data_frame=dff, x='car_condition', y='count', color='state',barmode="stack",orientation='v')
    fig4 = px.treemap(dff, path=[px.Constant('state'),'state','car_condition'],values = 'count',
                  color='state',maxdepth = 2)
    fig4.update_layout(
         title={
        'text': ' Treemap for Car Condition State-wise ',
        'y':0.98,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
    return fig4

@app.callback(
    Output(component_id='bar-graph2', component_property='figure'),
    Input(component_id='dpdn2', component_property='value'),
    
)
def update_graph_bottom(state_chosen):
    dff = df_3[df_3.state.isin(state_chosen)]
    fig3 = px.bar(data_frame=dff, x='drive', y='count', color='state',barmode="stack",orientation='v')
    fig3.update_layout(
         title={
        'text': ' Stacked Bar-plot for Drive Type State-wise ',
        'y':0.92,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
    return fig3

@app.callback(
    Output(component_id='bar-graph3', component_property='figure'),
    Input(component_id='dpdn2', component_property='value'),
    
)
def update_graph_bottom(state_chosen):
    dff = df_4[df_4.state.isin(state_chosen)]
    # fig3 = px.bar(data_frame=dff, x='fuel', y='count', color='state',barmode="stack",orientation='v')

    fig = make_subplots(rows=2, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}],[{'type':'domain'},{'type':'domain'}]])
    fig.add_trace(go.Pie(labels=dff['state'], values = dff['gas'], name="Gas"),1, 1)
    fig.add_trace(go.Pie(labels=dff['state'], values = dff['diesel'], name="Diesel"),1, 2)
    fig.add_trace(go.Pie(labels=dff['state'], values = dff['hybrid'], name="Hybrid"),2, 1)
    fig.add_trace(go.Pie(labels=dff['state'], values = dff['electric'], name="Electric"),2, 2)    

    # Use `hole` to create a donut-like pie chart
    fig.update_traces(hole=.4, hoverinfo="label+percent+name")

    fig.update_layout(
    title={
        'text': ' Fuel Type Comparison as per State ',
        'y':0.92,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='Gas', x=0.18, y=0.5, font_size=15, showarrow=False),
                 dict(text='Diesel', x=0.83, y=0.5, font_size=15, showarrow=False),
                 dict(text='Hybrid', x=0.16, y=-0.1, font_size=15, showarrow=False),
                 dict(text='Electric',x=0.84, y=-0.1, font_size=15, showarrow=False)])

    return fig



# if __name__ == '__main__':
#     app.run_server(debug=True)