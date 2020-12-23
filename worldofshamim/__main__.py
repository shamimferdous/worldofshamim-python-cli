import sys
from .formatter_module import greet
from .command_module import run_full_stack, run_server, run_full_stack_v2

command = sys.argv[1] if len(sys.argv) > 1 else 'None'


def main():
    if command != 'None':
        command_tree(command)
    else:
        greet()
        implicit_command = input('\n>> ')
        command_tree(implicit_command)


if __name__ == '__main__':
    main()


def command_tree(command):
    if command == 'fire-stack':
        print(f'\n\n>>Command: {command}')
        run_full_stack()
    elif command == 'fire-server':
        print(f'\n\n>>Command: {command}')
        run_server()
    elif command == 'fire-stack-v2':
        print(f'\n\n>>Command: {command}')
        run_full_stack_v2()
