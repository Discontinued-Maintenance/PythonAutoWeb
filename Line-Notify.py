import requests

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
    }
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code
    
# 修改為你要傳送的訊息內容
message = 'n••••••••••••••••••••••••••••••••••\n 123456'
# 修改為你的權杖內容
token = ''

lineNotifyMessage(token, message)