import yaml

class CLIUtil:
    """
    Класс для обработки файла .yaml с задачами и 
    билдами, получения их списка имен, а также для
    получения более детальной информации по каждому из них.
    """

    def __init__(self, file) -> None:
        self.file = file
    
    def get_list_of_names(self) -> list:
        """
        Получаем список для просмотра имен 
        загруженных билдов и задач соответственно.
        """
        list_with_tasks_or_builds = self.__get_list_of_items_from_yaml_file(self.file)
        return list(map(lambda x: x.get('name'), list_with_tasks_or_builds))
    
    def get_item_by_name(self, value) -> dict:
        """
        Команда get для получения детальной информации
        в формате словаря о какой-то конкретной задаче
        или билде.
        """
        list_with_tasks_or_builds = self.__get_list_of_items_from_yaml_file(self.file)
        return next(filter(lambda i: i.get('name') == value, list_with_tasks_or_builds), None)

    def __get_list_of_items_from_yaml_file(self) -> list:
        """
        Открываем нужный файл и получаем список словарей
        """
        with open(self.file) as f:
            return list(yaml.safe_load(f).values())[0]