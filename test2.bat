@echo off
chcp 65001 > nul
echo Start tests
echo === Список комманд для теста ===
type test_script2.sh
echo === Результаты теста ===
python Task1.py < test_script2.sh
echo End of testing
pause
