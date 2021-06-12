import os
import random
import qrcode

qr_dir = "qr_out"
file_out = "out.txt"
qr_fill_color = "#000000"
qr_back_color = "#ffc2d9"

def save_qr(data, number):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=40,
        border=4,
    )
    qr.add_data(f'{data}')
    qr.make(fit=True)
    img = qr.make_image(fill_color=qr_fill_color, back_color=qr_back_color)
    img.save(f"{qr_dir}/{number}.jpg")

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def generator(length):
    password = ''
    for n in range(length):
        password += random.choice(chars)
    return password

print(f"\n   1 - Сгенерировать пароли в {file_out}")
print(f"   2 - QRCode конвертация из {file_out} в папку {qr_dir}")
quest = int(input("\n\n Выберите действие: "))

def many_generator(number_of_passwords, length_of_passwords):
    passwords = []
    for n in range(number_of_passwords):
        passwords.append(generator(length_of_passwords))
    return passwords

if quest == 1:
    number_of_passwords = int(input("\n   Введите количество паролей: "))
    length_of_passwords = int(input("   Введите длину паролей: "))
    with open(f"{file_out}", 'w') as f:
        counter = 0
        for n in many_generator(number_of_passwords, length_of_passwords):
            counter += 1
            f.write(f"{counter}) {n}" + "\n") #Запись в файл и переход на новую строку
    print(f"Готово! Пароли сгенерированы в файл {file_out}")
    
elif quest == 2:
    os.system(f"mkdir {qr_dir}")
    number = 0
    with open(f"{file_out}", "r") as f:
        text = f.readlines()
    counter = 0
    for n in text:
        counter += 1
        save_qr(n, counter)