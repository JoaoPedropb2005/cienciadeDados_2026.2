from plotly.graph_objects import Figure
from functions.download import download_data
import plotly.express as px


def plot_history(ticker:str) -> Figure: 
    """
    Plot historical data from Yahoo Finance

    Args:
        ticker(str): The ticker
    """
    df = download_data(ticker, False)
    return px.line(
        df, 
        x = 'Date',
        y = 'Close',
        title = f'{ticker} stock price'
    )