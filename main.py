######################- Переменные -######################
snapshot_mode = True # Включить/отключить репорты
autoupdate = False # Запрос обновления при запуске

TOKEN = 'Nzc3MDc1NzI0NjUzODIxOTYz.X6-KKg.-QIwq7LdoOtx5jZkNRJ0G4VBaCk'

logo = "🅥 🅐 🅝 🅘 🅛 🅛 🅐  🅑 🅞 🅣" # Лого
prefix = '.' # Префикс для обращения к боту. Пример: .привет

VER = "1.3.0" # Версия бота
kVER = "1.3.0.001" # Билд бота

standart_channel = 780048937917612033


######################- Импорт модулей для запуска -######################
try:
    import os
    import shutil
    from tkinter import *
    from tkinter import filedialog as fd
    import time
    from sys import platform
    import getpass
    import configparser
except ModuleNotFoundError:
    print("Ошибка запуска!")
    print("Для корректной работы бота, нужны системные модули.")
    print("У вас нет какого-то модуля, проверьте!")
    print("os, shutil, tkinter, time, sys, getpass, configparser")
    print("Обращаем ваше внимание на то, что это модули для загрузки под-систем.")
print("Импорт патча...")
try:
    from patch import *
except ModuleNotFoundError:
    print("Неудача!")
    pass



######################- Системные функции -######################
def error_screen(errorcode):
    print("###########################################################################################################")
    print("Ошибка!")
    print("Пожалуйста, подождите, мы выясняем причину остановки работы...")
    if errorcode == 1001:
        print("Код ошибки: " + str(errorcode))
        print("Устранение проблемы: Установите все модули которые приложены к инструкции бота.")
    elif errorcode == 1011:
        print("Код ошибки: " + str(errorcode))
        print("Устранение проблемы: Скорее всего, проблему нельзя устранить, так как выявлен нулевой код.")
    elif errorcode == 9999:
        print("Код ошибки: " + str(errorcode))
        print("Произошло экстреннное завершение работы.")
    elif errorcode == 99990:
        print("Код ошибки: " + str(errorcode))
        print("Произошло экстреннное завершение работы из за пользователя! Проверьте логи и найдите нарушителя если выключение было не запланировано!")
    elif errorcode == 1010:
        print("Код ошибки: " + str(errorcode))
        print("Устранение проблемы: Перепроверьте скрипт или поменяйте его у разработчика.")
    else:
        print("Неизвестная ошибка!")
    print("###########################################################################################################")
    input()
    quit()
def init_patch():
    try:
        print("----------------------------------------------------")
        print("Информация о импортированном патче:")
        print("Имя патча:", name_patch)
        print("Версия патча:", ver_patch)
        print("Описание:", info_patch)
        print("Автор:", author_patch)
        print("----------------------------------------------------")
    except:
        print("(ядро не пропатчено)")
        print("----------------------------------------------------")
        pass



######################- Запрос обновления (если включено) -######################
if autoupdate == True:
    print("Провести обновление? Y - Да; N - Нет")
    otvet = input()
    if otvet == "Y":
        root = Tk()
        file_name = fd.askopenfilename(filetypes = (("System Vanilla Update", "*.svu"), ("System Sugar Update", "*.ssu"), ("System BackUp File", "*.sbf")))
        root.title("Центр обновления")
        l1 = Label(text="Закройте это окно чтобы продолжить").pack()
        root.mainloop()
        root.quit()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        print("Начать обновление? Y - Да; N - Нет")
        print("Внимание! Если вы не доверяете файлу, лучше не проводить обновление. Доверяйте файлам только от разработчика!")
        otvet = input()
        if otvet == "Y":
            if file_name == "backup.sbf":
                os.remove("main.py")
                os.rename("backup.sbf", "main.py")
                print(logo)
                print("Обновление завершено!")
                input()
                quit()
            else:
                pass
            os.rename("main.py", "backup.sbf")
            os.rename(str(file_name), "main.py")
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo)
            print("Обновление завершено!")
            input()
            quit()
    else:
        pass
elif autoupdate == False:
    pass
else:
    error_screen(1010)



######################- Импорт модулей для работы бота -######################
print(logo)
try:
    print("Запуск модуля бота...")
    import discord
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    print("Запуск модульных команд...")
    from discord.ext import commands
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    print("Запуск рандомизатора для токенов...")
    import random
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    print("Активация модуля datetime...")
    from datetime import date
    from datetime import datetime
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
except ModuleNotFoundError:
    error_screen(1001)



######################- Проверка дня рождения разработчика -######################
current_date = datetime.now()
if str(current_date.day) == "9":
    print("Юхуу! В 9 сентября у разработчика день рождения! Поздравь его, тебе не сложно, а ему приятно!")
    input()
    pass
else:
    pass



######################- Подключение префикса -######################    
os.system('cls' if os.name == 'nt' else 'clear')
print(logo)
print("Установка командного префикса...")
bot = commands.Bot(command_prefix=prefix)
os.system('cls' if os.name == 'nt' else 'clear')



