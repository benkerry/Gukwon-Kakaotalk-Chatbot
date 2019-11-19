# Webs
* ~/Webs를 Document Root로 설정할 것을 권장합니다.

## GukwonKakaoChatManager
* 관리자용 기능을 제공하는 웹입니다. 이하의 기능들을 가집니다.
>- 로그인
>- 구성원 인증번호 발급(교사 전용)
>- 관리자 인증번호 발급(교사 전용)
>- 건의 승인/닫기/열기/삭제/답글 달기
>- 개발자에게 메일 보내기
>- 전체 관리자에게 메일 보내기(교사 전용)
>- 관리자 권한 관리(교사 전용)

## SuggestionViewer
* 건의를 열람할 수 있는 웹입니다. 이하의 기능들을 가집니다.
>- 건의 목록 보기
>- 건의 열람하기
>- 답글 


## default.html
> https 연결 상태가 아닌 경우, 프로토콜을 https로 전환합니다. file_get_contents 하여 사용합니다.

## index.html
> Webs로 접속 시 곧 SuggestionViewer로 Redirect합니다.

## config.php
> 이하 변수들을 설정해주시길 바랍니다.
> $mail_id: 네이버 아이디
> $mail_pwd: 네이버 메일 앱 패스워드
> $db_addr: MySQL Addr
> $db_username: MySQL Username
> $db_pwd: MySQL Password
> $db_name: MySQL Database name