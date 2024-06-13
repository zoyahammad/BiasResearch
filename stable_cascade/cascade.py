import torch
import time
from diffusers import StableCascadeCombinedPipeline

start_time = time.time()

pipe = StableCascadeCombinedPipeline.from_pretrained("stabilityai/stable-cascade", variant="bf16", torch_dtype=torch.float32)
device = torch.device('mps')
pipe = pipe.to(device)

PROMPT = "an astronaut"

for i in range(0, 1):
    pipe(
        prompt=PROMPT,
        negative_prompt="",
        num_inference_steps=10,
        prior_num_inference_steps=20,
        prior_guidance_scale=3.0,
        width=1024,
        height=1024,
    ).images[0].save(f'cascade/doctor/cascade-{i}.png')

print(" Total time --- %s seconds ---" % (time.time() - start_time))

# Reference: https://huggingface.co/stabilityai/stable-cascade
