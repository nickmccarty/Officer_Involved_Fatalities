import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly_express as px
import pandas as pd
import flask

########### Set up the chart

px.set_mapbox_access_token('pk.eyJ1Ijoibmlja21jY2FydHkiLCJhIjoiY2pxemppMDZoMGJxeDQ0dDJ5OWxhcXA3dCJ9.k6cGbYHEbY2UDT-D6chFbw')

fatalities = pd.read_csv('Data/fatalities_geocoded_with_pop.csv')
fatalities = fatalities.drop('Unnamed: 0', axis = 1)

test = fatalities.groupby(['state', 'race', 'location', 'latitude', 'longitude'])['name'].count()
test = test.reset_index()
test = test.rename({'name' : 'count'}, axis = 1)
test = test.sort_values('count', ascending = False)

fig = px.scatter_mapbox(test, lat="latitude", lon="longitude",  color="race", size="count",
                  color_continuous_scale=px.colors.cyclical.IceFire, size_min=5, size_max=20, zoom=3, hover_name = 'location', opacity = .5)

########### Display the chart

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=external_stylesheets)

app.title = "Police Shootings"

description = 'Termed "legal intervention deaths" elsewhere, this map shows the locations\
               and raw counts of deaths (since 2015) caused by on-duty police officers\
               during confrontations with civilians. While we can safely assume that the fatalities\
               respectfully visualized here do not give us a complete picture of the reality seen in\
               the U.S. population, sincere gratitude is extended to John Muyskens and his colleagues\
               at the Washington Post for putting forth the effort to collect and maintain this dataset.'

caveat = 'As we know, raw death counts on a map do not adequately allow for anyone to gain a true sense of reality\
          from data that even the FBI only started collecting in earnest circa 2017. It is with this in mind\
          that funtionality and visualizations will be added incrementally to this page over time.'

contact = 'This is a good faith attempt at helping people gain clairty on a serious topic. With this in mind, please\
           send any critiques, observations, or inquiries to NumerateAnalytics@gmail.com.'

app.layout = html.Div(children=[
    html.H1('Officer-Involved Fatalities'),
    html.P(description),
    dcc.Graph(
        id='fatalities',
        figure=fig
    ),
    html.P(caveat),
    html.P('\n'),
    html.P(contact),
    html.P('\n'),
    html.A('Code', href='https://github.com/nickmccarty/Officer_Involved_Fatalities'),
    html.Br(),
    html.A('Data Source', href='https://raw.githubusercontent.com/washingtonpost/data-police-shootings/master/fatal-police-shootings-data.csv'),
    ]
)

if __name__ == '__main__':
    app.run_server()
