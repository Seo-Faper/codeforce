import requests
import time
def add_hyphens_to_uuid(uuid_string):
    # 문자열을 8-4-4-4-12 형식으로 변환
    return '-'.join([uuid_string[:8], uuid_string[8:12], uuid_string[12:16], uuid_string[16:20], uuid_string[20:]])

cookies = {
    'token_v2' : 'v02:user_token_or_cookies:GJYs8ezK1C1oRudw_y7Stjch0HQXnXIEbceLoLUCEp7fjx6qm7hwjQBtlgNh1eXcbdDqVGfYgP44SFay2dD1hXx1QNdnabNHgys-qXyOj0NYVRUC3FMEgS2twZmpRDXmeJUs'
}
page_id = '15f1a35fe20644c997628000d4f0b199'
payload = {
            "page": {
                "id": add_hyphens_to_uuid(page_id)
            },
            "limit": 30,
            "cursor": {
                "stack": []
            },
            "chunkNumber": 0,
            "verticalColumns": False
        }

res = requests.post('https://www.notion.so/api/v3/loadCachedPageChunk', json=payload, cookies=cookies)
print(res.json())
print("="*100)


payload = {"block":{"id":"ae377410-1042-4c2f-b195-253e7e6043a7","spaceId":"4c8b4293-1089-492d-b37f-e67de53de9fe"},"timestamp":int(time.time())}
res = requests.post('https://www.notion.so/api/v3/recordPageExit',json=payload, cookies=cookies) # EXIT
print("="*30+"EXIT"+"="*30)
print(res.json())
time.sleep(3)
print("="*100)


print("="*30+"VISIT"+"="*30)
payload = {"block":{"id":"eeb78ce4-a921-46b4-96a8-ed176341181c","spaceId":"cd485a0c-9bcc-4cc8-9808-b661dd831ab4"},"timestamp":int(time.time())}
res = requests.post('https://www.notion.so/api/v3/recordPageVisit',json=payload, cookies=cookies) # Visit 
print(res.json())

page_id = 'd9e5bc0df8564a49a1515d0598aa59ba'
payload = {
            "page": {
                "id": add_hyphens_to_uuid(page_id)
            },
            "limit": 30,
            "cursor": {
                "stack": []
            },
            "chunkNumber": 0,
            "verticalColumns": False
        }
res = requests.post('https://www.notion.so/api/v3/loadCachedPageChunk', json=payload, cookies=cookies)
print("="*100)
print(res.json())
print("="*100)