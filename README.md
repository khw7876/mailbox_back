# 몽글(Mongle)

## 📆 제작 기간 & 참여 인원
- 22/07/07 ~ 22/08/16
- 고현우, 주정한, 김하진, 최희원 (4인)<br>

## 👍 배포사이트
- ### www.mongle.site
<br>

## 📝 기획의도 
![20220822132858](https://user-images.githubusercontent.com/102797869/185839746-4c879cb4-b66d-4272-aca5-30035f1ba660.png)
<br>
<br>

## 🔨 페이지 별 기능

![20220818152045](https://user-images.githubusercontent.com/102797869/185308909-658e2d00-4722-4e0f-80ab-bb812a15c9b1.png)
<br>
<br>

## 🏛 개발 아키텍처

![Web App Reference Architecture (2)](https://user-images.githubusercontent.com/55477835/185822526-93e791e1-bf37-4d5f-a225-1de87cc83fab.png)
<br>
<br>

## 🛠 사용기술
- ### cloudfront와 route53, s3를 활용한 https 프론트 배포
- ### elb와 route53, ec2를 활용한 https 백엔드 배포
- ### pre-commit hook(black, isort, flake8)을 통한 코드 포맷팅
- ### 273개의 test코드를 통한 에러 핸들링
- ### 별개의 fast-API 서버를 운용하여 추천기능 구현
- ### APScheduler를 통해 4시간마다(fast-API서버에서) 추천 데이터가 담긴 csv파일 수신
- ### redis 캐싱을 통한 서버 응답속도 향상
- ### logstash를 활용하여 mysql 데이터 30분 마다 elastic-search로 업데이트
- ### elastic-search를 활용하여 유사 검색어 기능 구현
- ### 딥러닝을 활용한 비속어 필터링 기술 페이지의 의도와 맞지않는 편지내용이 들어갈 수도 있으므로 비속어나 비방언어를 사용하면 편지를 쓰지 못하게 막는다. [기술 링크](https://github.com/smilegate-ai/korean_unsmile_dataset)
- ### github actions과 도커를 통한 ci/cd 기능 구현
<br>
<br>

## 📚 ERD
![mongle_erd](https://user-images.githubusercontent.com/55477835/182724054-fd7394ac-121c-498a-8396-19e009e61685.png)
<br>
<br>

## 🏹 api명세서
- Postman mock server를 활용한 api명세서
- https://documenter.getpostman.com/view/9279033/Uzs9wMsa
<br>
<br>

## 🤙 컨벤션
- feat/ : 새로운 기능 추가/수정/삭제
- enhan/ : 기존 코드에 기능을 추가하거나 기능을 강화할 때
- refac/ : 코드 리팩토링,버그 수정
- test/ : 테스트 코드/기능 추가
- edit/ : 파일을 수정한 경우(파일위치변경, 파일이름 변경, 삭제)
<br>
<br>

## 🙏 그라운드 룰
1. 작업 단위로 팀원들에게 공유하기(매일 오후5시) and 하루 일정 공유하기(매일 오전 9시)
2. 저녁7시에 TIL 작성후 팀원들과 피드백
3. API 작업시 변동사항 API 설계 업데이트 하기.
4. PULL REQUESTS 작업시 다같이 라이브로 수정한다 or 주맨이 대표로 리뷰하고 merge 한다.
5. 자기가 맡은 역할 기간 안에 최선을 다해서 끝내기. ( 당연할 수록 어려움 )
6. 어렵거나 막히는 부분 있으면 팀원들이나 튜터님한테 적극적으로 소통하고 팀원들과 같이 해결하기.
11. 공통 파일 수정 후 main 브랜치에 머지한다면 모두가 풀한 후 작업을 다시 시작한다.
7. 하진이형이 형 동생들 멘탈 잘 잡아주기
8. 쉬는 시간 챙기면서 일하기.
9. 밤샘 금지
10. 아프면 바로 말해서 휴식 취하기!

## 🏁 회고 / 느낀점
> 프로젝트 회고 글 : https://khw7876.tistory.com/163
