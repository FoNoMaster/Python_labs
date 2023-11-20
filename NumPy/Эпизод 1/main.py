import numpy as np
from PIL import Image

img = Image.open("lunar03_raw.jpg")
data = np.array(img, dtype=np.float64)

data1 = ((data - data.min()) / (data.max() - data.min()) * 255).astype(np.uint8)

res_img = Image.fromarray(data1)
res_img.save("lunar3.jpg")
