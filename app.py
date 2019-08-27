import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly_express as px
import pandas as pd
import flask

########### Set up the chart

px.set_mapbox_access_token('pk.eyJ1Ijoibmlja21jY2FydHkiLCJhIjoiY2pxemppMDZoMGJxeDQ0dDJ5OWxhcXA3dCJ9.k6cGbYHEbY2UDT-D6chFbw')

fatalities = pd.read_csv('fatalities_geocoded_with_pop.csv')
fatalities = fatalities.drop('Unnamed: 0', axis = 1)

test = fatalities.groupby(['state', 'race', 'location', 'latitude', 'longitude'])['name'].count()
test = test.reset_index()
test = test.rename({'name' : 'count'}, axis = 1)
test = test.sort_values('count', ascending = False)

fig = px.scatter_mapbox(test, lat="latitude", lon="longitude",  color="race", size="count",
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=20, zoom=3, hover_name = 'location', opacity = .5)

########### Display the chart

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)

app.layout = html.Div(children=[
    html.H1('Officer-Involved Fatalities'),
    dcc.Graph(
        id='fatalities',
        figure=fig
    ),
    html.A('Code', href='https://https://github.com/nickmccarty/Officer_Involved_Fatalities'),
    html.Br(),
    html.A('Data Source', href='https://raw.githubusercontent.com/washingtonpost/data-police-shootings/master/fatal-police-shootings-data.csv'),
    ]
)

if __name__ == '__main__':
    app.run_server()
