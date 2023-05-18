import yaml
from yaml.loader import SafeLoader
from pprint import pprint


with open('builds.yaml') as f:
    data = yaml.safe_load(f)

items_list = (list(data.values())[0])

val = 'audience_stand'

# names = list(map(lambda x: x.get('name'), items_list))
get_task_or_build = next(filter(lambda i: i.get('name') == val, items_list), None)


# d = next(filter(lambda d: d.get(key) == val, dicts), None)
# print(d)        # {'lang': 'Python', 'version': '3.8'}


print(get_task_or_build)


