class Solution:
    def isValid(self, s: str) -> bool:
        stock = []
        close_open = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c in close_open:
                if stock and stock[-1] == close_open[c]:
                    stock.pop()
                else:
                    return False
            else:
                stock.append(c)

        return True if not stock else False