#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-

import argparse
import qrcode

def generate_qr(data, output="qrcode.png", size=300):
    """
    создаёт QR-код их данных и сохраняет в файл

    """

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output)
    print(f"QR-код сохранён в {output}")

def main():
    parser = argparse.ArgumentParser(description="генератор QR-кодов")
    parser.add_argument("data", help="текст или ссылка для кодирования")
    parser.add_argument("-o", "--output", default="qrcode.png", help="имя выходного файла")
    parser.add_argument("-s", "--size", type=int, default=300)
    args = parser.parse_args()

    generate_qr(args.data, args.output, args.size)

if __name__ == "__main__":
    main()
