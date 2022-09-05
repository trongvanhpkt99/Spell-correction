phuongxa=open("Dictionary/dict_phuongxa.txt", 'r',encoding="utf-8").read().split('\n')
quanhuyen=open("Dictionary/dict_quanhuyen.txt", 'r',encoding="utf-8").read().split('\n')
tinhtp=open("Dictionary/dict_thanhpho.txt", 'r',encoding="utf-8").read().split('\n')
output=open("loi.txt", 'a',encoding="utf-8")
for i in range (len(phuongxa)):
    output.write(', '.join((phuongxa[i],quanhuyen[i],tinhtp[i]))+'\n')
