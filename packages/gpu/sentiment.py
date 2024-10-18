#--docker apache/openserverless-runtime-go:v1.22proxy-2410121813
#--main main@http://71.105.97.10:42249

from subprocess import run

def setup(args, status):
    status.write("installing transformers\n")
    run(["pip", "install", "transformers", "--upgrade"])
    status.write("loading transformers\n")
    from transformers import pipeline
    pipeline("sentiment-analysis")

def main(args):
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
