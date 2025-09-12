class Solution(object):
    def intToRoman(self, num):
        hashMap = {1000:'M',500:'D',100:'C',50:'L',10:'X',5:'V',1:'I'}

        ans =[] ; dig = 0
        if num in hashMap : return hashMap[num]
        while num > 0 :
            cur = (num%10) * pow(10,dig)
            res = ""
            if cur:
                if cur in hashMap : res += hashMap[cur]
                elif   pow(10,dig) <= cur <= 3*pow(10,dig):
                    res += hashMap[pow(10,dig)] * (cur/(10**dig))
                elif  6*pow(10,dig)<= cur <= 8*pow(10,dig):
                    res += hashMap[5*(10**dig)] +  ((cur/(10**dig))-5) * hashMap[1*(10**dig)]
                elif cur == 9*pow(10,dig) :
                    res += hashMap[pow(10,dig)] + hashMap[pow(10,(dig+1))]
                elif  cur == 4*pow(10,dig):
                    res += hashMap[pow(10,dig)] + hashMap[5*pow(10,(dig))]
                
            if res : ans.append(res)
            num //= 10
            dig += 1
        return "".join(ans[::-1]) 