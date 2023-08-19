import requests as rq
res = rq.get("http://naver.com")
print("reply code :", res.status_code) # 200이면 정상

if res.status_code == rq.codes.ok:
    print("Everything is Nominal")