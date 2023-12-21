# Section 1

---

## Git을 배워야 하는 이유

게임, 웹, 앱 등 뭘 만들든 개발자가 되려면 Git을 다룰 줄 아는 것은 필수 소양이다.

→ 사무직이 워드나 한글을 다룰 줄 아는 것과 같은 느낌

### Git이 뭔데?

**VCS(Version Control System)** 종류의 프로그램 중 하나이다.

쉽게 말해 프로그램의 시간과 차원을 관리한다. 예를 들어서

**시간의 경우**

- 버전 5에 추가한 기능에 결함이 있어서 버전 4로 되돌아가야 하는 경우
- 버전 3, 4, 5에는 이상이 없는데 버전 2에서 했던 작업에 뒤늦게 문제가 발견돼서 딱 그것만 취소해야 하는 경우

**차원의 경우**

- 회사 앱에 자신의 아이디어를 시도해보고 싶은 경우
- 각 폴더들에서 각각 작업을 해나가다가 모든 안들을 실제품에 적용하기로 결정이 되어 모두 맨 프로젝트로 가져와야 하는 경우

이러한 경우들은 Git으로 정말 쉽게 해결이 된다. 

Git을 사용하면 내가 만들고 있는 거가 들어있는 폴더에 시간과 자원을 종횡으로 넘나들 수 있다. 이는 협업에 있어 매우 중요한 기능을 제공한다.

---

## CLI VS GUI. 무엇을 사용해야 할까?

**CLI(Command Line Interface)** - 터미널에 명령어를 이용하는 CLI 방식

**GUI(Graphical User Interface)** - 소스트리 등의 프로그램을 사용하는 GUI 방식

**얄코왈**

본인은 Git에서 뭔가를 실행하기 위한 어떤 명령들을 사용할 때는 CLI를 사용하고 프로젝트의 상태를 Git 창에서 자세히 살펴봐야 할 때는 Source Tree를 사용한다.

GUI가 당장 쓰기에는 편할지 모르겠지만 배우는 단계에서는 CLI를 통해 세세한 기능들을 모두 배우고 가는 것을 권장한다. 그래야 Git에 대해 보다 정확히 이해하고 제대로 사용할 수 있다!

---

## **1. Git 최초 설정**

### **Git 전역으로 사용자 이름과 이메일 주소를 설정**

- GitHub 계정과는 별개

터미널 프로그램 (Git Bash, iTerm2)에서 아래 명령어 실행

`git config --global user.name "(본인 이름)"`

`git config --global user.email "(본인 이메일)"`

아래의 명령어들로 확인

`git config --global user.name`

`git config --global user.email`

### **기본 브랜치명 변경**

`git config --global init.defaultBranch main`

## **2. 프로젝트 생성 & Git 관리 시작**

적당한 위치에 원하는 이름으로 폴더를 생성하고 **VS Code**로 열람

해당 폴더에서(VS Code 터미널 기본) 아래 명령어 입력

`git init`

폴더에 숨김모드로 **.git** 폴더 생성 확인

- 🛑 이 폴더를 지우면 Git 관리내역이 삭제됩니다. (현 파일들은 유지)
- 맥에서 숨김 파일 보기: `command` + `shift` + `.`

아래의 파일들 생성

*tigers.yaml*

```
team: Tigers
manager: John
members:
- Linda
- William
- David
```

*lions.yaml*

```
team: Lions
manager: Mary
members:
- Thomas
- Karen
- Margaret
```

### **❗️ 모든 작업(파일 생성, 수정)마다 파일을 꼭 저장하세요!**

터미널에 아래 명령어 입력

`git status`

## **3. 소스트리로 해보기**

### **현존하는 저장소 추가**

- 소스트리에 폴더를 드래그하거나, `로컬 저장소 추가`

### **Git이 관리하는 저장소 새로 만들기**

- .git 폴더 삭제 후 진행
- 소스트리에 폴더를 드래그하거나, `로컬 저장소 생성`

## **Git의 관리에서 특정 파일/폴더를 배제해야 할 경우**

### **a. 포함할 필요가 없을 때**

- 자동으로 생성 또는 다운로드되는 파일들 (빌드 결과물, 라이브러리)

### **b. 포함하지 말아야 할 때**

- 보안상 민감한 정보를 담은 파일

****.gitignore 파일을 사용해서 배제할 요소들을 지정할 수 있습니다.****

## **.gitignore 형식**

https://git-scm.com/docs/gitignore 참조

```
# 이렇게 #를 사용해서 주석

# 모든 file.c
file.c

# 최상위 폴더의 file.c
/file.c

# 모든 .c 확장자 파일
*.c

# .c 확장자지만 무시하지 않을 파일
!not_ignore_this.c

# logs란 이름의 파일 또는 폴더와 그 내용들
logs

# logs란 이름의 폴더와 그 내용들
logs/

# logs 폴더 바로 안의 debug.log와 .c 파일들
logs/debug.loglogs/*.c

# logs 폴더 바로 안, 또는 그 안의 다른 폴더(들) 안의 debug.log
logs/**/debug.log
```