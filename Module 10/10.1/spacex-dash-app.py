# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown',
                                            options=[
                                                {'label': 'All Sites', 'value': 'ALL'}
                                            ] + [
                                                {'label': site, 'value': site}
                                                for site in spacex_df['Launch Site'].unique()
                                            ],
                                            value='ALL',
                                            placeholder="Select a Launch Site here",
                                            searchable=True
                                            ),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',
                                                min=0, max=10000, step=1000,
                                                marks={0: '0',
                                                       2500: '2500',
                                                       5000: '5000',
                                                       7500: '7500',
                                                       10000: '10000'},
                                                value=[min_payload, max_payload]),
                                html.Br(),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        # Show total success launches count for all sites
        fig = px.pie(spacex_df,
                    values='class',
                    names='Launch Site',
                    title='Total Success Launches by Site')
        return fig
    else:
        # return the outcomes piechart for a selected site
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        fig = px.pie(filtered_df,
                    names='class',
                    title=f'Success vs Failed Launches for {entered_site}')
        return fig

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'),
               Input(component_id="payload-slider", component_property="value")])
def get_scatter_chart(entered_site, payload_range):
    filtered_df = spacex_df[
        (spacex_df['Payload Mass (kg)'] >= payload_range[0]) &
        (spacex_df['Payload Mass (kg)'] <= payload_range[1])
    ]
    if entered_site == 'ALL':
        fig = px.scatter(filtered_df,
                        x='Payload Mass (kg)',
                        y='class',
                        color='Booster Version Category',
                        title='Correlation between Payload and Success for all Sites')
        return fig
    else:
        # Filter for selected site
        filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]
        fig = px.scatter(filtered_df,
                        x='Payload Mass (kg)',
                        y='class',
                        color='Booster Version Category',
                        title=f'Correlation between Payload and Success for {entered_site}')
        return fig
    

@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [
        Input(component_id='site-dropdown', component_property='value'),
        Input(component_id='payload-slider', component_property='value')
    ]
)
def get_scatter_chart(entered_site, slider_values):

    # Filter by launch site
    if entered_site == 'ALL':
        filtered_df = spacex_df
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]

    max_count = (
        filtered_df
        .groupby(['Booster Version Category', 'class'])['class']
        .count()
        .max()
    ) + 1

    # Filter by payload mass range
    filtered_df = filtered_df[
        (filtered_df['Payload Mass (kg)'] >= slider_values[0]) &
        (filtered_df['Payload Mass (kg)'] <= slider_values[1])
    ].copy()

    # Prepare summary data
    summary_df = (
        filtered_df
        .groupby(['Booster Version Category', 'class'])
        .size()
        .reset_index(name='Count')
    )

    summary_df['Launch Outcome'] = summary_df['class'].map({
        0: 'Failure',
        1: 'Success'
    })

    payload_range = f"{slider_values[0]} - {slider_values[1]} kg"
    site_label = 'All Sites' if entered_site == 'ALL' else f"Site {entered_site}"

    fig = px.bar(
        summary_df,
        x='Booster Version Category',
        y='Count',
        color='Launch Outcome',
        color_discrete_map={'Failure': 'red', 'Success': 'blue'},
        title=(
            f"Launch Outcomes by Booster Version "
            f"with Payload Mass Ranging {payload_range} "
            f"for {site_label}"
        ),
        barmode='group'
    )

    fig.update_yaxes(range=[0, max_count])

    return fig
``
# Run the app
if __name__ == '__main__':
    app.run(debug=True)