# Python Advanced(1) - Context Manager(2) 
Keyword - Contextlib, __enter__, __exit__

Contextlib - Measure execution(타이머) 제작


## Ex1 - 함수 실행시간을 출력하는 Context manager
```python
# Use Class

import time

class ExcuteTimerCls(object):
    def __init__(self, msg):
        self._msg = msg

    def __enter__(self):
        self._start = time.monotonic()
        return self._start

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print("Logging exception {}".format((exc_type, exc_value, exc_traceback)))
        else:
            print('{}: {} s'.format(self._msg, time.monotonic() - self._start))
        return True # True

with ExcuteTimerCls("Start! job") as v:
    print('Received start monotonic1 : {}'.format(v))
    # Excute job.
    for i in range(10000000):
        pass
    # raise Exception("Raise! Exception.") # 강제로 발생
```

- 이와 같이 Context manager를 커스텀하여 동작의 실행시간을 축정 하는 등의 기능을 만들 수 있다.