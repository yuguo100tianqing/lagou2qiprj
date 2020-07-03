class Calculator():
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def dev(self, x, y):
        try:
            de = x / y
            return de
        except ZeroDivisionError:
            return "除数不能为0"
# cal=Calculator()
# print(cal.add(1,2))
# print(cal.sub(1,2))
# print(cal.mul(1,3))
# print(cal.dev(1,3))
# print(cal.dev(2,0))
