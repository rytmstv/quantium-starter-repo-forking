# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd


app = Dash(__name__)

colors = {
    'background': '#FFFFFF',
    'text': '#000000'
}

df = pd.read_csv('https://raw.githubusercontent.com/rytmstv/quantium-starter-repo-forking/main/formatted_data.csv')

fig = px.line(df, x="date", y="sales",
                color = "region")

app.layout = html.Div(
    
    style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children=' A visualization of the pink morsel sales from 2018 to 2022',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    
    
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])

if __name__ == '__main__':
     app.run_server(debug=True)

# A visualization of the pink morsel sales from 2018 to 2022