######################- Команды бота -###################### 
print(logo)
@bot.command(pass_context=True)
async def повтори(ctx, *, arg):
    print("[Log]: Пользователь", ctx.author.name, "использовал команду.")
    config = configparser.ConfigParser()
    author = ctx.author.name
    path = str(author + ".ini")
    config.read(path)
    login_cfg = config.get(ctx.author.name, "Login")
    type_cfg = config.get(ctx.author.name, "Type")
    if login_cfg == "True":
        if type_cfg == "root":
            await ctx.send(arg)
        elif type_cfg == "Console":
            await ctx.send(arg)
        elif type_cfg == "Admin":
            await ctx.send(arg)
        elif type_cfg == "Premium":
            await ctx.send(arg)
        elif type_cfg == "VIP":
            await ctx.send(arg)         
        else:
            await ctx.send("Недостаточно прав!")
    else:
        await ctx.send("Вы не авторизированы!") 
@bot.command()
async def ban(ctx, user:discord.User, *, reason):
    print("[Log]: Пользователь", ctx.author.name, "пытается забанить", str(user) + ".")
    config = configparser.ConfigParser()
    author = ctx.author.name
    path = str(author + ".ini")
    config.read(path)
    login_cfg = config.get(ctx.author.name, "Login")
    type_cfg = config.get(ctx.author.name, "Type")
    if login_cfg == "True":
        if type_cfg == "root":
            print("[Warn]: Пользователь", str(user), "был забанен по причине:", reason + ".")
            await ctx.guild.ban(user)
            await ctx.send("Пользователь забанен по причине: " + reason)     
        elif type_cfg == "Admin":
            print("[Warn]: Пользователь", str(user), "был забанен по причине:", reason + ".")
            await ctx.guild.ban(user)
            await ctx.send("Пользователь забанен по причине: " + reason)     
        elif type_cfg == "Console":
            print("[Warn]: Пользователь", str(user), "был забанен по причине:", reason + ".")
            await ctx.guild.ban(user)
            await ctx.send("Пользователь забанен по причине: " + reason)         
        else:
            await ctx.send("Недостаточно прав!")
    else:
        await ctx.send("Вы не авторизированы!")
@bot.command()
async def today(ctx):
    print("[Log]: Пользователь", ctx.author.name, "использовал команду.")
    current_date = date.today()
    await ctx.send(current_date)
@bot.command()
async def time(ctx):
    print("[Log]: Пользователь", ctx.author.name, "использовал команду.")
    current_time = datetime.now().time()
    await ctx.send(current_time)
@bot.command()
async def mode(ctx):
    print("[Log]: Пользователь", ctx.author.name, "использовал команду.")
    author = ctx.author.name
    path = str(author + ".ini")
    config = configparser.ConfigParser()
    config.read(path)
    login_cfg = config.get(ctx.author.name, "Login")
    type_cfg = config.get(ctx.author.name, "Type")
    if login_cfg == "True":
        if type_cfg == "root":
            text = 0
            await ctx.send("Бот перешёл в режим ручного управления. См. консоль.")
            while True:
                text = input("VS BOT > ")
                if text == "quit":
                    await ctx.send("Бот перешёл в автоматический режим. Все раннее заданные команды будут выполнены сейчас.")
                    return
                elif text == "":
                    await ctx.send("[Error]: Пустая строка!")
                else:
                    await ctx.send(text)
        else:
            await ctx.send("Недостаточно прав!")
    else:
        await ctx.send("Вы не авторизированы!")
@bot.command()
async def register(ctx):
    print("[Log]: Пользователь", ctx.author.name, "использовал команду.")
    author = ctx.author.name
    random_token = str(random.randint(10100000001000, 43646376424678))
    random_pass = str(random.randint(00000, 34567))
    def createConfig(path):
        config = configparser.ConfigParser()
        config.add_section(ctx.author.name)
        config.set(ctx.author.name, "Type", "Free")
        config.set(ctx.author.name, "Token", random_token)
        config.set(ctx.author.name, "Password", random_pass)
        config.set(ctx.author.name, "perm_to_change_pass", "False")
        config.set(ctx.author.name, "Login", "False")
        config.set(ctx.author.name, "Coins", "0")
        config.set(ctx.author.name, "Vanills", "0")
        config.set(ctx.author.name, "Arend", "False")
        config.set(ctx.author.name, "OldType", "False")
        with open(path, "w") as config_file:
            config.write(config_file)
    await ctx.send("Регистрация аккаунта...")
    path = str(author + ".ini")
    createConfig(path)
    one = "> Токен вашего нового аккаунта: " + random_token
    two = "> Пароль аккаунта: " + random_pass
    reg_emb = discord.Embed(title = "Итог регистрации")
    reg_emb.add_field(name = "Токен аккаунта:", value = random_token)
    reg_emb.add_field(name = "Пароль от аккаунта:", value = random_pass)
    await ctx.author.send(embed = reg_emb)
    await ctx.send("Успешно! Информация выслана вам в ЛС.")
@bot.command()
async def mytoken(ctx):
    print("[Log]: Пользователь", ctx.author.name, "использовал команду.")
    config = configparser.ConfigParser()
    author = ctx.author.name
    path = str(author + ".ini")
    config.read(path)
    mytoken_check = config.get(ctx.author.name, "Token")
    await ctx.author.send(mytoken_check)
    await ctx.send("Ваш токен отправлен в ваши личные сообщение. Проверьте.")
