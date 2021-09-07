import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Sample Graph"
)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True
app.layout = html.Div(
    children=[
        html.H1(children='Hello Dash'),
        dcc.Dropdown(
            id='greeting_dropdown',
            options=[
                {'label': 'English', 'value': 'Hello'},
                {'label': 'German', 'value': 'Hallo'},
                {'label': 'Japanese', 'value': 'Konichiwa'},
                {'label': 'Vietnamese', 'value': 'Chao'}
            ],
            value='Greeting',
        ),
        html.Div(id='output_dropdown'),
        dcc.ConfirmDialogProvider(
            children=html.Button(
                'Show graph'
            ),
            id='confirm_graph',
            message='Are you sure you want to view the graph?',
        ),
        html.Div(id='output_graph',
                 children=dcc.Graph(figure=fig),
                 style={'display': 'block'})
    ]
)


@app.callback(
    dash.dependencies.Output('output_dropdown', 'children'),
    dash.dependencies.Input('greeting_dropdown', 'value'))
def update_output_dropdown(value):
    if value is None:
        value = 'Greeting'
    return '{} Dash.'.format(value)


@app.callback(
    dash.dependencies.Output('output_graph', 'style'),
    dash.dependencies.Input('confirm_graph', 'submit_n_clicks'))
def update_output_dropdown(submit_n_clicks):
    if not submit_n_clicks:
        return {'display': 'none'}
    else:
        return {'display': 'block'}


if __name__ == '__main__':
    app.run_server(debug=True, port=8052)
