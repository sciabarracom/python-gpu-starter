#--kind go:1.22proxy
#--main main@http://69.159.131.90:35150
#--param hf_token $HUGGINGFACE_HUB_TOKEN
#--web true

from subprocess import run

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
    status.write("installing transformers\n")
    run(["pip", "install", "transformers", "--upgrade"])
    status.write("downloading model\n")
    run(["pip", "install", "huggingface_hub"])
    if login(args):
            status.write("logged in huggingface\n")
            import torch
            torch.cuda.empty_cache()
            from transformers import pipeline
            pipeline(model="microsoft/phi-1_5", device="cuda")
            pipeline.to("cuda")
            status.write("completed\n")
    else:
            status.write("cannot log in huggingface\n")

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
            chat = pipeline(model="microsoft/phi-1_5", device=device)

        output = "please provide some input"
        input = args.get("input")
        if input:
            text = chat(input, max_new_tokens=50)
            print(text)
            if len(text) > 0:
                output = text[0].get('generated_text', output)
    except Exception as e:
        output = f"```\n{str(e)}```"
    
    return {
        "body": {"output": output}
    }
