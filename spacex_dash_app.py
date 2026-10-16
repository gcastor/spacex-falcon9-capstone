"""SpaceX launch records dashboard.

Run:  pip install dash pandas plotly
      python spacex_dash_app.py      then open http://127.0.0.1:8050
"""
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

spacex_df = pd.read_csv("data/dataset_part_2.csv")
spacex_df["Booster Version Category"] = "Block " + spacex_df["Block"].astype(int).astype(str)
max_payload = spacex_df["PayloadMass"].max()
min_payload = spacex_df["PayloadMass"].min()

site_options = [{"label": "All Sites", "value": "ALL"}] + [
    {"label": s, "value": s} for s in sorted(spacex_df["LaunchSite"].unique())
]

app = Dash(__name__)
app.layout = html.Div(children=[
    html.H1("SpaceX Launch Records Dashboard",
            style={"textAlign": "center", "color": "#503D36", "font-size": 40}),
    # TASK 1: launch site dropdown
    dcc.Dropdown(id="site-dropdown", options=site_options, value="ALL",
                 placeholder="Select a Launch Site here", searchable=True),
    html.Br(),
    # TASK 2: success pie chart
    html.Div(dcc.Graph(id="success-pie-chart")),
    html.Br(),
    html.P("Payload range (Kg):"),
    # TASK 3: payload range slider
    dcc.RangeSlider(id="payload-slider", min=0, max=16000, step=1000,
                    marks={i: str(i) for i in range(0, 16001, 2000)},
                    value=[min_payload, max_payload]),
    # TASK 4: payload vs outcome scatter
    html.Div(dcc.Graph(id="success-payload-scatter-chart")),
])


@app.callback(Output("success-pie-chart", "figure"), Input("site-dropdown", "value"))
def get_pie_chart(entered_site):
    if entered_site == "ALL":
        success = spacex_df[spacex_df["Class"] == 1]
        return px.pie(success, names="LaunchSite", title="Total Successful Launches by Site")
    site_df = spacex_df[spacex_df["LaunchSite"] == entered_site]
    counts = site_df["Class"].value_counts().rename({1: "Success", 0: "Failure"}).reset_index()
    counts.columns = ["Outcome", "Count"]
    return px.pie(counts, values="Count", names="Outcome",
                  title=f"Total Success vs Failure for site {entered_site}")


@app.callback(Output("success-payload-scatter-chart", "figure"),
              [Input("site-dropdown", "value"), Input("payload-slider", "value")])
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    df = spacex_df[(spacex_df["PayloadMass"] >= low) & (spacex_df["PayloadMass"] <= high)]
    title = "Correlation between Payload and Success for all Sites"
    if entered_site != "ALL":
        df = df[df["LaunchSite"] == entered_site]
        title = f"Correlation between Payload and Success for {entered_site}"
    return px.scatter(df, x="PayloadMass", y="Class", color="Booster Version Category",
                      hover_data=["LaunchSite", "Serial"], title=title)


if __name__ == "__main__":
    app.run(debug=False)
