import torch
import ray  # ray.init() auto by Jobs

@ray.remote(num_gpus=1)
def gpu_task(gpu_id):
    gpus = ray.get_gpu_ids()
    print(f"Job GPU task on {gpus}, ID: {gpu_id}")
    if torch.cuda.is_available():
        x = torch.rand(1000, 1000).cuda()
        return f"GPU sum: {x.sum().item():.2f}"
    else:
        raise Exception(f"No GPUS!")
    return "No GPU"

ray.get([gpu_task.remote(i) for i in range(2)])