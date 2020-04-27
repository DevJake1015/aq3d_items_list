from PIL import Image
import os

for filename in os.listdir(f"{os.path.dirname(__file__)}/../assets/items_male"):
    if filename.endswith(".png"):
        im = Image.open(f"{os.path.dirname(__file__)}/../assets/items_male/{filename}")
        rgb_im = im.convert("RGB")
        rgb_im.save(f"{os.path.dirname(__file__)}/../assets/items_male/{filename[:-4]}.jpg")
        os.unlink(f"{os.path.dirname(__file__)}/../assets/items_male/{filename}")
