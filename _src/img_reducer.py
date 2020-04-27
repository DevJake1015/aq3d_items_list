from PIL import Image
import os

for filename in os.listdir(f"{os.path.dirname(__file__)}/../assets/items"):
    if filename.endswith(".png"):
        print(f"{os.path.dirname(__file__)}/../assets/items/{filename}")
        im = Image.open(f"{os.path.dirname(__file__)}/../assets/items/{filename}")
        print(im)
        rgb_im = im.convert("RGB")
        rgb_im.save(f"{os.path.dirname(__file__)}/../assets/items/{filename[:-4]}.jpg")
# os.unlink(f"code/backend/source/api/charts/{filename}")
