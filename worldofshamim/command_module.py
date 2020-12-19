import os


def run_full_stack():

    # Firing the node server
    os.chdir(
        'C:\\Users\\B A T  M A C H I N E\\Dropbox\\batman-year-one\\byo-repo\\server')
    os.system("start cmd /K npm run dev")

    # Firing Next/CRA Server
    os.chdir(
        'C:\\Users\\B A T  M A C H I N E\\Dropbox\\batman-year-one\\byo-repo\\client')
    os.system("start cmd /K npm run dev")

    # Firing Sass Engine and opening visual studio code
    os.chdir(
        'C:\\Users\\B A T  M A C H I N E\\Dropbox\\batman-year-one\\byo-repo\\client')
    os.system("start cmd /K npm run compile-sass && code")


def run_server():
    # Firing the node server
    os.chdir(
        'C:\\Users\\B A T  M A C H I N E\\Dropbox\\batman-year-one\\byo-repo\\server')
    os.system("start cmd /K npm run dev")


def run_full_stack_v2():
    # Firing the node server
    os.chdir(
        'C:\\Users\\B A T  M A C H I N E\\Dropbox\\batman-year-one\\byo-repo\\server')
    os.system("start cmd /K npm run dev")

    # Firing Next/CRA Server
    os.chdir(
        'C:\\Users\\B A T  M A C H I N E\\Dropbox\\batman-year-one\\byo-repo\\dashboard-client')
    os.system("start cmd /K npm start")

    # Firing Sass Engine and opening visual studio code
    os.chdir(
        'C:\\Users\\B A T  M A C H I N E\\Dropbox\\batman-year-one\\byo-repo\\dashboard-client')
    os.system("start cmd /K npm run compile-sass && code")
