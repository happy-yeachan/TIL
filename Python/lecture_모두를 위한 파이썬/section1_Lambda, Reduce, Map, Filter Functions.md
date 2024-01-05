# Chapter 1
Python Advanced(1) - Lambda, Reduce, Map, Filter Functions   
Keyword - lambda, map, filter, reduce

lambda 장점 : 익명, 힙 영역 사용 즉시 소멸, pythonic?, 파이썬 가비지 컬렉션(Count = 0)   
일반함수 : 재사용성 위해 메모리 저장   
시퀀스형 전처리에 Reduce, Map, Filter 자주 사용

## Ex1-lamda
```python
cul = lambda a, b, c: a * b + c

print('Ex1 >', cul(10, 15, 20))
```
-> lamda는 쉽게말해 함수를 간단하게 사용 가능하게 함
-> def로 선언한 함수와 다르게 람다 함수는 힙 영역에서 곧바로 사라져 카비지 컬렉션에서 처리할 필요가 없어 메모리 효율에 좋음
## Ex2-map
```python
digits1 = [x * 10 for x in range(1, 11)]
print('Ex2 >', digits1)

# def ex2_func(x):
#     return x **2

## result = list(map(ex2_func , digits))
result = list(map(lambda i: i ** 2 , digits1))

print('Ex2 >', result)

def also_square(nums):
    def double(x):
        return x ** 2
    return map(double, nums)

print('Ex2 >', list(also_square(digits1)))
```
- map함수는 시퀸스 형태에 많이 사용됨
- 2개의 인자를 받는데 앞에선 함수형 뒤는 리스트형을 넣어 동작함
- 각 리스트의 요소를 다 돌며 함수를 실행하는 형태
- 완료된 형태는 다시 list로 형변환 하여 사용해야함!
## Ex3-filter
```python
digits2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(filter(lambda x: x % 2 == 0, digits2))

print('Ex3 >', result)

def also_evens(nums):
    def is_even(x):
        return x % 2 == 0
    return filter(is_even, nums)

print('Ex3 >', list(also_evens(digits2)))
```
- filter함수도 2개의 인자를 받음
- 앞 수식에 참인 요소들만 뽑아주는 기능을 함.
- 이도 map과 마찬가지로 다시 list로 형변환을 해주어 사용해야함!
## Ex4-reduce
```python
from functools import reduce

digits3 = [x for x in range(1, 101)]

result = reduce(lambda x, y: x+y, digits3)

print('Ex4 >', result)

def also_add(nums):
    def add_plus(x, y):
        return x + y
    return reduce(add_plus, nums)

print('Ex3 >', also_add(digits3))
```
- reduce는 집계함수로 리스트의 총 합을 구할 때 자주 사용함.
- 이는 from functools import reduce를 해주어 사용해야 함.