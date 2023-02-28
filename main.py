import requests
import pandas as pd

def get_single_ticker_data(symbol):
    # """
    #     单个交易对的ticker数据获取
    # """
    ticker_url = "https://api.binance.com/api/v3/ticker/24hr?symbol={}".format(symbol)
    res_obj = requests.get(ticker_url)
    # json_obj = res_obj.json()
    # raw_df = pd.DataFrame(json_obj)

    json_obj = res_obj.json()
    data = [[json_obj[k] for k in json_obj]]
    raw_df = pd.DataFrame(data, columns=json_obj.keys())
    melted_df = pd.melt(raw_df, value_vars=['lastPrice', 'bidPrice', 'askPrice'], var_name='price_type', value_name='price')



    print(melted_df)

def main():
    # """
    # 主函数
    # """
    # 获取单个交易对数据
    #     处理
    symbol = "BTCUSDT"
    ticker_df = get_single_ticker_data(symbol)

    # 获取多个交易对数据
    #     处理

    # 获取交易对K线信息 
    #     单个获取
    #     多个获取

if __name__ == '__main__':
    main()

