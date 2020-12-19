from art import text2art
from colorama import Fore
from datetime import datetime
import platform


def greet():
    line_1 = text2art('Welcome Back')
    print(Fore.RED + line_1)

    line_2 = text2art('-Mr. Ferdous-')
    print(Fore.RED + line_2)

    now = datetime.now()
    line_3 = 'This is ' + \
        now.strftime('%A') + ', ' + now.strftime('%B') + \
        ' ' + now.strftime('%d') + ' ' + now.strftime('%Y')
    print(Fore.GREEN + line_3)

    line_4 = 'Current time is: ' + now.strftime("%I:%M:%S %p")
    print(line_4)

    line_5 = "You're currently on your -" + \
        platform.system() + "- machine if somehow you haven't noticed yet -.-"
    print(Fore.GREEN + line_5)

    commands()


def commands():
    cmd_1 = "\nRun command 'fire-stack' and I'll start the whole current development environment"
    print(Fore.MAGENTA + cmd_1)

    cmd_2 = "Run command 'fire-server' and I'll only start the backend server"
    print(Fore.MAGENTA + cmd_2)

    cmd_3 = "Run command 'fire-stack-v2' and I'll start the whole alternate development environment"
    print(Fore.MAGENTA + cmd_3)
