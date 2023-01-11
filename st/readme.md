# 개요
[Streamlit](https://streamlit.io/)으로 대시보드 만들기
 - 접속주소 : http://rotbeer-st.duckdns.org/
 - Streamlit이란? 
   - 오픈소스 파이썬 라이브러리
   - 데이터 대시보드를 빠르게 제작할 수 있음

## 사용한 기술
 - [Streamlit](https://streamlit.io/)
 - AWS: 배포
 - Nginx: 웹서버
 - docker: Streamlit으로 만든 앱을 도커 이미지로 만듬

 ## 스크린샷
 [![image.png](https://i.postimg.cc/wT0zq7qN/image.png)](https://postimg.cc/pph4kVnV)

 ## 해결한 문제 
 Streamlit은 웹소켓을 사용하는데, Nginx에서 웹소켓을 사용하려면 추가작업을 해야함 
 - 참고자료: https://www.nginx.com/blog/websocket-nginx/ 
 ```
# 서버에 이 부분을 추가해 준다
proxy_http_version 1.1;
proxy_set_header Upgrade $http_upgrade;
proxy_set_header Connection "Upgrade";
proxy_set_header Host $http_host;
```