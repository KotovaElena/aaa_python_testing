## issue-03
Тестирование функции `fit_transform` из one_hot_encoder.py с использованием `unittest`.

Файл one_hot_encoder.py содержит функцию, кодирующую значение в бинарное представление на основе порядкового номера первого встречаемго элемента.     
Файл test_one_hot_encoder_unittest.py содержит тесты.    
Файл result3.txt содержит команды и результаты запуска тестов.    

Для запуска тестов в терминале выполнить команду:  
`python -m unittest -v test_one_hot_encoder_unittest.py` 

Для запуска отдельных тестов в терминале выполнить команду, где `test_name` название теста:  
`python -m unittest -v test_one_hot_encoder_unittest.TestFitTransform.test_name`
