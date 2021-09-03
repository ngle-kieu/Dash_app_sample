import dash
import dash_core_components as dcc
from dash_core_components.ConfirmDialog import ConfirmDialog
from dash_core_components.ConfirmDialogProvider import ConfirmDialogProvider
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
        dcc.ConfirmDialogProvider(
            children=html.Button(
                'Show graph'
            ),
            id='confirm_graph',
            message='Are you sure you want to view the graph?',
        ),
        html.Div(id='output_dropdown'),
        html.Div(id='output_dialog_provider'),
    ]
)

@app.callback(
    dash.dependencies.Output('output_dropdown', 'children'),
    dash.dependencies.Input('greeting_dropdown', 'value'))
def update_output_dropdown(value):
    return '{} Dash.'.format(value)

@app.callback(
    dash.dependencies.Output('output_dialog_provider', 'children'),
    dash.dependencies.Input('confirm_graph', 'submit_n_clicks'))
def update_output_dropdown(submit_n_clicks):
    if not submit_n_clicks:
        return ''
    return """
        Graph shown!
    """

if __name__=='__main__':
    app.run_server(debug=True,port=8050)