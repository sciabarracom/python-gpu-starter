#--web true
import json

def main(arg):
    data = {
        "services": [
            { 
                "name": "Demo", 
                "url": "mastrogpt/demo",
            },
            {
                "name": "AI",
                "url": "openai/chat"
            },
        ]
    }
    return {"body": data}
