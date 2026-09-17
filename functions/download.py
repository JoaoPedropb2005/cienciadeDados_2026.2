import pandas as pd
import yfinance as yf

def download_data(
        tickers:str,
        multi_level_index:bool
) -> pd.DataFrame:

    """
    Download the data from yahoo finance

    Args:
        tickers(str): The ticker.
        multi_level_index(bool): Remove/include row indexes.
    """
    
    return yf.download(
        tickers = 'AAPL',
        multi_level_index = False
    ).reset_index()