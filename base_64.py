from io import BytesIO
from PIL import Image
import base64
import sys


def to_base64(pil_image):
    buff = BytesIO()
    pil_image.save(buff, format='JPEG', quality=85)
    return base64.b64encode(buff.getvalue()).decode('utf-8')


def encode(image_path):
    base64_txt = image_path + ".txt"
    filename = image_path

    b64 = to_base64(Image.open(filename))
    file = open(base64_txt, 'w')
    file.write(b64)
    file.close()


def main(image_path):
    encode(image_path)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("ERROR: No argument")
    else:
        image_path = sys.argv[1]
        main(image_path)
