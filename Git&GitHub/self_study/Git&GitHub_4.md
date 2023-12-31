## 브랜치(branch)

공식문서 정의에 의하면 

A branch in Git is simply a lightweight movable pointer to one of thes commits

\- 간단한 어떤 '특정한 목표'를 가지고 코드를 수정하기 시작할 때 만든다.

### 브랜치명 수정 명령어

```
git branch -M 브랜치명
```

\=> 보통 차별 이슈로 master브랜치를 main으로 바꾸고 사용함

### 뭔가 할 일을 할 때

1.  이슈를 생성
2.  이슈에 맞는 브랜치 생성
3.  생성한 브랜치로 전환하여 작업

### 브랜치 생성 명령어

```
git branch 브랜치명
```

### 브랜치 전환 명령어

```
git checkout 브랜치명
git switch 브랜치명
```

switch 명령어는 낮은 버전에서는 사용이 불가능하다.

### 브랜치 생성/전환을 동시에

```
git checkout -b 브랜치명
```

#### 브랜치가 전환된 상태에서 그 이슈에 맞는 작업을 진행한다.

이후 커밋을 만들 때에는 커밋 메시지에 해결하고 있는 이슈번호를 붙여주는 것이 좋다!

\=> 이러면 #이슈번호를 클릭시 이슈트래커로 한번에 이동이 가능함!

## merge(마지)

브랜치에서 작업한 내용을 다른 브랜치와 합치기 위해 사용

### 명령어

```
git merge 브랜치명
```

A브랜치를 B브랜치에 합칠 시 주의

1.  B 브랜치를 체크아웃한다.
2.  git merge A 명령어 실행

### GitHub 내에서 merge

GitHubdptj Pull requests를 통해 merge요청을 할 수 있다.

RP메시지 템플릿도 팀 혹은 프로젝트마다 만들어 사용하면 용이하다.

PR이 제출된 후에 코드리뷰가 진행되고 문제가 없을 시 merge

merge를 하는 주체는 조직마다 다르다!

### 자동머지메커니즘

두 부랜치가 만들어져 수정을 할 때

서로 다른 내용을 작업하면 거의 충돌이 나지 않는데 이는 자동머지메커니즘이 도와주기때문!

하지만 같은 내용을 작업하면 충돌이 발생한다!

## merge 중 충돌이 났을 경우

### vim으로 본 충돌 메시지

```
<<<<<<<< HEAD
...		<- 현재 체크아웃한 브랜치의 소스코드
|||||||||| merged common ancestors
....		<- 두 브랜치의 공통 조상의 소스코드
===========
....		<- 병합하려는 브랜치의 소스코드
>>>>>>병합하려는 브랜치이름
```

이렇게 소스코드가 수정되는데 여기서 본인이 원하는 코드만 남기고 지워주면 된다.

하지만 vim을 이요한 방법은 어려움이 있는 경우가 많아 보통 gui를 이용해 충돌을 해결한다.

vs코드에서 충돌이 일어나면 gui를 통해 클릭으로 편하게 충돌을 해결 할 수 있는 모습이 보인다.

## rebase

주둔지를 옮기다

브랜치를 합치는 방법에는 일반머지뿐만이 아니라 rebase도 존재한다.

### 명령어

```
git rebase 브랜치명
```

### rebase는 일반merge와 비슷하지만 차이점이 있다.

rebase를 사용하면 merge commit이 생성되지 않는다. 

이는 git graph를 굉장히 단순하게 만들기 때문에 나중에 버전관리에 있어 더욱 용이해진다.

대표적으로 우아한 형제들이 rebase의 개념을 사용한다고 볼 수 있다.

참고: [https://techblog.woowahan.com/2553/](https://techblog.woowahan.com/2553/)

 [우린 Git-flow를 사용하고 있어요 | 우아한형제들 기술블로그

{{item.name}} 안녕하세요. 우아한형제들 배민프론트개발팀에서 안드로이드 앱 개발을 하고 있는 나동호입니다. 오늘은 저희 안드로이드 파트에서 사용하고 있는 Git 브랜치 전략을 소개하려고 합

techblog.woowahan.com](https://techblog.woowahan.com/2553/)

## reset

reset은 commit을 삭제하는 기능을 가진다

### 명령어

```
git reset HEAD~1
```

이는 HEAD를 기준으로 하나의 commit만 삭제한다는 의미를 가짐

## revert

이미 push가 되어 팀원간에 공유되고 있는 커밋을 되돌릴 때는 git reset을 사용하면 안된다.

대신 revert를 사용하면 되돌리려고 하는 커밋 안에 있는 작업을 삭제해주는 새로운 커밋이 만들어준다.

### 명렁어

```
git revert 커밋아이디
```