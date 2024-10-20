#--kind go:1.22proxy
#--main main@https://3fbf254a-4e5b-49cd-bdf7-c3296a95576f-skg00018.k8sgpu.net

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
        res = "\n".join(args['setup_status'])
        return { "body": res }
    
    try:
        from transformers import pipeline
        sentiment = pipeline('sentiment-analysis')

        input = args.get("input", "")
        if input == "":
            return { "body": "please provide some input"}
        output = sentiment(input)
        return {
            "body": output
        }
    except:
        return {"body": "exception"}
