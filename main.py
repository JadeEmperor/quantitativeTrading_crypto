import requests
import pandas as pd
pd.set_option("expand_frame_repr", False)

def get_single_ticker_data(symbol):
    # """
    #     单个交易对的ticker数据获取
    # """
    ticker_url = "https://api.binance.com/api/v3/ticker/24hr?symbol={}".format(symbol)
    try:
        res_obj = requests.get(ticker_url, timeout=15)
    except Exception as e:
        print("错误", e)
        return None

    # json_obj = res_obj.json()
    # raw_df = pd.DataFrame(json_obj)

    raw_df = None

    if res_obj.status_code == 200:
        json_obj = res_obj.json()
        if "error_code" in json_obj:
            print("错误码：{}".format(json_obj["error_code"]))
        else:
            raw_df = pd.DataFrame(json_obj)
            data = [[json_obj[k] for k in json_obj]]
            raw_df = pd.DataFrame(data, columns=json_obj.keys())
            # melted_df = pd.melt(raw_df, value_vars=['lastPrice', 'bidPrice', 'askPrice'], var_name='price_type', value_name='price')

        return(raw_df)
    else:
        print("状态码：{}".format(res_obj.status_code))





def main():
    # """
    # 主函数
    # """
    # 获取单个交易对数据
    #     处理
    symbol = "BTCUSDT"
    ticker_df = get_single_ticker_data(symbol)
    print(ticker_df)

    # 获取多个交易对数据
    #     处理

    # 获取交易对K线信息 
    #     单个获取
    #     多个获取

if __name__ == '__main__':
    main()