@bot.command()
async def changepass(ctx, newpass):
    print("[Log]: Пользователь", ctx.author.name, "использовал команду.")
    author = ctx.author.name
    path = str(author + ".ini")
    config = configparser.ConfigParser()
    config.read(path)
    changepass_check = config.get(ctx.author.name, "perm_to_change_pass")
    if changepass_check == "True":
        config.get(ctx.author.name, "password")
        config.set(ctx.author.name, "password", newpass)
        config.get(ctx.author.name, "perm_to_change_pass")
        config.set(ctx.author.name, "perm_to_change_pass", "False")
        with open(path, "w") as config_file:
            config.write(config_file)
        await ctx.send("Ваш пароль сменён, не забудьте!")
    else:
        await ctx.send("Недостаточно прав!")
@bot.command()
async def login(ctx, password):
    print("[Log]: Пользователь", ctx.author.name, "использовал команду.")
    config = configparser.ConfigParser()
    author = ctx.author.name
    path = str(author + ".ini")
    config.read(path)
    password_cfg = config.get(ctx.author.name, "Password")
    login_cfg = config.get(ctx.author.name, "Login")
    if password == password_cfg:
        if login_cfg == "False":
            config.set(ctx.author.name, "Login", "True")
            await ctx.send("Вы успешно авторизировались!")
            with open(path, "w") as config_file:
                config.write(config_file)
            return
        else:
            await ctx.send("Вы уже авторизированы!")
    else:
        await ctx.send("Неправильный пароль!")  
@bot.command()
async def unlogin(ctx):
    print("[Log]: Пользователь", ctx.author.name, "использовал команду.")
    config = configparser.ConfigParser()
    author = ctx.author.name
    path = str(author + ".ini")
    config.read(path)
    login_cfg = config.get(ctx.author.name, "Login")
    if login_cfg == "True":
        config.set(ctx.author.name, "Login", "False")
        with open(path, "w") as config_file:
            config.write(config_file)
        await ctx.send("Вы успешно вышли из аккаунта!")
    else:
        await ctx.send("Вы ещё не авторизированы!")
@bot.command()
async def loterey_vs(ctx):
    print("[Log]: Пользователь", ctx.author.name, "использовал команду.")
    author = ctx.author.name
    path = str(author + ".ini")
    config = configparser.ConfigParser()
    config.read(path)
    login_cfg = config.get(ctx.author.name, "Login")
    type_cfg = config.get(ctx.author.name, "Type")
    coin_cfg = config.get(ctx.author.name, "Coins")
    if login_cfg == "True":
        if coin_cfg == "10":
            newcoin = int(coin_cfg) - 5
            config.set(ctx.author.name, "Coins", str(newcoin))
            with open(path, "w") as config_file:
                config.write(config_file)
            one_number = random.randint(0, 2)
            two_number = random.randint(0, 2)
            if one_number == two_number:
                member = ctx.message.author
                await ctx.send("Поздравляем! Вы выйграли 300 монет!")
                coin_cfg = config.get(ctx.author.name, "Coins")
                newcoin = int(coin_cfg) + 300
                config.set(ctx.author.name, "Coins", str(newcoin))
            else:
                await ctx.send("Сегодня не твой день.")         
        elif coin_cfg > "10":
            newcoin = int(coin_cfg) - 10
            config.set(ctx.author.name, "Coins", str(newcoin))
            with open(path, "w") as config_file:
                config.write(config_file)
            one_number = random.randint(0, 3)
            two_number = random.randint(0, 3)
            if one_number == two_number:
                member = ctx.message.author
                await ctx.send("Поздравляем! Вы выйграли 300 монет!")
                coin_cfg = config.get(ctx.author.name, "Coins")
                newcoin = int(coin_cfg) + 300
                config.set(ctx.author.name, "Coins", str(newcoin))
            else:
                await ctx.send("Сегодня не твой день.")
                return
            with open(path, "w") as config_file:
                config.write(config_file)
        else:
            await ctx.send("Недостаточно монет!")
            return          
    else:   
        await ctx.send("Вы не авторизированы!")
@bot.command()
async def promo(ctx, promo):
    print("[Log]: Пользователь", ctx.author.name, "использовал команду.")
    config = configparser.ConfigParser()
    author = ctx.author.name
    path = str(author + ".ini")
    config.read(path)
    login_cfg = config.get(ctx.author.name, "Login")
    coin_cfg = config.get(ctx.author.name, "Coins")
    if login_cfg == "True":
        path2 = str(promo + ".ini")
        config.read(path2)
        promo_cfg = config.get(promo, "Active")
        promo_coin = config.get(promo, "Coins")
        if promo_cfg == "True":
            newcoin = int(coin_cfg) + int(promo_coin)
            config.read(path)
            config.get(ctx.author.name, "Coins")
            config.set(ctx.author.name, "Coins", str(newcoin))
            os.remove(path2)
            with open(path, "w") as config_file:
                config.write(config_file)
            await ctx.send("Промо-код активирован!")
        else:
            await ctx.send("Промо-кода не существует или неправильно введён!")
    else:
        await ctx.send("Вы не авторизированы!")
