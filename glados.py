import os
import requests
​
# 获取JD_COOKIE环境变量
cookies = os.environ.get('gladosCookie')
​
# 将多个Cookie分割成列表
cookies_list = cookies.split('n/')
# 输出有几个Cookie
print(f"总共有 {len(cookies_list)} 个Cookie。")
​
​
# 目标URL
url = "https://glados.rocks/api/user/checkin"
# 要发送的数据
data = '{"token":"glados.one"}'
​
# 初始化响应列表
responses = []
​
# 使用索引遍历cookies_list
for i in range(len(cookies_list)):
    current_cookie = cookies_list[i]
    headers =  {
    "Host": "glados.rocks",
    "Connection": "keep-alive",
    "Content-Length": "22",
    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Microsoft Edge\";v=\"120\"",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json;charset=UTF-8",
    "sec-ch-ua-mobile": "?0",
    "Authorization": "46715581083554895601696132823919-1000-1600",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "sec-ch-ua-platform": "\"Windows\"",
    "Origin": "https://glados.rocks",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cookie": current_cookie }
    
​
 
​
# 在此处处理 responses 列表，可以根据需求进一步操作每个账号的响应
​
​
response = requests.post(url, headers=headers, data=data)
​
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response JSON
    response_json = response.json()
    # Print the 'message' from the response
    print(f"第{i + 1}个账号")
    print("Message:", response_json.get('message'))
    #print(response_json.get('business'))
else:
    print("Request failed with status code:", response.status_code)