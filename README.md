# Live-in
재빈을 re:bin 으로 풀어서 소리가 비슷한 Live in으로 구성을 해보았다. 희귀난치병으로부터 살아남다라는 뜻도 있지만, 같은 아픔을 지닌 사람들이 이곳에 공존하다라는 의미의 단어의 중의성을 모두 이용해보았다.
 
## TODO-List
### 1. main
  - 수치입력에 따라 허용불가 음식 구분(로그인 안해도 가능하도록 구현)
### 2. find
  - 병원 정보 DB 저장
  - 병원 의사 찾기(병원 이름 or 지역별 카테고리를 통해 검색)
  - 병원 의사 후기 게시판(별점, 간단한 후기작성)
### 3. notice
  - 재빈이해하기, 영양과 운동 관련 정보 게시판 (CRUD)
  - 전문가컬럼 구분하기
### 4. health_diary(투병일기)
  - 투병일기 게시판 (CRUD)
  - 댓글 (CRD)
  - mypage에 있는 수치기록 연동하여 글쓴이의 그 날 건강상태 보여주기
### 5. mypage
  - 회원가입/로그인
  - 캘린더(일정관리)
  - 수치기록 및 확인
  - my diary (기분이모티콘: 😍행복해요/🙃보통이에요/😑별로에요/😭슬퍼요/😡화나요)


## 진행상황
- 장고기본세팅완료!
  - project : Live_in
  - app : main, mypage, health_diary, find
  - createsuperuser

- mypage를 제외한 서브페이지 퍼블리싱 완료
  - 페이지간 라우팅 작업 완료
  
- model 테스트 구현
  - admin에서 잘 동작하는지 확인해봄
  - user, category 등 추후 수정필요
