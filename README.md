# CORS-bypass-server
이미지의 CORS 문제를 우회하기 위한 서버  
python 과 flask 프레임워크로 구성되어있습니다.  
상대서버 외에 자신의 서버자원을 사용하기에 '잘 우회했다' 라고 보기는 좀 그렇습니다.

<br/>

## 1. Install
### Requirements
다음 요구사항을 만족해야합니다.

- python 3
- flask
- requests
- waitress


### Run
flask 서버 실행 (Development 단계).
```shell
python app.py
```

waitress 서버 실행 (Production 단계).
```shell
python waitress-server.py
```

<br/>

## 2. Usage
### cors-bypass (GET http:localhost:5050/cors-bypass/{image-path} )

**주의 할 점은 image-path 의 물음표('?')는 전부 역물음표('¿')로 바꿔야 합니다.**  
이유는 url에 '?'가 있으면 쿼리파라미터로 인식하기 때문에 path variable 로 적용이 불가합니다.  


요청 예시:
```http request
http://localhost:5050/cors-bypass/https://images.unsplash.com/photo-1627662055794-94ab33f5913a
```

응답 예시:
![](https://images.unsplash.com/photo-1627662055794-94ab33f5913a)
