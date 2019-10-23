# ResponseGenerator
* 응답 메시지를 Format에 맞춰 생성합니다.
  
## GenerateOutput.py
### class ListCard: ListCard 관련 JSON을 생성하는 함수들의 집합입니다.
      def generate_listcard_item(self, str_title, str_description, str_img_url, str_url)
      : ListCard 아이템 하나를 만들어 반환합니다(딕셔너리 형태).

      def generate_listcard(self, str_header_title, str_img_url, lst_items)
      : ListCard Item 리스트를 이용해 ListCard Output을 생성해 반환합니다(딕셔너리 형태).
  
### class SimpleText: SimpleText 관련 JSON을 생성하는 함수가 들어 있습니다.
      def generate_simpletext(self, str_msg)
      : SimpleText Output을 생성해 반환합니다(딕셔너리 형태).
  

## OutputsPacker.py
      def pack_outputs(lst_outputs)
      : Output들의 List를 인자로 받아 완전한 형태의 응답 JSON 만들어 반환합니다(딕셔너리 형태).