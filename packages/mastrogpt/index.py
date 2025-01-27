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
            {
                "name": "GPU",
                "url": "gpu/check"
            },
            {
                "name": "Sentiment",
                "url": "gpu/sentiment"
            },
            {
                "name": "Phi",
                "url": "gpu/phi"
            },
        ]
    }
    return {"body": data}
