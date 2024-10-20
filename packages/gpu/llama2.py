#--web true
#--kind go:1.22proxy
#--main main@http://69.159.131.90:35150
#--param hf_token $HUGGINGFACE_HUB_TOKEN

from subprocess import run

MODEL="meta-llama/Llama-2-7b-chat-hf"

def login(args):
    from huggingface_hub import login, whoami
    try:
        whoami()
        return True
    except:
       try:
          login(token=args.get("hf_token", ""))
          return True
       except:
          return False

def setup(args, status):
    from subprocess import run
    status.write("installing libraries\n")
    run(["pip", "install", "transformers", "--upgrade"])
    run(["pip", "install", "huggingface_hub"])
    if login(args):
            status.write("downloading model\n")
            from transformers import pipeline
            pipeline(model=MODEL)
            status.write("completed\n")
    else:
            status.write("cannot login hugging face\n")

chat = None
def main(args):
    global chat
    
    if "setup_status" in args:
        return {"body": {"output": f"```\n{args['setup_status']}```"}}
    
    try:
        from transformers import pipeline
        if not chat:
            import torch
            device = "cuda" if torch.cuda.is_available() else "cpu"
            chat = pipeline(model=MODEL, device=device)

        output = chat(args.get("input", "who are you"), max_new_tokens=50)
    except Exception as e:
        output = f"```\n{str(e)}```"
    
    return {
        "body": {"output": output}
    }
