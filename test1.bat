@echo off
chcp 65001 > nul
echo Start tests
echo === Список комманд для теста ===
type test_script1.sh
echo === Результаты теста ===
python Task1.py < test_script1.sh
echo End of Testing
pause
