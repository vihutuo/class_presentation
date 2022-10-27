import requests
import pandas
api_key="jiFu34s"
timeout=5
appid=2
def Init(aid):
    global appid
    appid=aid
def Getappid():
    return appid
def GetTokens(student_id):
    URL = "https://cp.lshss.xyz/get_tokens.php"
    PARAMS = {'student_id':student_id,"api_key":api_key}
    r = requests.get(url = URL, params = PARAMS,timeout=timeout)
    data = r.json()
    return data["tokens"]
def AddTokens(student_id,token_amount,description):
    URL = "https://cp.lshss.xyz/add_tokens.php"
    data = {'student_id':student_id,"api_key":api_key,"token_amount":token_amount,"description":description,"appid":appid}
    r = requests.post(url = URL, data = data,timeout=timeout)
    data = r.json()
    return data
def AddScore(player_name,score):
    URL = "https://cp.lshss.xyz/add_app_score.php"
    data = {'player_name':player_name,"api_key":api_key,"score":score,"appid":appid}
    r = requests.post(url = URL, data = data,timeout=timeout)
    data = r.json()
    return data
def GetScores(limit):
    URL = "https://cp.lshss.xyz/get_app_scores.php"
    PARAMS = {'appid':appid,"limit":limit}
    r = requests.get(url = URL, params = PARAMS,timeout=timeout)
    data = r.json()
    return data
def GetTokenTransactions(student_id):
    URL = "https://cp.lshss.xyz/get_token_transactions.php"
    PARAMS = {'student_id':student_id}
    r = requests.get(url = URL, params = PARAMS,timeout=timeout)
    
    data = r.json()
    return data
def ShowScoreBoard(limit):
    L1 = GetScores(limit)
    df=pandas.DataFrame(L1,columns=["Name","Score"])
    df.index +=1
    #print(data.to_string(index=False))
    #display(HTML(df.to_html(index=False))) Use this to display without first index col
    display(df)
def ShowTokenTransactions(student_id):
    L1 = GetTokenTransactions(student_id)
    #print(L1)
    df=pandas.DataFrame(L1,columns=["Date","Amount","Description","Appid"])
    df.index +=1
    #print(data.to_string(index=False))
    #display(HTML(df.to_html(index=False))) Use this to display without first index col
    display(df)
def ShowRecentTokenTransactions(limit=20):
    L1 = GetRecentTokenTransactions(limit)
    #print(L1)
    df=pandas.DataFrame(L1)
    df.index +=1
    #print(data.to_string(index=False))
    #display(HTML(df.to_html(index=False))) #Use this to display without first index col
    display(df)
def ShowTotalTokensIssued():
    L1 = GetTotalTokensIssued()
    #print(L1)
    df=pandas.DataFrame(L1)
    df.index +=1
    #print(data.to_string(index=False))
    #display(HTML(df.to_html(index=False))) Use this to display without first index col
    df["total"] = pandas.to_numeric(df["total"])
    #df.append(pandas.DataFrame(df.MyColumn.sum(), index = ["total"], columns=["MyColumn"]))
    #df.loc["Total", "total"] = df.total.sum()
    display(df)
    Total = df['total'].sum()
    print("Grand Total : ",Total)
    
def GetStudentDetails(student_id):
    URL = "https://cp.lshss.xyz/get_student_details.php"
    PARAMS = {'student_id':student_id}
    r = requests.get(url = URL, params = PARAMS,timeout=timeout)
    data = r.json()
    return data
def GetRecentTokenTransactions(limit=20):
    URL = "https://cp.lshss.xyz/get_recent_token_transactions.php"
    PARAMS = {'limit':limit}
    r = requests.get(url = URL, params = PARAMS,timeout=timeout)
    
    data = r.json()
    return data
def GetTotalTokensIssued():
    URL = "https://cp.lshss.xyz/get_total_tokens_issued.php"
    PARAMS = {}
    r = requests.get(url = URL, params = PARAMS,timeout=timeout)
  
    data = r.json()
    return data
#print(GetTotalTokensIssued())
#ShowTotalTokensIssued()
#print(AddTokens(500,20,"Winner"))
#print(GetTokenTransactions(1))
#ShowTokenTransactions(1)
#print(AddScore("Op",55))  
#ShowScoreBoard(6)
#print(GetStudentDetails(5))
#print(GetTokenTransactions(20))
#print(GetRecentTokenTransactions(20))
#ShowRecentTokenTransactions()