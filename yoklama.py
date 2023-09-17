pip install deepface
from deepface import DeepFace
from PIL import Image,ImageDraw,ImageFont

dfs = DeepFace.find(img_path = "/res7.jpeg", db_path = "/ekip", detector_backend = "retinaface")
l=len(dfs)
im1 = Image.open("/res7.jpeg")
font = ImageFont.truetype("/hel.ttf",size=25)
for i in range(0,l):
  if len(dfs[i])<2:
    print("tanımlanamayan kişi")
  else:
    x=dfs[i]['source_x'][0]
    y=dfs[i]['source_y'][0]
    w=dfs[i]['source_w'][0]
    h=dfs[i]['source_h'][0]

    img1 = ImageDraw.Draw(im1)
    img1.text((x, y+h), dfs[i]["identity"][0], fill="cyan", font=font)
    img1.rectangle([(x,y),(x+w,y+h)], outline ="green",width=5)
im1.show()