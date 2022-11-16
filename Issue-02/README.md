## issue-02
Тестирование функции `decode` из morse.py с использованием `pytest.mark.parametrize`.

Файл morse.py содержит переводчик Морзе.   
Файл test_morse_decode.py содержит функцию `decode` из morse.py и параметрический тест.    
Файл result2.txt содержит команды и результаты запуска теста.    

Установка пакета с помощью pip:  
`pip install -U pytest`  

Для запуска теста в терминале выполнить команду:  
`python -m pytest -v test_morse_decode.py`

Для сохранения результатов тестов в файл в терминале выполнить команду:  
`python -m pytest -v test_morse_decode.py > result2.txt`