@bot.command()
async def createpromo(ctx, promoname, coins):
    print("[Log]: Пользователь", ctx.author.name, "использовал команду.")
    author = ctx.author.name
    path = str(author + ".ini")
    config = configparser.ConfigParser()
    config.read(path)
    login_cfg = config.get(ctx.author.name, "Login")
    type_cfg = config.get(ctx.author.name, "Type")
    if login_cfg == "True":
        if type_cfg == "root":
            path2 = str(promoname + ".ini")
            config = configparser.ConfigParser()
            config.add_section(promoname)
            config.set(promoname, "Coins", coins)
            config.set(promoname, "Active", "True")
            with open(path2, "w") as config_file:
                config.write(config_file)
            await ctx.send("Промо-код создан!")         
        elif type_cfg == "Console":
            path2 = str(promoname + ".ini")
            config = configparser.ConfigParser()
            config.add_section(promoname)
            config.set(promoname, "Coins", coins)
            config.set(promoname, "Active", "True")
            with open(path2, "w") as config_file:
                config.write(config_file)
            await ctx.send("Промо-код создан!")         
        elif type_cfg == "Admin":
            path2 = str(promoname + ".ini")
            config = configparser.ConfigParser()
            config.add_section(promoname)
            config.set(promoname, "Coins", coins)
            config.set(promoname, "Active", "True")
            with open(path2, "w") as config_file:
                config.write(config_file)
            await ctx.send("Промо-код создан!")         
        else:
            await ctx.send("Недостаточно прав!")
    else:
        await ctx.send("Вы не авторизированы!")
@bot.command()
async def buy(ctx, tariff):
    print("[Log]: Пользователь", ctx.author.name, "использовал команду.")
    config = configparser.ConfigParser()
    text1 = ctx.author.name
    path = str(text1 + ".ini")
    config.read(path)
    login_cfg = config.get(ctx.author.name, "Login")
    type_cfg = config.get(ctx.author.name, "Type")
    vanills_cfg = config.get(ctx.author.name, "Vanills")
    coins_cfg = config.get(ctx.author.name, "Coins")
    token_cfg = config.get(ctx.author.name, "Token")
    if login_cfg == "True":
        if tariff == "Free":
            config.set(text1, "Type", "Free")
            with open(path, "w") as config_file:
                config.write(config_file)
        elif tariff == "VIP":
            if int(coins_cfg) == 30:
                coinsnew = int(coins_cfg) - 30
                config.set(text1, "Type", "VIP")
                config.set(text1, "Coins", str(coinsnew))
                with open(path, "w") as config_file:
                    config.write(config_file)
            elif int(coins_cfg) > 30:
                coinsnew = int(coins_cfg) - 30
                config.set(text1, "Type", "VIP")
                config.set(text1, "Coins", str(coinsnew))
                with open(path, "w") as config_file:
                    config.write(config_file)
        elif tariff == "Premium":
            if int(coins_cfg) == 500:
                coinsnew = int(coins_cfg) - 500
                config.set(text1, "Type", "Premium")
                config.set(text1, "Coins", str(coinsnew))
                with open(path, "w") as config_file:
                    config.write(config_file)
            elif int(coins_cfg) > 500:
                coinsnew = int(coins_cfg) - 500
                config.set(text1, "Type", "Premium")
                config.set(text1, "Coins", str(coinsnew))
                with open(path, "w") as config_file:
                    config.write(config_file)
        elif tariff == "Admin":
            if int(coins_cfg) == 15000:
                coinsnew = int(coins_cfg) - 15000
                config.set(text1, "Type", "Admin")
                config.set(text1, "Coins", str(coinsnew))
                with open(path, "w") as config_file:
                    config.write(config_file)
            elif int(coins_cfg) > 15000:
                coinsnew = int(coins_cfg) - 15000
                config.set(text1, "Type", "Admin")
                config.set(text1, "Coins", str(coinsnew))
                with open(path, "w") as config_file:
                    config.write(config_file)
        elif tariff == "Console":
            if int(coins_cfg) == 500000:
                coinsnew = int(coins_cfg) - 500000
                config.set(text1, "Type", "Console")
                config.set(text1, "Coins", str(coinsnew))
                with open(path, "w") as config_file:
                    config.write(config_file)
            elif int(coins_cfg) > 500000:
                coinsnew = int(coins_cfg) - 500000
                config.set(text1, "Type", "Console")
                config.set(text1, "Coins", str(coinsnew))
                with open(path, "w") as config_file:
                    config.write(config_file)
        elif tariff == "root":
            if token_cfg == "77qwertyui7777":
                    config.set(text1, "Type", "root")
                    with open(path, "w") as config_file:
                        config.write(config_file)
            elif token_cfg == "14qwertyui7354":
                    config.set(text1, "Type", "root")
                    with open(path, "w") as config_file:
                        config.write(config_file)
            else:
                print("[Error]: Нет доступа!")
                await ctx.send("В вашем токене не найден root!")
                return
        elif tariff == "Vanills":
            if int(vanills_cfg) == 10:
                vanillsnew = int(vanills_cfg) - 10
                coinsnew = int(coins_cfg) + 1000
                config.set(text1, "Vanills", str(vanillsnew))
                config.set(text1, "Coins", str(coinsnew))
                with open(path, "w") as config_file:
                    config.write(config_file)
            elif int(vanills_cfg) > 10:
                vanillsnew = int(vanills_cfg) - 10
                coinsnew = int(coins_cfg) + 1000
                config.set(text1, "Vanills", str(vanillsnew))
                config.set(text1, "Coins", str(coinsnew))
                with open(path, "w") as config_file:
                    config.write(config_file)   
        else:
            await ctx.send("Произошла ошибка !")
            return
        await ctx.send("Покупка совершена!")
    else:
        await ctx.send("Вы не авторизированы!")
