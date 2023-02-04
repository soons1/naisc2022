from dash import dash, dcc, html
import pandas as pd
import plotly.express as px

#Palette used
colors = {
    'background': '#152238',
    'text': '#e0ffff'
}

#Create an instance of the Dash class
app = dash.Dash(__name__)
app.title = "Sentiment Analysis Dashboard"

#Read data from CSV file
df = pd.read_csv("scraped_data.csv")

#Formatting data
format = pd.melt(df, value_vars=["Negative", "Neutral", "Positive"], value_name="Count", var_name="Sentiment")
sumOfTweets = format.sum(axis = 0, numeric_only = True)

#Creating Pie Chart
piechart = px.pie(format, 
                values = "Count", 
                names = "Sentiment",
                color = "Sentiment",
                color_discrete_sequence = px.colors.sequential.RdBu,
                hole = 0.4,
                title = "Sentiment Breakdown")
#Pie Chart Traces
piechart.update_traces(textposition = "inside", textinfo = "percent+label")
#Pie Chart Styling
piechart.update_layout(
    font = dict(
        family = "Roboto Mono",
        size = 16,
    ),
    title_font_size = 25,
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

#Creating Bar Chart
barchart = px.bar(format, 
            x = "Sentiment", 
            y ="Count",
            text_auto = True,
            title = "Distribution of Satisfaction Levels",
            color = "Sentiment"
            )
#Bar Chart Traces
barchart.update_traces(textposition = "inside", width = 0.3)
#Bar Chart Styling
barchart.update_layout(
    bargap = 0.1,
    font = dict(
        family = "Roboto Mono",
        size = 16,
    ),
    title_font_size = 25,
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
    
)


#Defining the layout
app.layout = html.Div([
    html.Div(children = [
        html.H1(
            children = "Sentiment Analysis for Businesses", style= {"margin": 0}),
        html.H3(
            children = "Using Natural Language Processing to determine" 
            " if Tweets made are negative, neutral or positive" 
            " to determine the people's sentiment on certain products or services!"
            )], style = {
                'textAlign' : 'center',
                'color': colors["text"],
                'font': 'Roboto Mono'
                }),
        
        dcc.Graph(id = "barchart", figure = barchart, config={"displayModeBar": False}),
        
    html.Div([
        html.Div(children = [
            dcc.Graph(id = "piechart", figure = piechart, config={"displayModeBar": False})
        ], style={'padding': 50, 'flex': 1, "margin": 0}),

        html.Div(children = [
                html.H1(children = "Total Number of Tweets Scraped"),
                html.H1(children = sumOfTweets)
            ], style={'padding': 50, 'flex': 1, 'textAlign': 'center', 'color': colors["text"], 'fontSize': '40'}),
            
        
    ], style={'display': 'flex', 'flex-direction': 'row', 'height' : '56vh'}),
        

], style = {'backgroundColor': colors["background"]})

        

#Run the Dashboard on Local Host
if __name__ == "__main__":
    app.run_server(debug=True)
