import os
import ray
import torch  # Assumes CUDA/torch on GPU node

address = f"{os.environ['RAY_API_SERVER_IP']}:{os.environ['RAY_API_SERVER_PORT']}"
print(f"{address=}")
ray.init(
    address=address
)  # Connect to cluster


@ray.remote(num_gpus=1)
def gpu_task(gpu_id):
    gpus = ray.get_gpu_ids()
    print(f"Task on GPUs: {gpus}, ID: {gpu_id}")
    if torch.cuda.is_available():
        x = torch.rand(1000, 1000).cuda()
        return f"GPU compute OK: {x.sum().item():.2f}"
    return "No GPU"


# Submit 2 tasks (schedules across available GPUs)
futures = [gpu_task.remote(i) for i in range(2)]
print(ray.get(futures))