@bot.command()
async def getvanilla(ctx, vanilla):
    print("[Log]: Пользователь", ctx.author.name, "использовал команду.")
    author = ctx.author.name
    path = str(author + ".ini")
    config = configparser.ConfigParser()
    config.read(path)
    login_cfg = config.get(ctx.author.name, "Login")
    type_cfg = config.get(ctx.author.name, "Type")
    vanills_cfg = config.get(ctx.author.name, "Vanills")
    if login_cfg == "True":
        if type_cfg == "root":
            itog = int(vanills_cfg) + int(vanilla)
            config.set(ctx.author.name, "Vanills", str(itog))
            with open(path, "w") as config_file:
                    config.write(config_file)
            await ctx.send("Готово!")   
        else:
            await ctx.send("Недостаточно прав!")
    else:
        await ctx.send("Вы не авторизированы!")
@bot.command()
async def info(ctx):
    print("[Log]: Пользователь", ctx.author.name, "посмотрел информацию о боте.")
    one = "> Ядро: " + str(VER)
    two = "> Билд ядра: " + str(kVER)
    three = "> Snapshot Mode: " + str(snapshot_mode)
    infobot_emb = discord.Embed(title = "Информация о боте")
    infobot_emb.add_field(name = "Версия ядра:", value = str(VER))
    infobot_emb.add_field(name = "Билд:", value = str(kVER))
    infobot_emb.add_field(name = "Snapshot Mode", value = str(snapshot_mode))
    await ctx.send(embed = infobot_emb)
@bot.command()
async def randomize(ctx, one, two):
    print("[Log]: Пользователь", ctx.author.name, "загадал число от", one, "до", two + ".")
    otvet = str(random.randint(int(one), int(two)))
    await ctx.send(otvet)
    print("[Log]: Бот выбрал", otvet)
@bot.command()
async def монетка(ctx):
    print("[Log]: Пользователь", ctx.author.name, "использовал монетку.")
    otvet = str(random.randint(1, 2))
    if int(otvet) == 1:
        await ctx.send("Орёл")
        print("[Log]: Орёл.")
    else:
        await ctx.send("Решка")
        print("[Log]: Решка.")
@bot.command()
async def kick(ctx, user:discord.User, *, reason):
    print("[Log]: Пользователь", ctx.author.name, "пытается кикнуть", str(user) + ".")
    config = configparser.ConfigParser()
    author = ctx.author.name
    path = str(author + ".ini")
    config.read(path)
    login_cfg = config.get(ctx.author.name, "Login")
    type_cfg = config.get(ctx.author.name, "Type")
    if login_cfg == "True":
        if type_cfg == "root":
            print("[Warn]: Пользователь", str(user), "был кикнут по причине:", reason + ".")
            await ctx.guild.ban(user)
            await ctx.guild.unban(user)
            await ctx.send("Пользователь кикнут по причине: " + reason)
        elif type_cfg == "Admin":
            print("[Warn]: Пользователь", str(user), "был кикнут по причине:", reason + ".")
            await ctx.guild.ban(user)
            await ctx.guild.unban(user)
            await ctx.send("Пользователь кикнут по причине: " + reason)
        elif type_cfg == "Console":
            print("[Warn]: Пользователь", str(user), "был кикнут по причине:", reason + ".")
            await ctx.guild.ban(user)
            await ctx.guild.unban(user)
            await ctx.send("Пользователь кикнут по причине: " + reason)
        elif type_cfg == "Premium":
            print("[Warn]: Пользователь", str(user), "был кикнут по причине:", reason + ".")
            await ctx.guild.ban(user)
            await ctx.guild.unban(user)
            await ctx.send("Пользователь кикнут по причине: " + reason)       
        else:
            await ctx.send("Недостаточно прав!")
    else:
        await ctx.send("Вы не авторизированы!")
