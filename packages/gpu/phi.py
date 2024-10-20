#--kind go:1.22proxy
#--main main@https://3fbf254a-4e5b-49cd-bdf7-c3296a95576f-skg00018.k8sgpu.net
#--param hf_token $HUGGINGFACE_HUB_TOKEN

from subprocess import run

def login(args, status):
    from huggingface_hub import login, whoami
    try:
        whoami()
        status.write("already logged in\n")
        return True
    except:
       try:
          login(token=args.get("hf_token", ""))
          status.write("logged in\n")
          return True
       except:
          status.write("cannot log in - did you provide a correct hf_token?\n")
          return False

def setup(args, status):
    from subprocess import run
    run(["pip", "install", "transformers", "--upgrade"])
    status.write("downloading model\n")
    run(["pip", "install", "huggingface_hub"])
    if login(args, status):
            from transformers import pipeline
            pipeline(model="microsoft/phi-1_5", device="cuda")
            pipeline.to("cuda")
            status.write("logged in\n")

chat = None
def main(args):
    global chat
    if "setup_status" in args:
        return {"body": args['setup_status']}
    
    from transformers import pipeline
    if not chat:
        chat = pipeline(model="microsoft/phi-1_5", device=0)
    
    return {
        "body": chat(args.get("input", "who are you"), max_new_tokens=50)
    }
