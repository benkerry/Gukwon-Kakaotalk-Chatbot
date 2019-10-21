import requests
import json
import os

def run(logger):
    # 변수 초기화!!
    dict_filename = {'this_week':'data/ThisWeekTimeTable.dat', 'next_week':'data/NextWeekTimeTable.dat'}
    dict_json = {'this_week':'', 'next_week':''}
    dict_response = {'this_week':'', 'next_week':''}

    # 서버에 이번 주 시간표 데이터를 요청한다.
    dict_response['this_week'] = requests.get("http://112.186.146.81:4081/98372?MzQ3MzlfMzExNTRfMF8x")
    dict_response['this_week'].encoding = 'utf-8'

    # 서버에 다음 주 시간표 데이터를 요청한다.
    dict_response['next_week'] = requests.get("http://112.186.146.81:4081/98372?MzQ3MzlfMzExNTRfMF8y")
    dict_response['next_week'].encoding = 'utf-8'

    # 이번 주 시간표 데이터, 다음 주 시간표 데이터를 Dictionary로 변환한다.
    dict_json['this_week'] = json.loads(dict_response['this_week'].text.split('\n')[0])
    dict_json['next_week'] = json.loads(dict_response['next_week'].text.split('\n')[0])

    # JSON으로 파일에 저장!
    with open(dict_filename['this_week'], 'w', encoding="UTF-8") as fp:
        json.dump(dict_json['this_week'], fp, ensure_ascii=False, sort_keys=True, indent=4)

    with open(dict_filename['next_week'], 'w', encoding="UTF-8") as fp:
        json.dump(dict_json['next_week'], fp, ensure_ascii=False, sort_keys=True, indent=4)
    
    # 로그 남기기
    logger.log("Data Parsing Completed.")