#--docker apache/openserverless-runtime-go:v1.22proxy-2410121813
#--main main@http://71.105.97.10:42249

def main(args):
    try:
        import torch
        cuda = torch.cuda.is_available()
        return {
            "body": f"Cuda: {cuda}"
        }
    except:
        return {
            "body": "no torch"
        }
