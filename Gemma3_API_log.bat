@echo off
title Gemma3_API Server
chcp 65001 >nul

:: 激活 Conda 环境（请根据你的环境名修改）
call conda activate IPEX_ollama

:: 切换到脚本目录
cd /d F:\llama-cpp-ipex-llm-2.2.0-win

:: 启动服务，并将输出同时打印到屏幕和 log.txt
python gemma3_api.py | tee log.txt

pause
