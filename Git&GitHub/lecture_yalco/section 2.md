# Section 2

---

## **1. 프로젝트의 변경사항들을 타임캡슐(버전)에 담기**

변경사항 확인

```python
git status
```

- 추적하지 않는(**untracked**) 파일: Git의 관리에 들어간 적 없는 파일

파일 하나 담기

```python
git add tigers.yaml
```

- `git status`로 확인

모든 파일 담기

```python
git add .
```

- `git status`로 확인

## **2. 타임캡슐 묻기**

아래 명령어로 **commit**

```python
git commit
```

- Vi 입력 모드로 진입 - [Vim 강좌](https://www.yalco.kr/10_vim/)

| 작업 | Vi 명령어 | 상세 |
| --- | --- | --- |
| 입력 시작 | i | 명령어 입력 모드에서 텍스트 입력 모드로 전환 |
| 입력 종료 | ESC | 텍스트 입력 모드에서 명령어 입력 모드로 전환 |
| 저장 없이 종료 | :q |  |
| 저장 없이 강제 종료 | :q! | 입력한 것이 있을 때 사용 |
| 저장하고 종료 | :wq | 입력한 것이 있을 때 사용 |
| 위로 스크롤 | k | git log등에서 내역이 길 때 사용 |
| 아래로 스크롤 | j | git log등에서 내역이 길 때 사용 |
- `FIRST COMMIT` 입력한 뒤 저장하고 종료

커밋 메시지까지 함께 작성하기

```python
git commit -m "FIRST COMMIT"
```

아래 명령어와 소스트리로 확인

```python
git log
```

- 종료는 `:q`

---

### **Git에서 과거로 돌아가는 두 방식**

- **reset** : 원하는 시점으로 돌아간 뒤 이후 내역들을 지웁니다.
- **revert** : 되돌리기 원하는 시점의 커밋을 거꾸로 실행합니다.

→ revert를 이용하면 되돌리려는 시점의 커밋 이후로 여러가지의 커밋이 쌓여있을 때 사용하기 좋음!

## 1**. reset 사용해서 과거로 돌아가기**

아래 명령어로 커밋 내역 확인

```python
git log
```

- 되돌아갈 시점의 커밋 해시 복사
- `:q`로 빠져나가기

```python
git reset --hard (돌아갈 커밋 해시)
```

- reset의 옵션(--hard 등)은 섹션 5에서 다룰 것
- • 💡 뒤에 커밋 해시가 없으면 마지막 커밋을 가리킴

## 2**. revert 로 과거의 커밋 되돌리기**

아래 명령어로 **revert**

```python
git revert (되돌릴 커밋 해시)
```

- `:wq`로 커밋 메시지 저장

### **🎯 `Replace Lions with Leopards`의 커밋 되돌려보기**

- 이후 `leopards.yaml` 수정한 내역 때문에 충돌
    - `git rm leopards.yaml`로 Git에서 해당 파일 삭제
    - `git revert --continue`로 마무리
    - `:wq`로 커밋 메시지 저장

### **🎯 reset 사용해서 revert 전으로 되돌아가기**

### **💡 커밋해버리지 않고 revert하기**

```python
git revert --no-commit (되돌릴  커밋 해시)
```

- 원하는 다른 작업을 추가한 다음 함께 커밋
- 취소하려면 `git reset --hard`
- 커밋만 안 한 상태 뭐 더 수정하고 싶은 내용이 있을 때 사용!