#--kind go:1.22proxy
#--main main@http://69.159.131.90:35150
#--web true

def main(args):
    
    output = "no torch"
    try:
        import torch
        cuda = torch.cuda.is_available()
        output = f"Cuda: {cuda}"
    except: pass
    
    if args.get("input", "") == "flush":
        torch.cuda.empty_cache()
        output = "flushed"

    return {"body": {"output": output}}
