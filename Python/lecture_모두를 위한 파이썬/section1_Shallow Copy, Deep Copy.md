# Python Advanced(1) - Shallow Copy & Deep Copy
Keyword - shallow & deep cody


객체의 복사 종류 : Copy, Shallow Copy, Deep Copy  
정확한 이해 후 사용 프로그래밍 개발 중요(문제 발생 요소)

## Ex1 - Copy
```python
a_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]] # mutable
b_list = a_list

print('Ex1 > ', id(a_list))
print('Ex1 > ', id(b_list))

b_list[2] = 100

print('Ex1 > ', a_list)
print('Ex1 > ', b_list)

b_list[3][2] = 100

print('Ex1 > ', a_list)
print('Ex1 > ', b_list)

# immutable : int, str 변경 불가
```
- 단순 등호(=)를 통해 copy를 진행하면 두 리스트가 같은 곳을 가르키게 된다.
- 둘 중 하나만 값을 수정해도 동시에 수정사항이 적용됨.

## Ex2 - Shallow Copy
```python
import copy

c_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
d_list = copy.copy(c_list) 

print('Ex2 > ', id(c_list))
print('Ex2 > ', id(d_list))

# print('Ex2 > ', id(c_list[3]))
# print('Ex2 > ', id(d_list[3]))

d_list[1] = 100

print('Ex2 > ', c_list)
print('Ex2 > ', d_list)

d_list[3].append(1000)
d_list[4][1] = 10000

print('Ex2 > ', c_list)
print('Ex2 > ', d_list)
```
- 얕은 복사를 하기 위해서는 import copy를 해주고
- copy.copy(리스트) 행태로 복사를 진행
- 얕은 복사는 가변형 객체 안에 있는 리스트나 참조형에 대한 주소값까지 다 다른 것으로 카피해 주지 않음!
- **중첩 리스트와 같은 형태에는 적합하지 않다!!!**

## Ex3 - Deep Copy
```python
import copy
e_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
f_list = copy.deepcopy(e_list) 

print('Ex3 > ', id(e_list))
print('Ex3 > ', id(f_list))

# print('Ex3 > ', id(e_list[3]))
# print('Ex3 > ', id(f_list[3]))

f_list[3].append(1000)
f_list[4][1] = 10000

print('Ex3 > ', e_list)
print('Ex3 > ', f_list)
```
- 깊은 복사도 동일하게 import copy를 해줘야 함
- copy.deepcopy(리스트) 형태로 복사 진행
- 당연히 얕은 복사보다 많은 메모리와 시간이 걸리지만 얕은 복사의 문제점을 해결할 수 있다.