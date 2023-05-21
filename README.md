# Билд-система

Для разработки игр требуется билд-система, которая автоматизирует и ускоряет рутинные процессы.
Система оперирует понятиями “задача” и “билд”.

**Задача** – это то, что нужно сделать.
Например:
- собрать ресурсы игры, 
- скомпилировать .exe, 
- запаковать игру,
и так далее.

**Задача** описывается уникальным именем (`name`) и ее зависимостями (`dependencies`) от других задач. Задача не может быть выполнена раньше, чем ее зависимости. 
Описания задач задаются в .yaml-файле `data/tasks.yaml`.

**Билд** – это группа задач, объединенных функционально.
Например:
- "Собрать игру" с задачами: "собрать ресурсы игры", "скомпилировать .exe", "запаковать игру".
- "Запустить тесты" с задачами: "собрать ресурсы игры", "скомпилировать .exe";
и так далее.

**Билд** описывается уникальным именем (`name`) и списком задач (`tasks`).
Описания билдов задаются в yaml-файле `data/builds.yaml`.


## Использование

- Утилита была написана с помощью **Python** Для обработки аргументов в командной строке была использована — [docopt](http://docopt.org/)

- Программа загружает `tasks.yaml` и `builds.yaml` файлы из папки **data**, которые содержат задачи и билды соответственно, и дальше оперирует ими.

- Программа поддерживает:

1. Команду `test` для тестирования корректности работы программы.
[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=~+app.py+test)](https://git.io/typing-svg)


2. Команду `list` с аргументами `builds` и `tasks` для просмотра имен загруженных билдов и задач соответственно.

**Примеры:**

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=~+app.py+list+builds)](https://git.io/typing-svg)
```
app.py list builds
List of available builds:
 * test_game
 * pack_game
```
[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=~+app.py+list+tasks)](https://git.io/typing-svg)
```
app.py list tasks
List of available tasks:
 * compile_exe
 * compile_shaders
 * pack_build
```
3. Команду get с аргументами `build` <build_name> и `task` <task_name> для получения детальной информации.

**Примеры:**

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=~+app.py+get+task+pack_build)](https://git.io/typing-svg)
```
app.py get task pack_build
Task info:
 * name: pack_build
 * dependencies: compile_exe, compile_shaders
```
[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=~+app.py+get+build+pack_game)](https://git.io/typing-svg)
```
app.py get build pack_game
Build info:
 * name: pack_game
 * tasks: compile_exe, compile_shaders, pack_build
```
При выводе задач билда учитываются зависимости задач (т.е. сначала выводится зависимости, а затем — зависящие от них задачи).
