# FastAPI 활용 프로젝트
## 비동기 게이트웨이 ASGI, Uvicorn
### ASGI
- 애플리케이션 프로그램의 실행 결과를 웹 서버에 전달해주며, 웹 서버는 ASGI로부터 전달받은 응답 결과를 웹 클라이언트에 전송한다.
- WSGI(Web Server Gateway Interface)의 문제점을 보안하기 위해 개발됨
- 비동기적인 것을 제공하기 위해 등장

### Uvicon
- ASGI서버의 구현체
- uvloop와 httptools를 사용하는 ASGI 웹 서버
- ASGI 웹 애플리케이션을 실행하는 서버