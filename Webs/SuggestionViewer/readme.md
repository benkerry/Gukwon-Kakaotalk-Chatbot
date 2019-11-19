# SuggestionViewer
* 건의를 열람할 수 있는 웹입니다.

## index.php
>- 건의들의 목록을 볼 수 있습니다.

## SuggestionViewer.php
>- 건의 index를 $_GET['idx']로 넘겨주면 해당 건의를 열람할 수 있도록 해줍니다. 단, 승인 전 건의나 삭제된 건의는 열람할 수 없습니다.

# SuggestionViewer/style
* 각종 css 파일들이 포함된 디렉터리입니다.
  
>## SuggestionViewer/style/master.css
>* SuggestionViewer 내부 모든 프론트엔드 파일에 해당하는 css 코드를 담고 있습니다.

# SuggestionViewer/functions
* 각종 기능 파일들이 포함된 디렉터리입니다.
  
>## SuggestionViewer/functions/dbconn.php
>* MySQL Connection을 체결하는 기능이 담긴 파일입니다. DB 접근이 필요한 파일에서 import하여 사용합니다.