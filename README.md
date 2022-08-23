# 몽글(Mongle)

## 📆 제작 기간 & 참여 인원
- 22/07/07 ~ 22/08/16
- 고현우, 주정한, 김하진, 최희원 (4인)<br>

## 👍 배포사이트 및 시연영상
- ### www.mongle.site
- ### https://www.youtube.com/watch?v=WB4Q_mE30ck&t=117s<br>


## 🙏 지킨 그라운드 룰
<details>
<summary>코드 컨벤션</summary>
<div markdown="1">
  - feat/ : 새로운 기능 추가/수정/삭제<br>
  - enhan/ : 기존 코드에 기능을 추가하거나 기능을 강화할 때<br>
  - refac/ : 코드 리팩토링,버그 수정<br>
  - test/ : 테스트 코드/기능 추가<br>
  - edit/ : 파일을 수정한 경우(파일위치변경, 파일이름 변경, 삭제)<br>
</div>
</details>
PR을 올릴 시 test코드가 터지지 않는지 유무 체크<br>
PR은 팀원의 검토 후 merge 진행<br>

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

## ⚠️ 원활한 프로젝트 진행을 위한 팀과의 노력
😄 [6.16 팀원 타임어택 진행](https://www.notion.so/6-21-CRUD_further-20987bcdb6cb4a29ae7d79ed16f96030)

💥 [6/21일 CRUD_further](https://www.notion.so/6-21-CRUD_further-20987bcdb6cb4a29ae7d79ed16f96030)

🏹 [6월 20일 타임어택](https://www.notion.so/6-20-19423f82fe4b4acfbf2d1fedf25ddb3f)
<br>
<br>


## 🏁 회고 / 느낀점
> 프로젝트 회고 글 : https://khw7876.tistory.com/163
