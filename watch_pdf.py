import os
import time
from pdf2image import convert_from_path

pdf_path = "Резюме.pdf"
png_path = "Резюме.png"

last_mtime = 0

def convert_pdf_to_png():
    images = convert_from_path(pdf_path, dpi=150)
    if images:
        images[0].save(png_path, "PNG")
        print(f"✅ Конвертировано: {png_path}")

while True:
    try:
        mtime = os.path.getmtime(pdf_path)
        if mtime != last_mtime:
            last_mtime = mtime
            print("🔄 Обнаружено изменение PDF...")
            convert_pdf_to_png()
    except FileNotFoundError:
        print("⚠️ PDF не найден.")
    time.sleep(1)
