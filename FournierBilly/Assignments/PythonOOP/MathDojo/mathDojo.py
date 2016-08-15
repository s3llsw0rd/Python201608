class MathDojo(object):
    def __init__(self):
        self.value = 0

    def add(self, num,*args):
        if hasattr(num,'__iter__'):
            for ele in num:
                self.add(ele)
        else:
            self.value += num

        if not args: return self

        for item in args:
            if not isinstance(item, (float,int,list)): continue
            if hasattr(item,'__iter__'):
                for ele in item:
                    self.add(ele)
            else:
                self.value += item
        return self

    def sub(self, num, *args):
        if hasattr(num,'__iter__'):
            for ele in num:
                self.sub(ele)
        else:
            self.value -= num

        if not args: return self

        for item in args:
            if not isinstance(item, (float,int,list)): continue
            if hasattr(item,'__iter__'):
                for ele in item:
                    self.sub(ele)
            else:
                self.value -= item

        print 'self.value: ', self.value
        return self

md = MathDojo()
print md.add([1,2,3],4,[5,[6,7]]).value # 28
print md.add([1,2,3],4,[5,[6,7]]).sub(1,[2,[3,4]]).value # 18
