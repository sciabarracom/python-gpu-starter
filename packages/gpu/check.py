# --kind go:1.22proxy
# --main main@http://69.159.131.90:35150

def main(args):
    
    output = "no torch"
    try:
        import torch
        cuda = torch.cuda.is_available()
        output = f"Cuda: {cuda}"
    except: pass

    return {"body": {"output": output}}
