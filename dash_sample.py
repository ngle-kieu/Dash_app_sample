import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout= html.Div(
    children=[
        html.H1(children='Hello Dash'),
        dcc.Dropdown(
            id='greeting_dropdown',
            options=[
                {'label':'English', 'value':'Hello'},
                {'label':'German', 'value':'Hallo'},
                {'label':'Japanese', 'value':'Konichiwa'},
                {'label':'Vietnamese', 'value':'Chao'}
            ],
            value='Hey',
        ),
        html.Div(id='output-dropdown')
    ]
)

@app.callback(
    dash.dependencies.Output('output-dropdown', 'children'),
    dash.dependencies.Input('greeting_dropdown', 'value'))
def update_output_dropdown(value):
    return '{} Dash.'.format(value)

if __name__=='__main__':
    app.run_server(debug=True,port=8050)