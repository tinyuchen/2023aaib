class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d={}
        for c in s:
            if c in d:
                d[c]=d[c]+1
            else:
                d[c]=1
        print(d)        #可以印看看，字母出現的次數統計結果

        for c in t:
            if c not in d:      #沒出現過 -> 就是它
                return c        #找到多出的字母了
            if d[c]==0:      #字母用光了，不夠用 -> 就是它
                return c        #找到多出的字母了
            else:
                d[c]=d[c]-1     #減一
        return""        #這行沒寫也沒關係，因為題目保證在前面就找到答案了
    