import requests

url = "https://glados.rocks/api/user/checkin"
gladosCookie = "koa:sess=eyJ1c2VySWQiOjQyNTgzMCwiX2V4cGlyZSI6MTczMTA1MjQ1MTM4MywiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=_rFG_6WWBjrMWUDragkkYKDan2M"

headers = {
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
    "Cookie": gladosCookie }

data = '{"token":"glados.one"}'

response = requests.post(url, headers=headers, data=data)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response JSON
    response_json = response.json()
    # Print the 'message' from the response
    print("Message:", response_json.get('message'))
else:
    print("Request failed with status code:", response.status_code)
