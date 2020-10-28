class Solution:
    def defangIPaddr(self, address: str) -> str:
        a = []
        for i,e in enumerate(address):
            if e == ".":
                a.append('[.]')
            else:
                a.append(e)
            b = ''.join(a)
        return b;
