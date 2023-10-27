class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        while n>1:  #因為1是2^0不用再除了
            if n%2!=0:  #餘數不是0
                return False    #失敗
            n=n//2
        #經過上面check後，都沒出錯的話
        return True #就成功