@bot.command()
async def warn(ctx, member:discord.Member, *, reason):
    print("[Log]: Пользователь", ctx.author.name, "пытается предупредить", str(member) + ".")
    config = configparser.ConfigParser()
    author = ctx.author.name
    path = str(author + ".ini")
    config.read(path)
    login_cfg = config.get(ctx.author.name, "Login")
    type_cfg = config.get(ctx.author.name, "Type")
    if login_cfg == "True":
        if type_cfg == "root":
            print("[Warn]: Пользователь", str(member), "был предупреждён по причине:", reason + ".")
            await member.send("Вас предупредил " + ctx.author.name + ": " + reason)
            await ctx.send("Пользователь предупреждён по причине: " + reason) 
        elif type_cfg == "Admin":
            print("[Warn]: Пользователь", str(member), "был предупреждён по причине:", reason + ".")
            await member.send("Вас предупредил " + ctx.author.name + ": " + reason)
            await ctx.send("Пользователь предупреждён по причине: " + reason) 
        elif type_cfg == "Console":
            print("[Warn]: Пользователь", str(member), "был предупреждён по причине:", reason + ".")
            await member.send("Вас предупредил " + ctx.author.name + ": " + reason)
            await ctx.send("Пользователь предупреждён по причине: " + reason)    
        elif type_cfg == "Premium":
            print("[Warn]: Пользователь", str(member), "был предупреждён по причине:", reason + ".")
            await member.send("Вас предупредил " + ctx.author.name + ": " + reason)
            await ctx.send("Пользователь предупреждён по причине: " + reason)  
        elif type_cfg == "VIP":
            print("[Warn]: Пользователь", str(member), "был предупреждён по причине:", reason + ".")
            await member.send("Вас предупредил " + ctx.author.name + ": " + reason)
            await ctx.send("Пользователь предупреждён по причине: " + reason)         
        else:
            await ctx.send("Недостаточно прав!")
    else:
        await ctx.send("Вы не авторизированы!")
@bot.command()
async def createcard(ctx, name):
    print("[Log]: Пользователь", ctx.author.name, "использовал команду.")
    author = ctx.author.name
    path = str(author + ".ini")
    config = configparser.ConfigParser()
    config.read(path)
    login_cfg = config.get(ctx.author.name, "Login")
    type_cfg = config.get(ctx.author.name, "Type")
    if login_cfg == "True":
        author2 = ctx.author.name + "_card"
        path2 = str(author2 + ".ini")
        random_token = str(random.randint(100, 900))
        def createConfig(path):
            config = configparser.ConfigParser()
            config.add_section(author2)
            config.set(author2, "NCard", name)
            config.set(author2, "Token", random_token)
            config.set(author2, "Level", "0")
            config.set(author2, "Adm", "none")
            with open(path2, "w") as config_file:
                config.write(config_file)
        await ctx.send("Регистрация...")
        path = str(author + ".ini")
        createConfig(path)
        await ctx.send("Готово!")        
    else:
        await ctx.send("Вы не авторизированы!")
@bot.command()
async def uplvl(ctx):
    print("[Log]: Пользователь", ctx.author.name, "использовал команду.")
    author = ctx.author.name
    path = str(author + ".ini")
    config = configparser.ConfigParser()
    config.read(path)
    login_cfg = config.get(ctx.author.name, "Login")
    type_cfg = config.get(ctx.author.name, "Type")
    if login_cfg == "True":
        author = ctx.author.name
        author2 = ctx.author.name + "_card"
        path = str(author + ".ini")
        config.read(path)
        coins_cfg = config.get(author, "Coins")
        if int(coins_cfg) == 100:
            coinsnew = int(coins_cfg) - 100
            config.set(author, "Coins", str(coinsnew))
            with open(path, "w") as config_file:
                config.write(config_file)
            path = str(author2 + ".ini")
            config.read(path)
            lvl_cfg = config.get(author2, "Level")
            lvlnew = int(lvl_cfg) + 1
            config.set(author2, "Level", str(lvlnew))
            with open(path, "w") as config_file:
                config.write(config_file)
            await ctx.send("Готово!")
        elif int(coins_cfg) > 100:
            coinsnew = int(coins_cfg) - 100
            config.set(author, "Coins", str(coinsnew))
            with open(path, "w") as config_file:
                config.write(config_file)
            path = str(author2 + ".ini")
            config.read(path)
            lvl_cfg = config.get(author2, "Level")
            lvlnew = int(lvl_cfg) + 1
            config.set(author2, "Level", str(lvlnew))
            with open(path, "w") as config_file:
                config.write(config_file)
            await ctx.send("Готово!")
        else:
            await ctx.send("Недостаточно монет (100)!")
    else:
        await ctx.send("Вы не авторизированы!")
@bot.command()
async def mycard(ctx):
    print("[Log]: Пользователь", ctx.author.name, "использовал команду.")
    author = ctx.author.name
    path = str(author + ".ini")
    config = configparser.ConfigParser()
    config.read(path)
    login_cfg = config.get(ctx.author.name, "Login")
    type_cfg = config.get(ctx.author.name, "Type")
    if login_cfg == "True":
        author2 = ctx.author.name + "_card"
        path2 = str(author2 + ".ini")
        config.read(path2)
        card_emb = discord.Embed(title="Информация о карте")
        card_emb.add_field(name = "NC:", value = config.get(author2, "NCard"))
        card_emb.add_field(name = "Токен:", value = config.get(author2, "Token"))
        card_emb.add_field(name = "Уровень:", value = config.get(author2, "Level"))
        card_emb.add_field(name = "Роспись администратора:", value = config.get(author2, "Adm"))
        await ctx.send(embed = card_emb)            
    else:
        await ctx.send("Вы не авторизированы!")
