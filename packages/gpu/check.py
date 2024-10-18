#--docker apache/openserverless-runtime-go:v1.22proxy-2410150849
#--main main@http://
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
