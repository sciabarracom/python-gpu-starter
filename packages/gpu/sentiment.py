#--web true
#--kind go:1.22proxy
#--main main@http://69.159.131.90:35150

from subprocess import run

def setup(args, status):
    status.write("installing transformers\n")
    run(["pip", "install", "transformers", "--upgrade"])
    status.write("loading transformers\n")
    from transformers import pipeline
    pipeline("sentiment-analysis")

def main(args):
    import os
    print(dict(os.environ))
    global sentiment
    
    if "setup_status" in args:
        return {"body": {"output": f"```\n{args['setup_status']}```"}}

    try:
        import torch
        device = "cuda" if torch.cuda.is_available() else "cpu"
        from transformers import pipeline
        sentiment = pipeline('sentiment-analysis', device=device)

        input = args.get("input", "")
        output = "please provide some input"
        if input != "":
            res = sentiment(input)
            output = res[0]['label']+": "+str(res[0]['score'])
    except:
        output = "something went wrong"
        
    return {"body": {"output": output}}
