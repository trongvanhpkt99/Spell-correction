import re

def editDistDP(str1, str2, m, n):
    # Create a table to store results of subproblems
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0:
                dp[i][j] = j    # Min. operations = j
 
            elif j == 0:
                dp[i][j] = i    # Min. operations = i

            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                   dp[i-1][j],        # Remove
                                   dp[i-1][j-1])    # Replace
    return dp[m][n]

def distance (str1, str2):
    return editDistDP(str1, str2, len(str1), len(str2))
#
def load_dict(file_input):
    dictionary={}
    source=open(file_input, 'r',encoding="utf-8").read().split('\n')
    source=list(set(source))
    for i in source:
        if i not in dictionary:
            dictionary[i.lower()]=i
    return dictionary
#
def dict_correction(ip,dictionary):
    if len(ip)==0: return ip
    if ip in dictionary: 
        return ip
    else:
        max=-1
        key=""
        for i in dictionary:
            distance_value=distance(ip.strip().lower(),i)
            if (len(ip)-distance_value)/len(ip) >max:
                max= (len(ip)-distance_value)/len(ip)
                key=i
        if max >0.65:
            return dictionary[key]["value"]
    return ip.strip()

def get_err_from_str(str_input,dict):
    head=0
    tail=len(str_input)
    arr=[]
    pre_tail=0
    while(head<tail):
        sub_str=str_input[head:tail]
        if sub_str.lower() in dict:
            # print(head,tail,sub_str)
            if str_input[pre_tail:head].strip()!= '':
                arr.append(str_input[pre_tail:head])
            if sub_str.strip() != ',' and sub_str.strip() != '':
                arr.append(sub_str)
            pre_tail=tail
            head+=len(sub_str)
            tail=len(str_input)
        else:
            tail-=1
            if(head==tail and head<len(str_input)):
                head+=1
                tail=len(str_input)
    # print(head,tail,pre_tail,len(str_input))
    if str_input[pre_tail:len(str_input)].strip()!= '':
        arr.append(str_input[pre_tail:len(str_input)])
    return arr
# str_input='Số 1 ngách 29 ngõ Quỳnh, phố Bạch Mai, phường Thanh Nhân, quận Hai Bà Trưng, Hà Nội'
# diction=load_dict('Dictionary/dict_tonghop.txt')
# print(  get_err_from_str(str_input,diction))