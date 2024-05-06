import dash
from dash import dcc  # dash core components
from dash import html  # dash html components

app = dash.Dash("DGAP Trade Bot")

def page_setup(fig) -> None:
    app.layout = html.Div(style={"backgroundColor" : "#008888"}, children=[
        html.H1("DGAP trade bot", style={"textAlign" : "center"}),
        dcc.Graph(figure=fig, style={"width":"700px"}),
        html.Button("Button1", id='button1', title="hahahaha")
        ])

def run_server():
    app.run(debug=True)