# Chapter 1
Python Advanced(1) - Python Variable Scope   
Keyword - scope, global, nonlocal, locals, globals..

전역변수는 주로 변하지 않는 고정 값에 사용   

### 지역변수 사용 이유 
- 지역변수는 함수 내에 로직 해결에 국한, 소멸주기 함수 실행 해제 시 전역변수를 지역내에서 수정되는 것은 권장X

## Ex1
```python
a = 10 # Global variable

def foo():
    # Read global variable
    print('Ex1 > ', a) 

foo()
# Read global variable
print('Ex1 > ', a)  
```
-> 전역변수는 지역에서 읽을 수 있음

## Ex2
```python
b = 20

def bar():
    b = 30              # Local variable
    print('Ex2 > ', b)  # Read local variable

bar() 

print('Ex2 > ', b)      # Read global variable
```
-> 지역스코프에서 선언하면 지역스코프 밖으로 가면 적용이 안됨
## Ex3
```python
c = 40

def foobar():
    # c = c + 10   # UnboundLocalError
    # c = 10
    # c += 100
                 
    print('Ex3 > ', c)          

foobar()       
```
-> 전역변수는 지역에서 사용이 불가능! (읽기만 가능)

## Ex4
```python
d = 50
def barfoo():
    global d     
                 
    d = 60       
    print('Ex4 > ', d)

barfoo()   

print('Ex4 > ', d)        
 # Prints 5. Global variable d was modified within barfoo()
``` 
-> 전역변수를 지역에서 사용하고 싶다면 global이라는 예약어를 사용하면 된다.   


**하지만 global 선언을 지양하자. 전역변수가 어딘가의 지역에서 변화가 일어나면 나중에 찾기 힘들 수 있음 ㅇㅅㅇ**

## Ex5(중요)
```python
def outer():
    e = 70
    def inner():
        nonlocal e    
        e += 10 # e = e + 10 
        print('Ex5 > ', e)
    return inner

in_test = outer() # Closure

in_test()          
in_test()         
```
클로져 형태 - 간단히 말하면함수의 호출이 끝나도 함수 안의 변수의 값이 계속 기억되는 형태!   
참고 -https://wikidocs.net/134789

-> 지역스코프 안의 지역변수를 그 하위의 지역스코프에서 사용하기 위해서는 nonlocal이라는 예약어를 사용하여 수정이 가능하다.
## Ex6
```python
def func(var): 
    x = 10 
    def printer():
        print('Ex5 > ', "Printer Func Inner") 
    print('Func Inner', locals()) # 지역 전체 출력

func("Hi")
```
-> locals() 함수는 해당 영역에 존재하는 모든 것을 딕셔너리 형태로 가져올 수 있음!
## Ex7
```python
print('Ex7 >', globals()) # 전역 전체 출력
globals()['test_variable'] = 100
print('Ex7 >', globals())
```
-> globals() 함수는 모든 전역 값들을 딕셔너리 형태로 볼 수 있음   
-> 딕셔너리 형태이니 2번째 줄과 같이 전역변수를 지정 할 수 있음!
## Ex8(지역 -> 전역 변수 작성)
```python
for i in range(1, 10): 
    for k in range(1, 10): 
        globals()['plus_{}_{}'.format(i, k)] = i + k 

print(plus_3_5) 
print(plus_9_9)
```
-> Ex7 같은 형태를 알고 있으면 지역스코프에서도 전역변수를 선언 할 수 있음! 고급 기술임 ㅇㅇ