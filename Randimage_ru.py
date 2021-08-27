from PIL import Image;
import random;
import os;
import colorama;
from tkinter.filedialog import asksaveasfilename;
from tkinter import Tk;
from colorama import Fore, Back, Style;
import ctypes;
colorama.init();
ctypes.windll.kernel32.SetConsoleTitleW('Randimage');

colorama.init();
Tk().withdraw();
colorlist = [0,255];

while True:
    os.system('cls');
    print(Fore.YELLOW + 'Добро пожаловать в Randimage!' + Style.RESET_ALL);
    print('Введите 0, чтобы сгенерировать изображение');
    print('Введите 1, чтобы сгенерировать изображение в чёрно-белом варианте');
    print('Введите 2, чтобы сгенерировать изображение, используя только чёрный и белый цвета');
    print('Введите 3, чтобы сгенерировать изображение из горизонтальных линий');
    print('Введите 4, чтобы сгенерировать изображение из вертикальных линий');
    print('Введите 5, чтобы выйти');
    user_input = input();

    if user_input == '0' or '1' or '2' or '3' or '4':
        os.system('cls');
        while True:
            try:
                print('Введите путь к папке, где будет сохранён файл: ');
                p = asksaveasfilename(title='Сохранить файл',defaultextension='.png');

                n = input('Введите название файла: ');
                c = p + n + '.png';

                a = int(input('Введите ширину: '));
                b = int(input('Введите длину: '));
                
                img = Image.new('RGB', (a, b), 'white');

                if user_input == '0':
                    for i1 in range(a):
                        for i2 in range(b):
                            h1 = random.randrange(0,255);
                            h2 = random.randrange(0,255);
                            h3 = random.randrange(0,255);
                            img.putpixel((i1,i2), (h1,h2,h3));
                
                if user_input == '1':
                    for i1 in range(a):
                        for i2 in range(b):
                            h1 = random.randrange(0,255);
                            img.putpixel((i1,i2), (h1,h1,h1));
                
                if user_input == '2':
                    for i1 in range(a):
                        for i2 in range(b):
                            h1 = random.choice(colorlist);
                            img.putpixel((i1,i2), (h1,h1,h1));
                
                if user_input == '3':
                    for i2 in range(a):
                        h1 = random.randrange(0,255);
                        h2 = random.randrange(0,255);
                        h3 = random.randrange(0,255);
                        for i1 in range(b):
                            img.putpixel((i1,i2), (h1,h2,h3));

                if user_input == '4':
                    for i1 in range(a):
                        h1 = random.randrange(0,255);
                        h2 = random.randrange(0,255);
                        h3 = random.randrange(0,255);
                        for i2 in range(b):
                            img.putpixel((i1,i2), (h1,h2,h3));

                img.save(c);
                print(Fore.YELLOW + 'Готово! Нажмите Enter, чтобы вернуться в главное меню.');
                img.show();
                input();
                break;

            except Exception as e:
                print(e);
                print(Fore.RED + 'Произошла ошибка: было введено нечисловое значение.\nПопробуйте ещё раз.');
                input();
                break;

    if user_input == '5':
        break;
    
    else:
        os.system('cls');