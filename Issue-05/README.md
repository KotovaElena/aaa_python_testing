## issue-05
Тестирование функции `what_is_year_now` из what_is_year_now.py   
с использованием `unittest.mock` для замены реального обращения к API.

Файл what_is_year_now.py содержит функцию, возвращающую текущий год.   
Файл test_what_is_year_now.py содержит тесты.    
Файл result5.txt содержит результаты запуска тестов с покрытием.  

Установка пакетов с помощью pip:  
`pip install -U pytest`  
`pip install -U pytest-cov`   

Для запуска теста в терминале выполнить команду:  
`python -m pytest -v -s test_what_is_year_now.py`

Для запуска теста с замером покрытия в терминале выполнить команды:  
 `python -m pytest test_what_is_year_now.py --cov=what_is_year_now`  

Для сохранения результатов тестов с замером покрытия в файл в терминале выполнить команду:  
`python -m pytest test_what_is_year_now.py --cov=what_is_year_now > result5.txt`

Для получения отчета о покрытии тестами в html:  
`python -m pytest test_what_is_year_now.py --cov=what_is_year_now --cov-report html`

