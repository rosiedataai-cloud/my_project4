# 대시보드 홈페이지
# 1. 모듈 가져오기
from fastapi import FastAPI, Request
# 백엔드 서버 구성시 템플릿엔진 사용 => 서버측에서 동적으로 html을 생성 응답 => SSR
# 파이썬 계열 주로 사용되는 템플릿엔진 jinja2 <= 웹, LLM 프럼프트 구성시 => AI
# html 관여
from fastapi.templating import Jinja2Templates
# 정적 데이터 처리용 => css, js 관여
from fastapi.staticfiles import StaticFiles

# 2. Fastapi 앱 생성, 템플릿엔진, 정적데이터 처리 설정
app = FastAPI()
templates = Jinja2Templates(directory="templates") # 특정 위치를 지정할 수 있다
# 정적 데이터의 위치, url 표기법 설정
app.mount("/static", StaticFiles(directory="static"), name="static")

# 3. 라우팅 구성/정의 -> 메소드 결정 (get방식 적용=>대시보드 홈페이지)
#    "/" => URL 정의 => 여기서는 홈페이지 의미함
@app.get("/") # 홈페이지가 요청되면 누가(함수) 처리할것인가?
def home(req:Request): # 요청객체가 함수 인자로 전달됨 
    # 비즈니스 로직 => 생략
    # 응답 -> 결론은 문자열 (json 형식, html 형식, xml 형식, ...)
    # 클라이언트 요청 (주소 : http://localhost/ ) -> .. -> 서버 도착 -> 
    # URL,메소드 해석 -> 어떤 함수가 처리할지 특정 후 호출 ->
    # 비즈니스 로직 진행(로그인,회원가입,..) 
    # -> 응답 (json, html (템플릿엔진이용 html, 데이터 => 동적 html 구성 => 렌더링), xml, ...)
    # -> 클라이언트 브라우저 도착 -> 브라우저 파서가 파싱, Dom tree등 처리 -> 화면에 그리기 시작
    # -> 클라이언트는 화면을 보게 됨
    return templates.TemplateResponse(req, "index.html")

# 로그인 페이지 라우팅 처리
@app.get("/auth/login")
def login(req:Request):
    return templates.TemplateResponse(req, "login.html")

# 4. 서버가동 => 명령어 대체