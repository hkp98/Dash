import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import main, buyers, apper
import home


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    
    if pathname == '/apps/main':
        return main.layout
    elif pathname == '/apps/buyers':
        return buyers.layout
    elif pathname == '/apps/apper':
        return apper.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=False)