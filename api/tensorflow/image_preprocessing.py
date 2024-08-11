import base64
import io
import numpy as np
from PIL import Image


def base64_to_numpy(base64string: str):
    # デコード
    decoded = base64.b64decode(base64string)
    # 画像化
    img = Image.open(io.BytesIO(decoded))
    # numpy配列
    numpy_img = np.array(img)
    # 濃淡のみの二次元配列
    img_gray = numpy_img[:, :, 3]
    # 正規化
    img_gray_norm = img_gray / 255.0
    # バッチサイズを追加した三次元配列
    img_gray_batch = np.expand_dims(img_gray_norm, 0)

    return img_gray_batch
