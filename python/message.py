import json
from datetime import datetime

with open('./python/data.json', 'r') as file:
    data = json.load(file)

messages = data['chat_messages']

for message in messages:

    created_at = message['created_at']
    
    if created_at[-3] == ':' and created_at[-2:] == '00':
        created_at = created_at[:-3] + ':00'

    timestamp = datetime.fromisoformat(created_at).strftime('%Y-%m-%d %H:%M:%S')
    
    print(f"[{timestamp}]")
    sender = "User" if message['sender'] == "human" else "Assistant"
    print(f"{sender}: {message['text']}\n")
