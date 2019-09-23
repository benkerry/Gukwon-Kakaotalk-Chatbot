import requests
import json
import os

def Run(logger):
    # 변수 초기화!!
    file_name = {'this_week':'data/ThisWeekTimeTable.dat', 'next_week':'data/NextWeekTimeTable.dat'}
    json_data = {'this_week':'', 'next_week':''}
    response = {'this_week':'', 'next_week':''}

    # 읽어온 데이터를 저장할 디렉터리가 없을 때 실행
    if os.path.isdir('data') == False:
        os.mkdir('data')

    
    # 서버에 이번 주 시간표 데이터를 요청한다.
    response['this_week'] = requests.get("http://112.186.146.81:4081/98372?MzQ3MzlfMzExNTRfMF8x")
    response['this_week'].encoding = 'utf-8'

    # 서버에 다음 주 시간표 데이터를 요청한다.
    response['next_week'] = requests.get("http://112.186.146.81:4081/98372?MzQ3MzlfMzExNTRfMF8y")
    response['next_week'].encoding = 'utf-8'

    # 이번 주 시간표 데이터, 다음 주 시간표 데이터를 Dictionary로 변환한다.
    json_data['this_week'] = json.loads(response['this_week'].text.split('\n')[0])
    json_data['next_week'] = json.loads(response['next_week'].text.split('\n')[0])

    # JSON으로 파일에 저장!
    with open(file_name['this_week'], 'w') as fp:
        json.dump(json_data['this_week'], fp, indent='\t')

    with open(file_name['next_week'], 'w') as fp:
        json.dump(json_data['next_week'], fp, indent='\t')
    
    # 로그 남기기
    logger.Log("Data Parsing Completed.")

if __name__ == "__main__":
    Run()