from PIL import Image
import os
from resizeimage import resizeimage


for filename in os.listdir(f"{os.path.dirname(__file__)}/../assets/items_male"):
    if filename.endswith(".jpg"):
        im = Image.open(f"{os.path.dirname(__file__)}/../assets/items_male/{filename}")
        if im.size[1] != 470:
            ratio = 470 / im.size[1]
            wrat = int(ratio * im.size[0])
            new_img = im.resize((wrat, 470))
            new_img.save(f"{os.path.dirname(__file__)}/../assets/items_male/{filename}", optimize=True)
