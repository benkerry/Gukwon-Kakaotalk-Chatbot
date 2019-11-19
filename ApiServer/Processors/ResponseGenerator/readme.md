# ResponseGenerator
* 응답 메시지를 Format에 맞춰 생성합니다.
  
## GenerateOutput.py
### class ListCard : ListCard Output을 생성하는 데 필요한 함수가 들어있는 정적 클래스입니다.
      def generate_listcard_item(str_title:str, str_description:str, str_img_url:str, str_url:str) -> dict
      : ListCard Item 제목, 내용, 배경 이미지 url, 클릭 시 이동할 url을 넘겨주면 ListCard 아이템 하나를 만들어 반환합니다.

      def generate_listcard(str_header_title:str, str_img_url:str, lst_items:str) -> dict
      : ListCard 제목, 배경 이미지 url, ListCard Item 리스트 넘겨주면 그것들을 엮어 ListCard Output을 생성/반환합니다.
  
### class SimpleText : SimpleText Output을 생성하는 함수가 들어있는 정적 클래스입니다.
      def generate_simpletext(str_msg:str) -> dict
      : SimpleText Output을 생성해 반환합니다.

### class SimpleImage : SimpleImage Output을 생성하는 함수가 들어있는 정적 클래스입니다.
      def generate_simpleimage(str_url:str, str_alttext:str) -> dict
      : 이미지의 url, url이 작동되지 않을 시 표시할 alttext를 넘겨주면 SimpleImage Output을 생성/반환합니다.

### OutputsPacker.py
      def pack_outputs(lst_outputs)
      : Output들의 List를 인자로 받아 완전한 형태의 응답 JSON을 만들어 반환합니다.