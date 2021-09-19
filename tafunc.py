import pandas as pd
import ta


def srsi_analyze(candledata):
    print("analysing")
    result = {}
    close_list = []
    
    for trade in candledata[0]:
        close_list.append(float(trade[4]))
            
    t_c = pd.Series(close_list)
    t_d = ta.momentum.stochrsi_d(t_c, window=14, smooth1=3, smooth2=3, fillna=False)
    t_k = ta.momentum.stochrsi_k(t_c, window=14, smooth1=3, smooth2=3, fillna=False)
    
    result["k%"]=t_k[len(t_k)-1]*100
    result["d%"]=t_d[len(t_d)-1]*100
    
    
    if(t_d[len(t_d)-1]*100) < 20 and (t_k[len(t_k)-1]*100) < 20:
        if t_d[len(t_d)-1] < t_k[len(t_k)-1]:
            result["signal"] = "buy"
        else:
            result["signal"] = "get ready to buy"
    elif(t_d[len(t_d)-1]*100) > 80 and (t_k[len(t_k)-1]*100) > 80:
        if t_d[len(t_d)-1] > t_k[len(t_k)-1]:
            result["signal"] = "sell"
        else:
            result["signal"] = "get ready to sell"
    else:
        result["signal"] = "hold"
        
    print("analysed")
    return result
