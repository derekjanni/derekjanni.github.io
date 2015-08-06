from skimage.transform import resize 
from PIL import Image

for i in range(0, 4):
    img = Image.open('/users/derekjanni/pyocr/site/img/'+ str(i+1) + '.Bmp')
    img = img.resize((200,200))
    img.save(str(i+1)+'.Bmp')