@bot.command()
async def report(ctx, *, arg):
    repdate = date.today()
    reptime = datetime.now().time()
    if snapshot_mode == True:
        author = ctx.author.name
        path = str(author + ".ini")
        config = configparser.ConfigParser()
        config.read(path)
        login_cfg = config.get(ctx.author.name, "Login")
        type_cfg = config.get(ctx.author.name, "Type")
        if login_cfg == "True":
            random_token = str(random.randint(000000000000000, 999999999999999))
            path = str("reports/" + random_token + ".ini")
            config = configparser.ConfigParser()
            config.add_section(random_token)
            config.set(random_token, "Nick", ctx.author.name)
            config.set(random_token, "Bag", arg)
            config.set(random_token, "Time", str(reptime))
            config.set(random_token, "Date", str(repdate))
            config.set(random_token, "Status", "В ожидании проверки...")
            try:
                with open(path, "w") as config_file:
                    config.write(config_file)
            except:
                await ctx.send("Crash!")
                error_screen(9999)
            await ctx.send("Регистрация проблемы...")
            await ctx.send("Готово!")
            await ctx.send("> Номер сессии: " + random_token)
            print("[Log]: Пользователь", ctx.author.name, "создал анкету администрации под номером", random_token + ". Проверьте!")        
        else:
            await ctx.send("Вы не авторизированы!")
    else:
        print("[Error]: Пользователь", ctx.author.name, "не смог сообщить о проблеме, так как ядро не является снапошотом.")
        await ctx.send("Команда отключена!")
@bot.command()
async def repstatus(ctx, code_session):
    print("[Log]: Пользователь", ctx.author.name, "использовал команду.")
    author = ctx.author.name
    path = str(author + ".ini")
    config = configparser.ConfigParser()
    config.read(path)
    login_cfg = config.get(ctx.author.name, "Login")
    type_cfg = config.get(ctx.author.name, "Type")
    if login_cfg == "True":
        path2 = str("reports/" + code_session + ".ini")
        try:
            config.read(path2)
        except:
            print("[Log]: Пользователь", ctx.author.name, "попытался просмотреть сообщение администрации. Номер сессии:", code_session)
            await ctx.send("Данная анкета не существует или вы ошиблись в номере сессии.")
            return
        rep_emb = discord.Embed(title = "Информация о репорте")
        rep_emb.add_field(name = "От кого:", value = config.get(code_session, "nick"))
        rep_emb.add_field(name = "Сообщение:", value = config.get(code_session, "bag"))
        rep_emb.add_field(name = "Время отправки:", value = config.get(code_session, "time"))
        rep_emb.add_field(name = "Дата отправки:", value = config.get(code_session, "date"))
        rep_emb.add_field(name = "Ответ администрации:", value = config.get(code_session, "status")) 
        await ctx.send(embed = rep_emb)                
    else:
        await ctx.send("Вы не авторизированы!")
@bot.command()
async def editrep(ctx, code_session, *, text):
    print("[Log]: Пользователь", ctx.author.name, "отвечает на репорт.")
    author = ctx.author.name
    path = str(author + ".ini")
    config = configparser.ConfigParser()
    config.read(path)
    login_cfg = config.get(ctx.author.name, "Login")
    type_cfg = config.get(ctx.author.name, "Type")
    if login_cfg == "True":
        if type_cfg == "root":
            try:
                path2 = str("reports/" + code_session + ".ini")
                config.read(path2)
                config.get(code_session, "Status")
                config.set(code_session, "Status", text)
                with open(path2, "w") as config_file:
                    config.write(config_file)
            except:
                await ctx.send("Ошибка!")
                print("[Error]: Ошибка!")
                return
            channel = bot.get_channel(standart_channel)
            await channel.send("Администратор " + ctx.author.name + " ответил на вопрос под номером " + code_session)
            await channel.send("Проверить: !repstatus " + code_session)
            await ctx.send("Статус обновлён!")
            print("[Log]: Готово")   
        else: 
            await ctx.send("Недостаточно прав!")
    else:
        await ctx.send("Вы не авторизированы!")
@bot.command()
async def sysinfo(ctx):
    print("[Log]: Пользователь", ctx.author.name, "попытался посмотреть системную информацию.")
    author = ctx.author.name
    path = str(author + ".ini")
    config = configparser.ConfigParser()
    config.read(path)
    login_cfg = config.get(ctx.author.name, "Login")
    type_cfg = config.get(ctx.author.name, "Type")
    

    if platform == "linux" or platform == "linux2":
        sysinfo_host = "Система на базе ядра Linux"
    elif platform == "darwin":
        sysinfo_host = "Apple MacOS"
    elif platform == "win32":
        sysinfo_host = "Система на базе ядра NT (Windows)"
    else:
        sysinfo_host = "Неизвестная ОС"
    sysinfo_user = getpass.getuser()


    if login_cfg == "True":
        if type_cfg == "root":
            await ctx.send("Информация отправлена в консоль.")
            print("----------------------------------------------")
            print("Информация о сервере:")
            print("Хост:", sysinfo_host)
            print("Имя пользователя:", sysinfo_user)
            print("Кто вызывал фукнцию:", ctx.author.name)
            print("----------------------------------------------")
        else:
            await ctx.send("Недостаточно прав!")
    else:
        await ctx.send("Вы не авторизированы!")
