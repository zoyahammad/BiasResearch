from diffusers import AutoPipelineForText2Image
import torch
import time

start_time = time.time()

pipe = AutoPipelineForText2Image.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float32, variant="fp16", use_safetensors=True
)

device = torch.device('mps')
pipe = pipe.to(device)

PROMPT = "a Computer Engineer"

name = "computer"

for i in range (0,1):
    image = pipe(prompt=PROMPT).images[0].save(f'{name}/{name}_{i}.png')

print("Total time --- %s seconds ---" % (time.time() - start_time))

