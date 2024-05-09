# -*- coding: utf-8 -*-
from functools import reduce
import operator


class SimpleCalculator:
    def add(self,*args):
        return sum(args)
    
    def sub(self, a, b):
        return a - b
    
    def mul(self, *args):
        if not all(args):
            raise ValueError
        
        return reduce(operator.mul, args)
    
    def div(self,a,b):
        try:
            return a / b
        except ZeroDivisionError:
            return float('inf')
        
    def avg(self,lst: list,ut: int =0,lt:int=0):
        return_value=0

        if len(lst)>0:
            if ut>0:
               lst = list(filter(lambda x: x<=ut,lst))
            
            if lt>0:
               lst= list(filter(lambda x: x>=lt,lst))

            count= len(lst)

            if count > 0:
               total_sum = reduce((lambda x,y:x+y),lst)
               return_value = round(float(total_sum/count),2)
        
        return return_value