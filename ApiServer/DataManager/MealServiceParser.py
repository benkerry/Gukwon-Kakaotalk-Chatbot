# 학교 홈페이지에서 이번 달의 급식을 Parsing하고, 
# 그것을 날짜 + '-' + 조식 || 중식 || 석식(string):급식(list) 형태의 Key-Value를 가진 Dictionary로 변환한다.
# 저장 예시: {"20190926-중":["밥", "물", "김치"], "20190926-석":[물", "밥", "김치"]}
#
# 그리고 그것을 json 형태로 data/ 디렉터리에 저장한다.(확장자는 .dat)
# 이러한 기능을 하는 코드를 run()이라는 이름의 함수로 만들기 바란다.

# 새 Branch를 생성하고, 새 Branch에서 develop/DataManager를 Merge한 후 코딩을 시작하면 된다.
# 예시: git checkout -b feature/DataManager/MealServiceParser --> git merge develop/DataManager