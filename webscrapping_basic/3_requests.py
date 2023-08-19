import requests as rq
res = rq.get("http://google.com")
# res = rq.get("http://nadocoding.tistory.com")
res.raise_for_status()
# print("reply code :", res.status_code) # 200이면 정상

# if res.status_code == rq.codes.ok:
#     print("Everything is Nominal")
# else:
#     print("ther is a problem. [ErrorCode ", res.status_code, "]")

with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)