import re
# ca?e
# care, cafe, case, cave



p = re.compile("ca.e") 
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (O) | caffe (X)
# ^ (^de) : 문자열의 시작 > desk, destination (O) | fade (X)
# $ (se$) : 문자열의 끝 > case, base (O) | face (X)

m = p.match("case")
print(m.group()) # 매치되지 않으면 에러가 발생