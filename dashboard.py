import pandas as pd
import dash
from dash import dcc, html, Input, Output, State
import plotly.express as px

# Load and prepare the data
data = pd.read_excel(
    "C://Users//jtani//Downloads//sampledatafoodsales//sampledatafoodsales.xlsx",
    sheet_name='FoodSales'
)
data['Date'] = pd.to_datetime(data['Date'])
data['Month'] = data['Date'].dt.to_period('M').astype(str)

# For animated top products, find the ten top products overall first
all_time_top = data.groupby('Product')['TotalPrice'].sum().nlargest(10).index.tolist()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H2("Food Sales Dashboard"),

    dcc.DatePickerRange(
        id='date-picker',
        min_date_allowed=data['Date'].min(),
        max_date_allowed=data['Date'].max(),
        start_date=data['Date'].min(),
        end_date=data['Date'].max()
    ),

    dcc.Tabs([
        # Animated Sales by Region tab
        dcc.Tab(label='Sales by Region', children=[
            dcc.Graph(id='region-animated-graph')
        ]),

        # Sales by Category tab (animated)
        dcc.Tab(label='Sales by Category', children=[
            dcc.Dropdown(
                options=[{'label': c, 'value': c} for c in data['Category'].unique()],
                value=data['Category'].unique().tolist(),
                multi=True,
                id='category-dropdown'
            ),
            dcc.Graph(id='category-graph')
        ]),

        # Animated Top 10 Products tab with Download option
        dcc.Tab(label='Top 10 Products', children=[
            html.Div([
                dcc.Graph(id='products-animated-graph'),
                html.Button("⬇️ Download Current View (CSV)", id="btn-download-csv"),
                dcc.Download(id="download-dataframe-csv")
            ])
        ])
    ])
])

# ANIMATED Sales by Region over time
@app.callback(
    Output('region-animated-graph', 'figure'),
    [Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date')]
)
def update_region_animated_chart(start_date, end_date):
    filtered = data[
        (data['Date'] >= start_date) & 
        (data['Date'] <= end_date)
    ].copy()
    region_monthly = filtered.groupby(['Month', 'Region'])['TotalPrice'].sum().reset_index()
    fig = px.bar(
        region_monthly,
        x='Region',
        y='TotalPrice',
        color='Region',
        animation_frame='Month',
        range_y=[0, region_monthly['TotalPrice'].max() * 1.1],
        title='Sales by Region Over Time',
        text_auto=True,
        labels={'TotalPrice': 'Total Sales', 'Region': 'Region', 'Month': 'Month'},
        color_discrete_sequence=px.colors.sequential.Plasma
    )
    fig.update_layout(
        plot_bgcolor='rgba(240,240,240,0.5)',
        xaxis_title='<b>Region</b>',
        yaxis_title='<b>Total Sales (₹)</b>',
        font=dict(size=14, family="Arial"),
        bargap=0.2
    )
    return fig

# Animated Sales by Category over time
@app.callback(
    Output('category-graph', 'figure'),
    [Input('category-dropdown', 'value'),
     Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date')]
)
def update_category_chart(categories, start_date, end_date):
    filtered = data[
        (data['Category'].isin(categories)) &
        (data['Date'] >= start_date) &
        (data['Date'] <= end_date)
    ].copy()
    summary = filtered.groupby(['Month', 'Category'])['TotalPrice'].sum().reset_index()
    fig = px.bar(
        summary,
        x='Category',
        y='TotalPrice',
        color='Category',
        animation_frame='Month',
        range_y=[0, summary['TotalPrice'].max()*1.1],
        title='Sales by Category Over Time',
        text_auto=True,
        labels={'TotalPrice': 'Total Sales', 'Category': 'Category', 'Month': 'Month'},
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    fig.update_layout(
        plot_bgcolor='rgba(250,250,250,0.5)',
        font=dict(size=13, family="Arial")
    )
    return fig

# Animated Top 10 Products chart
@app.callback(
    Output('products-animated-graph', 'figure'),
    [Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date')]
)
def update_products_animated_chart(start_date, end_date):
    filtered = data[
        (data['Date'] >= start_date) &
        (data['Date'] <= end_date) &
        (data['Product'].isin(all_time_top))
    ].copy()
    prod_monthly = filtered.groupby(['Month', 'Product'])['TotalPrice'].sum().reset_index()
    fig = px.bar(
        prod_monthly,
        x='TotalPrice',
        y='Product',
        color='Product',
        animation_frame='Month',
        orientation='h',
        range_x=[0, prod_monthly['TotalPrice'].max() * 1.1 if not prod_monthly.empty else 1],
        title='Top 10 Products by Sales Over Time',
        text_auto=True,
        labels={'TotalPrice': 'Total Sales', 'Product': 'Product', 'Month': 'Month'},
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig.update_layout(
        plot_bgcolor='rgba(245,245,245,0.5)',
        font=dict(size=13, family="Arial"),
        yaxis=dict(autorange="reversed")  # Keeps products in descending order
    )
    return fig

# Data Download Callback for Top Products
@app.callback(
    Output("download-dataframe-csv", "data"),
    Input("btn-download-csv", "n_clicks"),
    State('date-picker', 'start_date'),
    State('date-picker', 'end_date'),
    prevent_initial_call=True
)
def download_data(n_clicks, start_date, end_date):
    # Only export the monthly sales of top 10 products in the selected date range
    filtered = data[
        (data['Date'] >= start_date) & 
        (data['Date'] <= end_date) &
        (data['Product'].isin(all_time_top))
    ][['Month', 'Product', 'TotalPrice']]
    export = filtered.groupby(['Month', 'Product'])['TotalPrice'].sum().reset_index()
    return dcc.send_data_frame(export.to_csv, "animated_top10_products.csv", index=False)

if __name__ == '__main__':
    app.run(debug=True)
