def bollinger_band_plot(ticker, startDate, endDate, MA_Period=20, stdev_default=2):
    """
    :param ticker: stock ticker from Yahoo finance
    :param startDate: start date in YYYY-MM-DD
    :param endDate: end date in YYYY-MM-DD
    :param MA_Period: moving average window period
    :param stdev_default: number of standard deviation in default
    :return: plot
    """
    import numpy as np
    import matplotlib.pyplot as plt
    import warnings
    warnings.filterwarnings('ignore')
    import pandas_datareader.data as web
    import pandas
    from pandas_datareader import data as pdr
    import yfinance as yfin
    yfin.pdr_override()

    stockDF = pdr.get_data_yahoo({ticker}, start={startDate}, end={endDate})['Close']
    stockDF.columns = {'Close Price'}
    stockDF.head()

    meanPrice = stockDF.rolling(MA_Period).mean()
    meanPrice = np.round(meanPrice, 3)
    stdev = stockDF.rolling(MA_Period).std()
    stdev = np.round(stdev, 3)
    upperBand = meanPrice + stdev_default * stdev
    upperBand = np.round(upperBand, 3)
    lowerBand = meanPrice - stdev_default * stdev
    lowerBand = np.round(lowerBand, 3)

    stockDF.plot(c='k', figsize=(20, 10), lw=2, fontsize=12)
    meanPrice.plot(c='b', figsize=(20, 10), lw=1)
    upperBand.plot(c='g', figsize=(20, 10), lw=1)
    lowerBand.plot(c='r', figsize=(20, 10), lw=1)

    plt.title('Bollinger Bands: {}'.format(ticker), fontsize=20)
    plt.ylabel("Price in USD ($)", fontsize=15)
    plt.xlabel("Date", fontsize=15)
    plt.legend()
    plt.grid()
    plt.show()