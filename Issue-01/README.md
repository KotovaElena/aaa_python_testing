## issue-01
Тестирование функции `encode` из morse.py с использованием `doctest`.

Файл morse.py содержит переводчик Морзе.   
Файл test_morse_encode.py содержит функцию `encode` из morse.py и доктесты.    
Файл result1.txt содержит команды и результаты запуска теста.    

Для запуска тестов в терминале выполнить команду:  
`python -m doctest -o NORMALIZE_WHITESPACE -v test_morse_encode.py`

Для сохранения результатов тестов в файл в терминале выполнить команду:  
`python -m doctest -o NORMALIZE_WHITESPACE -v test_morse_encode.py > result1.txt`