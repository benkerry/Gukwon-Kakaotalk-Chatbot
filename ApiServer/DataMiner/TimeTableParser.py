import requests
import json
import os

def Run():
    file_name = {'this_week':'data/ThisWeekTimeTable.dat', 'next_week':'data/NextWeekTimeTable.dat'}
    json_data = {'this_week':'', 'next_week':''}

    if os.path.isdir('data') == False:
        os.mkdir('data')

    response = {'this_week':'', 'next_week':''}

    response['this_week'] = requests.get("http://112.186.146.81:4081/98372?MzQ3MzlfMzExNTRfMF8x")
    response['this_week'].encoding = 'utf-8'

    response['next_week'] = requests.get("http://112.186.146.81:4081/98372?MzQ3MzlfMzExNTRfMF8y")
    response['next_week'].encoding = 'utf-8'

    json_data['this_week'] = json.loads(response['this_week'].text.split('\n')[0])
    json_data['next_week'] = json.loads(response['next_week'].text.split('\n')[0])

    with open(file_name['this_week'], 'w') as fp:
        json.dump(json_data['this_week'], fp, indent='\t')

    with open(file_name['next_week'], 'w') as fp:
        json.dump(json_data['next_week'], fp, indent='\t')

if __name__ == "__main__":
    Run()