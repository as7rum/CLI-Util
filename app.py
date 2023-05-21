from docopt  import docopt
from progress.bar import ShadyBar
import random

from file_service import FileService

def main():
    # Регистрируем доступные команды для командной строки
    usage = '''
Builds and Tasks CLI.

Usage:
    app.py test
    app.py list <file_name>
    app.py get <file_name> <task_or_build_name>
'''
    # Передаем регистрацию в docopt для отлавливания запросов в командной строке
    args = docopt(usage)

    # Формируем команду test для проверки работоспособности утилиты
    if args['test']:
        with ShadyBar('Tests complite:', max=6) as bar:
            build_task_list = ['build', 'task']
            for item in build_task_list:
                service = FileService(f'data/{item}s.yaml')
                try:
                    service._FileService__get_list_of_items_from_yaml_file()
                    bar.next()
                    print(f'File "{item}s.yaml" was found.', end=' ///// ')
                    try:
                        service.get_list_of_names()
                        bar.next()
                        print(f'List function works with "{item}s.yaml" correct.',
                        end=' ///// ')
                        try:
                            service.get_item_by_name(random.choice(service.get_list_of_names()))
                            bar.next()
                            print(f'Get function works with "{item}s.yaml" correct.',
                            end=' ///// ')
                        except:
                            print(f'Get function DOES NOT works with "{item}s.yaml" correct.',
                            end=' ///// ')
                    except:
                        print(f'List function DOES NOT works with "{item}s.yaml" correct.',
                        end=' ///// ')
                except:
                    print(f'File "{item}s.yaml" was NOT found.', end=' ///// ')

    # Формируем команду list для вывода списка Задач или Билдов
    if args['list']:
        try:
            service = FileService(f'data/{args["<file_name>"]}.yaml')
            print(f'List of available {args["<file_name>"]}:')
            print(*[f' * {item} \n' for item in service.get_list_of_names()], end='')
        except:
            print(
    '''The file does not exist or the request was entered incorrectly. Try again!''')

    # Формируем команду get для получения более подробной информации 
    # по конкретной Задаче или Билду

    if args['get']:
        try:
            service = FileService(f'data/{args["<file_name>"]}s.yaml')
            item = service.get_item_by_name(args["<task_or_build_name>"])
            if item:
                what_is_list = next(filter(lambda i: type(item[i]) is list, item), None)
                item[what_is_list] = ', '.join(item[what_is_list])
                print(f'{args["<file_name>"].title()} info:')
                print(*[f' * {i}: {item[i]}\n' for i in item], end='')
            else:
                print(
    '''Task or Build does not exist or the Name was entered incorrectly. Try again!''')
        except:
            print(
    '''Item does not exist or the request was entered incorrectly. Try again!''')


if __name__ == '__main__':
    main()