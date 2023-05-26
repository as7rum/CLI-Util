from docopt  import docopt
from progress.bar import ShadyBar

from file_service import FileService

def main():
    # Регистрируем доступные команды для командной строки
    usage = '''
Builds and Tasks CLI.

Usage:
    app.py test
    app.py list <file_name>
    app.py get <task_or_build> <task_or_build_name>
'''
    # Передаем регистрацию в docopt для отлавливания запросов в командной строке
    args = docopt(usage)

    # Формируем команду test для проверки работоспособности утилиты
    if args['test']:
        pass


    # Формируем команду list для вывода списка Задач или Билдов
    if args['list']:
        try:
            service = FileService()
            print(f'List of available {args["<file_name>"]}:')
            print(*[f' * {item} \n' for item in service.get_list_of_names(
                f'data/{args["<file_name>"]}.yaml')], end='')
        except:
            print(
    '''The file does not exist or the request was entered incorrectly. Try again!''')

    # Формируем команды get для получения более подробной информации 
    # по конкретной Задаче или Билду

    if args['get']:
        service = FileService()
        item = None
        if args['<task_or_build>'] == 'task':
            try:
                item = service.get_task_dependencies(args["<task_or_build_name>"])
            except:
                print(
        '''Task does not exist or the request was entered incorrectly. Try again!''')
        if args['<task_or_build>'] == 'build':
            try:
                item = service.get_builds_with_tasks_and_their_dep(args["<task_or_build_name>"])
            except:
                print(
        '''Build does not exist or the request was entered incorrectly. Try again!''')
        if item:
            item_name = item['name']
            what_is_list = next(filter(lambda i: type(item[i]) is list, item), None)
            print(f'{args["<task_or_build>"].title()} info:')
            print(f'* name: {item_name}')
            print(f'* {what_is_list}:')
            for i in item[what_is_list]:
                print_task(i)
        else:
            print(
    '''Request was entered incorrectly.''')

# Рекурсивный принт для красивого вывода
def print_task(task: dict, level=0):
    indent = "|" + "   " * level
    task_name = task['name']
    what_is_list = next(filter(lambda t: type(task[t]) is list, task), None)
    print(f'{indent}* {task_name}')
    for dependency in task[what_is_list]:
        print_task(dependency, level + 1)

if __name__ == '__main__':
    main()