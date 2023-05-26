import yaml

class FileService:
    """
    Класс для обработки файла .yaml с задачами и 
    билдами, получения их списка имен, а также для
    получения более детальной информации по каждому из них.
    """

    def init(self, file: str) -> None:
        self.file = file
    
    def get_list_of_names(self, file) -> list:
        """
        Получаем список для просмотра имен 
        загруженных билдов и задач соответственно.
        """
        list_with_tasks_or_builds = self.__get_list_of_items_from_yaml_file(file)
        return list(map(lambda x: x.get('name'), list_with_tasks_or_builds))
    
    def get_builds_with_tasks_and_their_dep(self, build_name: str) -> dict:
        """
        Команда get для получения детальной информации
        в формате словаря о каком-то билде с учетом зависимостей.
        """
        builds_data = self.__get_list_of_items_from_yaml_file('data/builds.yaml')
        build_dict = next(filter(lambda i: i.get('name') == build_name, builds_data), None)
        build_tasks_list = next(build['tasks'] for build in builds_data if build['name'] == build_name)
        # Рекурсивный поиск зависимостей
        build_dict['tasks'] = list(map(lambda task_name: self.get_task_dependencies(task_name), build_tasks_list))
        return build_dict
        
    def get_task_dependencies(self, task_name) -> dict:
        """
        Команда get для получения детальной информации
        в формате словаря о задаче с учетом зависимостей.
        """
        task = next(filter(lambda t: t['name'] == task_name, 
                           self.__get_list_of_items_from_yaml_file('data/tasks.yaml')), None)
        dependencies = task.get('dependencies', [])
        return {
        'name': task['name'],
        'dependencies': list(map(lambda dep: self.get_task_dependencies(dep), dependencies))
    }
    

    def __get_list_of_items_from_yaml_file(self, file) -> list:
        """
        Открываем файл .yaml и преобразуем его в список словарей
        """
        with open(file) as f:
            return list(yaml.safe_load(f).values())[0]