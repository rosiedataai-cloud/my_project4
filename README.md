# my_project
CI/CD를 위한 프로젝트. 간단한 대시보드 구성

# 사용 소프트웨어
- app
    - 백엔드 : fastapi, uvicorn
    - 프런트 : 부트스트랩기반 adminlte 제품 4.0.0  버전 사용
- db
    - mysql
- proxy
    - nginx
- 가상환경 구성
    - docker
        - Dockerfile, Docker-compose

# 구조
```
# 맥 brew 
tree /F /A >> struct.txt
```
/
|   .gitignore
|   docker-compose.yml
|   README.md
|   struct.txt
|   
+---.github
|   \---workflows
|           deploy.yml
|           
+---app
|   |   main.py
|   |   requirements.txt
|   |   
|   +---static
|   |   +---assets
|   |   |   \---img
|   |   |       \---credit
|   |   |               
|   |   +---css
|   |   |       
|   |   \---js
|   |           
|   \---templates
|           Dockerfile
|           index.html
|           login.html
|           
\---nginx
        Dockerfile
        web.conf
        
# 개발 환경(로컬 PC) 구동
```
docker-compose up -d --build
```
# 컨테이너 구성
docker-compose up -d --build

# 다시 구성
docker-compose down

# 접속 테스트, 브라우저
http://localhost
```