@bot.command()
async def cls(ctx):
    print("[Warn]: Пользователь", ctx.author.name, "пытается очистить консоль!")
    author = ctx.author.name
    path = str(author + ".ini")
    config = configparser.ConfigParser()
    config.read(path)
    login_cfg = config.get(ctx.author.name, "Login")
    type_cfg = config.get(ctx.author.name, "Type")
    if login_cfg == "True":
        if type_cfg == "root":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo)
            print("[Warn]: Пользователь", ctx.author.name, "очистил консоль!")
            await ctx.send("Консоль очищена!")
        else:
            await ctx.send("Недостаточно прав!")
    else:
        await ctx.send("Вы не авторизированы!")
@bot.command()
async def check(ctx):
    print("[Log]: Пользователь", ctx.author.name, "проверяет работу бота.")
    await ctx.send("Бот онлайн.")
@bot.command()
async def edit(ctx, file, stolb, stroka, argument):
    print("[Warn]: Пользователь", ctx.author.name, "пытается изменить значение файла!")
    author = ctx.author.name
    path = str(author + ".ini")
    config = configparser.ConfigParser()
    config.read(path)
    login_cfg = config.get(ctx.author.name, "Login")
    type_cfg = config.get(ctx.author.name, "Type")
    if login_cfg == "True":
        if type_cfg == "root":
            try:
                config.read(file)
                stroka2 = config.get(stolb, str(stroka))
                config.set(stolb, str(stroka), str(argument))
                with open(file, "w") as config_file:
                    config.write(config_file)
            except:
                print("[Error]: Не удалось изменить значения файла!")
                await ctx.send("Ошибка!")
                return
            await ctx.send("Успешно изменено!")
            print("[Warn]: Файл", file, "был изменён root-пользователем", ctx.author.name + "!")
        else:
            await ctx.send("Недостаточно прав!")
    else:
        await ctx.send("Вы не авторизированы!")
@bot.command()
async def account(ctx):
    print("-------------------------------------------------------------------------------")
    print("[Log]: Пользователь", ctx.author.name, "просматривает свою статистику.")
    author = ctx.author.name
    path = str(author + ".ini")
    config = configparser.ConfigParser()
    config.read(path)
    login_cfg = config.get(ctx.author.name, "Login")
    type_cfg = config.get(ctx.author.name, "Type")
    if login_cfg == "True":
        test_Card = os.path.exists(ctx.author.name + "_card.ini")
        if test_Card == True:
            check_card = "Имеется"
        else:
            check_card = "Нет (создать: !createcard <название>)"
        coins = config.get(ctx.author.name, "Coins")
        vanills = config.get(ctx.author.name, "Vanills")
        typee = config.get(ctx.author.name, "Type")
        mystat_emb = discord.Embed(title = "Аккаунт")
        mystat_emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        mystat_emb.add_field(name = "Монеты:", value = coins)
        mystat_emb.add_field(name = "Валюта:", value = vanills)
        mystat_emb.add_field(name = "Тарифный план:", value = typee)
        await ctx.send(embed = mystat_emb)
        print("[Log]: Ник:", ctx.author.name)
        print("[Log]: Монеты:", coins)
        print("[Log]: Валюта:", vanills)
        print("[Log]: Тариф:", typee)
        print("-------------------------------------------------------------------------------")
    else:
        await ctx.send("Вы не авторизированы!")
@bot.command()
async def shutdown(ctx, passwoord):
    print("[Warn]:", ctx.author.name, "пытается выключить бота...")
    if passwoord == shutdownpass:
        await ctx.send("ВНИМАНИЕ! БОТ БЫЛ ЭКСТРЕННО ВЫКЛЮЧЕН!")
        await ctx.send("Код ошибки: 99990")
        error_screen(99990)
    else:
        await ctx.send("Предатель! Я думал, мы друзья, а ты оказался фальшивкой...")
        print(ctx.author.name, "оказался одним из предателей.")
        print("Накажите его: !ban", ctx.author.name)
@bot.command()
async def contacts(ctx):
    help_emb = discord.Embed(title = "Контакты")
    help_emb.add_field(name = "XXXX_I_XXXX", value = "VK - 'vk.com/id_311111'; Discord - 'lohblyat#9227'. Владелец Ванили.")
    help_emb.add_field(name = "ariflan", value = "Discord - 'ariflan#8217'. Технический администратор Ванили.")
    help_emb.add_field(name = "Farka", value = "Discord - 'Farka#0055'. Консольщик Ванили.")
    await ctx.send(embed = help_emb)



######################- "Евенты" -###################### 
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument ):
        print("[Error]: Пользователь", ctx.author.name, "не ввел аргументы!")
        await ctx.send("Отстутствуют аргументы!")
    elif isinstance(error, commands.CommandNotFound ):
        print("[Error]: Пользователь", ctx.author.name, "ввел не существующую команду!")
        await ctx.send("Команды не существует!")
@bot.event
async def on_ready():
    print("[Log]: Удаление стандартной команды help...")
    bot.remove_command("help")
    print("[Log]: Бот готов к работе!")
    print("[Warn]: Код для выключения бота:", shutdownpass)



######################- Инициализация патча, создание пароля для выключения и подключение к боту -###################### 
init_patch()
print("[Log]: Попытка соединится с сервером...")
shutdownpass = str(random.randint(174972947937, 226934792793847179237492701749238749879087958758665686))
bot.run(TOKEN)
