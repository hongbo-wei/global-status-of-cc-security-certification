import requests

# 取得Token
def get_access_token():
    # API網址
    url = "https://account.kkbox.com/oauth2/token"

    # 標頭
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "account.kkbox.com"
    }
    # 參數
    data = {
        "grant_type": "client_credentials",
        "client_id": "貼上ID內容",
        "client_secret": "貼上Secret內容"
    }
    access_token = requests.post(url, headers=headers, data=data)
    return access_token.json()["access_token"]

# 取得該音樂排行榜的歌曲列表
def get_charts_tracks(chart_id):
    access_token = get_access_token()
    url = "https://api.kkbox.com/v1.1/charts/" + chart_id + "/tracks"
    headers = {
        "accept": "application/json",
        "authorization": "Bearer " + access_token
    }
    params = {
        "territory": "TW"
    }
    response = requests.get(url, headers=headers, params=params)
    result = response.json()["data"]
    return result