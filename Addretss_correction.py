def address_correction(str_input):
    return str_input
# A Dynamic Programming based Python program for edit 
# distance problem 
def EditDistDP(str1, str2):
     
    len1 = len(str1)
    len2 = len(str2)

    DP = [[0 for i in range(len1 + 1)]
             for j in range(2)];
 
    for i in range(0, len1 + 1):
        DP[0][i] = i

    for i in range(1, len2 + 1):

        for j in range(0, len1 + 1):

            if (j == 0):
                DP[i % 2][j] = i
 

            elif(str1[j - 1] == str2[i-1]):
                DP[i % 2][j] = DP[(i - 1) % 2][j - 1]

            else:
                DP[i % 2][j] = (1 + min(DP[(i - 1) % 2][j],
                                    min(DP[i % 2][j - 1],
                                  DP[(i - 1) % 2][j - 1])))
    return DP[len2 % 2][len1]
 
# Driver code
if __name__ == '__main__':
     
    str1 = "a"
    str2 = "hat"
     
    print(EditDistDP(str1, str2))