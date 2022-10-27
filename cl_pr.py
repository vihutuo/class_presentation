import requests
import pandas
api_key="jiFu34s"
timeout=5
appid=0
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
def GetStudentDetails(student_id):
    URL = "https://cp.lshss.xyz/get_student_details.php"
    PARAMS = {'student_id':student_id}
    r = requests.get(url = URL, params = PARAMS,timeout=timeout)
    data = r.json()
    return data
#print(AddTokens(1,2,""))
#print(GetTokenTransactions(1))
#ShowTokenTransactions(1)
#print(AddScore("Op",55))  
#ShowScoreBoard(6)
#print(GetStudentDetails(2))