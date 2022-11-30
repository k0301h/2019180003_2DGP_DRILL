# 역직렬화는 아직X ==> dic=>str 이기 때문이다. pasing proccess가 필요하다.
# parsing : txt에서 해석을해서 형식을 파악

f = open('data.txt', 'r')
data = f.read()
f.close()
print(data)
