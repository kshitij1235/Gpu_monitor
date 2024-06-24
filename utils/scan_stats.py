from GPUtil import getGPUs

class scan:
    def __init__(self) -> None:
        self.gpus = getGPUs()
    def get_detail(self):
        return self.gpus[0] 

    def get_gpu_name(self):
        gpu = self.gpus[0] 
        return gpu.name


