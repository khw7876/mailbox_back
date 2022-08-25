# 몽글(Mongle)

## 📝 기획의도 
![20220822132858](https://user-images.githubusercontent.com/102797869/185839746-4c879cb4-b66d-4272-aca5-30035f1ba660.png)
<br>
<br>
## 👍 배포사이트 및 
- ### www.mongle.site
- ### https://www.youtube.com/watch?v=WB4Q_mE30ck&t=117s<br>
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

## 🤝 제작 기간 & 팀원 별 역할
- 22/07/07 ~ 22/08/16 
### 🧔🏻‍♀️ 주정한 : 팀장  
- 백엔드 배포(https)  
- 프로필 페이지  
- 편지함 페이지  
- CI / CD  
- 검색기능(Elastic Search)  
- 신고기능(APScheduler)  

### 🍞 고현우  
- 익명게시판 페이지  
- 고민게시판 페이지  
- 편지받기 페이지  
- 편지쓰기 페이지  
- 비밀번호 찾기 기능  

### 👩‍🌾 김하진  
- 프론트 배포(https)  
- 메인페이지  
- 편지 보내는 페이지  
- 반응형 페이지  
- 몽글 튜토리얼 페이지  
- 텍스트 에디터(커스텀)  
- Redis  

### 🦥 최희원  
- 로그인 페이지  
- 회원가입 페이지  
- 욕설감지 기능  
- 게시글 추천 기능(APScheduler)  
- 알림기능(Web Push)  

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

## `❓ 사용자 피드백을 받기 전`

<details>
<summary>1️⃣  익명게시판, 고민게시판</summary>
<div markdown="1">
  - &nbsp;&nbsp;&nbsp;1. Django의 RestFramework를 이용하여 게시글에 대한 CRUD 구현<br>
  - &nbsp;&nbsp;&nbsp;2. 발생 가능한 Error를 TDD 방식을 활용하여 에러 핸들링 구현 (100여개)<br>
  - &nbsp;&nbsp;&nbsp;3. Custom Pagination을 통한 로직 구현<br>
  - &nbsp;&nbsp;&nbsp;4. 쿼리수 줄이기, 필요한 데이터만 Return 하는 등 로직에 대한 이해<br>
  - &nbsp;&nbsp;&nbsp;5. 백엔드적 관리에 집중<br>
</div>
</details>

<details>
<summary>2️⃣  TDD 방식을 활용한 이유</summary>
<div markdown="1">
  - &nbsp;&nbsp;&nbsp;발생 가능한 Error를 직접 핸들링 하기 위해서 사용<br>
  - &nbsp;&nbsp;&nbsp;ex) 권한이 주어지지 않은 user가 서버에 데이터를 요청하였을 경우에 관한 핸들링<br>
</div>
</details>

<details>
<summary>3️⃣  TDD 방식을 통해 얻은 이점</summary>
<div markdown="1">
  - &nbsp;&nbsp;&nbsp;새로운 Error에 대한 쉬운 핸들링
  - &nbsp;&nbsp;&nbsp;발생가능한 Error의 핸들링을 통한 서비스의 안정감 확보
</div>
</details>



## `🚧 사용자 피드백 (총66개의 피드백 중 나의 개선내용 중)`

1️⃣ 비밀번호를 잃어버린 경우에 대한 대책 x

2️⃣ 모바일 환경에서의 불편함

3️⃣ 예기치 못한 새로운 Error의 발생
<br>
<br>

## `✅ 사용자 피드백을 받은 후`

1️⃣ 새로운 View를 작성하여 비밀번호를 재생성하는 기능 구현

2️⃣ 모바일 환경에 대한 반응형 추가 설계

3️⃣ 새롭게 발생한 오류에 대한 Test코드 추가 반영 및 수정
<br>
<br>

## 🏋🏼‍♀️ 원활한 프로젝트 진행을 위한 팀과의 노력
😄 [6.16 팀원 타임어택 진행](https://www.notion.so/6-21-CRUD_further-20987bcdb6cb4a29ae7d79ed16f96030)

💥 [6/21일 CRUD_further](https://www.notion.so/6-21-CRUD_further-20987bcdb6cb4a29ae7d79ed16f96030)

🏹 [6월 20일 타임어택](https://www.notion.so/6-20-19423f82fe4b4acfbf2d1fedf25ddb3f)
<br>
<br>
## ⚠️ 마주한 문제점 및 해결방안
> #### ✔️ 한 로직에서 거치는 쿼리수가 많아져서 로딩이 길어지는 문제점이 발생<br>
>  - CaptureQueriesContext 를 통하여 로직의 쿼리수를 파악한 후
>  - selected_related, prefetch_related를 통하여 쿼리수를 절반가량 줄였습니다.<br>
> 
> #### ✔️ migrations 파일들이 생성한 시간대별로 저장이 되기에 팀원들끼리의 잦은 충돌 발생<br>
>  - 팀원들과 합의하여 Settings.py나 migrations등 모두가 공유하는 파일을 수정하였을 경우 즉각적인 Push와 pull 진행을 하였습니다.<br>
> 
> #### ✔️ pagination된 페이지에 해당 페이지에서 꼭 필요한 데이터만을 보내는 것이 아닌 모든 데이터를 전송하는 상황 발생<br>
>  - Javascript에서 pagination을 커스텀하여 작성하였습니다. 프론트에서 Query Params를 통해 정보를 전달하였고, <br> 백엔드에서는 페이지에 꼭 필요한 데이터만을 전송하도록 하였습니다.> <br>
>
> #### ✔️ 변수명만으로 어떠한 데이터가 들어있는지 특정하기 어려웠던 문제점 발생<br>
> - 작업자 이외에도 타인들이 보았을 때 어떠한 데이터가 들어있는 변수인지 이해할 수 있도록 변수명 선언이 되도록 하였습니다.<br>
> <hr>
> 
> #### ✔️ 문제점을 해결하면서 느낀점<br>
> -  문제를 직면하였을 때 어떠한 방법으로 해결할 수 있을지에 대한 사고능력을 키울 수 있었습니다.<br>
> -  나 혼자만의 코드가 아닌, 팀원들과 공유하는 코드라는 마인드를 가지게 되었습니다.<br>
> -  무작정 코드를 입력하기에 앞서 짜고자 하는 로직에 대해 구상하는 능력을 키울 수 있었습니다.<br>


## 🏁 회고 / 느낀점
> 프로젝트 회고 글 : https://khw7876.tistory.com/163
