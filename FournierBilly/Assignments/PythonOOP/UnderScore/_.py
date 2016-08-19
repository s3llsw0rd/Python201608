class Underscore(object):
    def map(self,arr, iteratee):
        return [iteratee(ele) for ele in arr]

    def reduce(self, arr, iteratee, memo=None):
        for index, ele in enumerate(arr):
            if not memo:
                memo = ele
            else:
                memo = iteratee(memo, ele, index)
        return memo

    def find(self, arr, predicate):
        for ele in arr:
            if predicate(ele):
                return ele
        return None

    def filter(self, arr, predicate):
        ret = []
        for ele in arr:
            if predicate(ele):
                ret.append(ele)
        return ret

    def reject(self, arr, predicate):
        ret = []
        for ele in arr:
            if not predicate(ele):
                ret.append(ele)
        return ret

_ = Underscore()
print _.map([1, 2, 3], lambda num : num * 3)
print _.reduce([1, 2, 3], lambda memo, num, index : memo + num, 0)
print _.find([1, 2, 3, 4, 5, 6], lambda num : num % 2 == 0 )
print _.filter([1, 2, 3, 4, 5, 6], lambda num : num % 2 == 0 )
print _.reject([1, 2, 3, 4, 5, 6], lambda num : num % 2 == 0 )
