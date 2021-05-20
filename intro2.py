import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# ---------- Import and clean data (importing csv into pandas)
# df = pd.read_csv("intro_bees.csv")
df = pd.read_csv("patient_data.csv")


print(df.groupby("detected_district").count())


# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Covid 19 updates in Kerala", style={'text-align': 'center'}),

    dcc.Dropdown(id="stats",
                 options=[
                     {"label": "Abroad", "value": "Abroad"},
                     {"label": "India", "value": "India"}],
                     multi=False,
                     value="India",
                     style={'width': "40%"}
                     ),

    

    dcc.Graph(id="bar-chart")

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    Output("bar-chart", "figure"), 
    [Input("stats", "value")])
def update_bar_chart(status):
    df1=df[df["origin_country"]==status]
    fig = px.bar(df1, x="detected_district", y="recovery_time")
    return fig

     # Plotly Graph Objects (GO)
    # fig = go.Figure(
    #     data=[go.Choropleth(
    #         locationmode='USA-states',
    #         locations=dff['state_code'],
    #         z=dff["Pct of Colonies Impacted"].astype(float),
    #         colorscale='Reds',
    #     )]
    # )
    #
    # fig.update_layout(
    #     title_text="Bees Affected by Mites in the USA",
    #     title_xanchor="center",
    #     title_font=dict(size=24),
    #     title_x=0.5,
    #     geo=dict(scope='usa'),
    # )

    


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)

    