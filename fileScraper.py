import requests
import json
import sys

ct = ""
bucket = "kabob"

def process_page(bucket="", ct=""):
    my_items = []
    url = "https://www.googleapis.com/storage/v1/b/" + bucket + "/o?pageToken=" + ct
    r = requests.get(url)
    rj = r.json()
    if("error" in r.json().keys()):
        return []
    
    if ("items" in r.json().keys()):
        for i in rj['items']:
            # print ("[Worker]: Process Item!")
            try:
                obj = dict()
                obj['bucket'] = bucket
                obj['mediaLink'] = i['mediaLink']
                obj['contentType'] = i['contentType']
                my_items.append(obj)
            except KeyError as e:
                pass # handle the error
    if ('nextPageToken' in r.json().keys()):
        my_items += process_page(bucket, rj['nextPageToken'])
    
    #there isnt another page we can return what we have
    return my_items

bucket_contents = process_page(sys.argv[1], ct)
j_out = {"items": json.dumps(bucket_contents)}
jj = json.loads(json.dumps(j_out))
print(str(bucket_contents)[1:-1])
