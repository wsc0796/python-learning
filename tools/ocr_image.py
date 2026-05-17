"""
图片文字识别（OCR）
依赖：pip install easyocr
用法：python ocr_image.py <图片路径>

示例：
  python ocr_image.py screenshot.png
  python ocr_image.py C:/Users/50469/Desktop/course.png
"""

import easyocr
import sys
from PIL import Image


def split_and_ocr(img_path: str, n_segments: int = 6):
    """
    将大图切分成多段分别 OCR，提高识别质量

    参数:
        img_path: 图片路径
        n_segments: 切分段数（默认 6，越长越大的图可以设更多）
    """
    img = Image.open(img_path)
    w, h = img.size
    print(f"图片尺寸: {w} x {h}")
    print(f"切分段数: {n_segments}")

    seg_h = h // n_segments
    reader = easyocr.Reader(["ch_sim", "en"], gpu=False)
    all_text = []

    for i in range(n_segments):
        top = i * seg_h
        bottom = (i + 1) * seg_h if i < n_segments - 1 else h
        crop = img.crop((0, top, w, bottom))
        crop_path = f"/tmp/ocr_seg_{i}.png"

        print(f"\n--- 第 {i + 1}/{n_segments} 段 (y={top}-{bottom}px) ---")
        crop.save(crop_path)
        results = reader.readtext(crop_path, detail=1, paragraph=True)
        all_text.extend(results)
        for r in results:
            print(r[1])

    print(f"\n[完成] 共识别 {len(all_text)} 段文字")
    return all_text


def simple_ocr(img_path: str):
    """对小图直接 OCR"""
    reader = easyocr.Reader(["ch_sim", "en"], gpu=False)
    print("正在识别...")
    results = reader.readtext(img_path, detail=1, paragraph=True)
    for r in results:
        print(r[1])
    print(f"\n[完成] 共识别 {len(results)} 段文字")
    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python ocr_image.py <图片路径>")
        print("示例: python ocr_image.py screenshot.png")
        sys.exit(1)

    img_path = sys.argv[1]

    # 检测图片大小，大图自动切分
    try:
        img = Image.open(img_path)
        height = img.height
    except Exception as e:
        print(f"无法打开图片: {e}")
        sys.exit(1)

    if height > 3000:
        split_and_ocr(img_path)
    else:
        simple_ocr(img_path)
