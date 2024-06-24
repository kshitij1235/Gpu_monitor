def update_gpu_temp(self, temperature):
    self.gpu_temp_var.set(f"{temperature} °C")
def update_gpu_load(self, load):
    self.gpu_load_var.set(f"{int(load * 100)}%")
def update_gpu_mem_used(self, used, total):
    self.gpu_mem_used_var.set(f"{used} MB / {total} MB")