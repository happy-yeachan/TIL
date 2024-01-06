# Python Advanced(1) - Context Manager(1) 
Keyword - Contextlib, __enter__, __exit__, exception


가장 대표적인 with 구문 이해  
원하는 시점에 리소스 할당 및 회수  
정확한 이해 후 사용 프로그래밍 개발 중요(문제 발생 요소)

## Ex1 - try, cont
```python
# No use with.

file = open('./testfile1.txt', 'w')
try:
    file.write('Context Manager Test1.\nContextlib Test1.')
finally:
    file.close()
```
- 예전에는 이런 식으로 많이 사용
## Ex2
```python
# Use with.

with open('testfile2.txt', 'w') as f:
    f.write('Context Manager Test2.\nContextlib Test2.')
```
- 이는 Ex1의 finally 구문을 자동으로 실행해줌

## Ex3
```python
# Use Class -> Context Manager with exception handling

class MyFileWriter():
    def __init__(self, file_name, method):
        print('MyFileWriter started : __init__')
        self.file_obj = open(file_name, method)
        
    def __enter__(self):
        print('MyFileWriter started : __enter__')
        return self.file_obj

    def __exit__(self, exc_type, value, trace_back):
        print('MyFileWriter started : __exit__')
        if exc_type:
            print("Logging exception {}".format((exc_type, value, trace_back)))
        self.file_obj.close()
        

with MyFileWriter('testfile3.txt', 'w') as f: # __init__
    f.write('Context Manager Test3.\nContextlib Test3.') # __enter__
#__exit__
```
- 이처럼 Context Manager를 자유롭게 다룰 수 있음
- 단순 with open 구문을 커스텀하여 메모리가 할당 될 때 종료 될 때의 동작을 자유롭게 다룰 수 있음.