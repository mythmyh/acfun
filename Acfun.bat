@echo off
echo 当前盘符：%~d0
echo 当前盘符和路径：%~dp0
echo 当前批处理全路径：%~f0
set "strc=pythonfromroot"
set "stra=%~sdp0%strc%"
echo "%stra%"
cd "%stra%"
python ontime.py
cd %~sdp0
pause