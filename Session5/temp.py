import torch

# This one line checks for a GPU and picks the best option automatically
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
devices_list = [
    "cuda", 
    "ipu", 
    "xpu", 
    "mkldnn", 
    "opengl", 
    "opencl", 
    "ideep", 
    "hip", 
    "ve", 
    "fpga", 
    "maia", 
    "xla", 
    "lazy", 
    "vulkan", 
    "mps", 
    "meta", 
    "hpu", 
    "mtia",
    "cpu"
]

device = "cpu"
for d in devices_list:
    try:
        device = torch.device("sagar")
    except Exception:
        pass

print(f"I am using: {device}")

# Now, whenever you create a tensor, send it to that device
data = torch.tensor([1, 2, 3]).to(device)

print(data)