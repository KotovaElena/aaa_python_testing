## issue-04
Тестирование функции `fit_transform` из one_hot_encoder.py с использованием `pytest`.

Файл one_hot_encoder.py содержит функцию, кодирующую значение в бинарное представление на основе порядкового номера первого встречаемго элемента.     
Файл test_one_hot_encoder_pytest.py содержит тесты.    
Файл result4.txt содержит команды и результаты запуска тестов.    

Установка пакета с помощью pip:  
`pip install -U pytest`

Для запуска тестов в терминале выполнить команду:  
`python -m pytest -v test_one_hot_encoder_pytest.py` 

Для запуска отдельных тестов в терминале выполнить команду, где `test_name` название теста:  
`python -m pytest -v test_one_hot_encoder_pytest.py::test_name`

Для сохранения результатов тестов в файл в терминале выполнить команду:  
`python -m pytest -v test_one_hot_encoder_pytest.py > result4.txt`
