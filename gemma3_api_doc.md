
# 📄 gemma3_api.py 文件结构说明

本文件为基于 Flask 构建的本地推理服务，封装了 Intel IPEX LLM 提供的 `llama-gemma3-cli.exe`，实现 OpenAI API 兼容接口，支持文本、多模态对话，并可对接 Open WebUI 使用。

---

## 📌 核心功能

- 支持多轮对话（记忆历史 user/assistant 消息）
- 支持 System Prompt 前置引导
- 支持图文输入（自动识别 base64 图片）
- 自动调用本地命令行模型进行推理
- 自动跳过模型输出前 24 行日志冗余
- 支持 Open WebUI / Postman / 自定义前端接入

---

## 🔁 文件结构逻辑说明

| 部分 | 说明 |
|------|------|
| **模块导入** | Flask 接口 + 子进程 + 多线程锁 + base64 图像处理 |
| **路径配置** | 可执行文件、模型文件、默认图像路径、模型名 |
| **线程锁** | 保证同一时间只有一个命令在执行 |
| **接口 `/v1/models`** | 返回模型 ID，用于 WebUI 模型列表 |
| **接口 `/models`** | 向后兼容旧格式模型查询 |
| **接口 `/v1/completions`** | 普通 prompt 补全（OpenAI v1 文本补全风格） |
| **接口 `/v1/chat/completions`** | ChatGPT 风格接口，拼接完整多轮对话 + system prompt |
| **核心函数 `completions_internal()`** | 负责构建命令行、传入图像、执行模型、过滤返回、输出 JSON |
| **调试输出** | 控制台打印完整拼接 prompt 和模型原始输出 |

---

## ⚠️ 默认图像文件说明

### ❗ 本项目运行依赖 `--image` 参数，即使不使用图像也必须指定。

如果您未上传图像，系统将使用如下默认图片：

```
F:\input\641.png
```

> 若该图片缺失，CLI 执行命令将报错并终止。

### ✅ 建议：

- 永久保留该文件，大小无要求
- 可自定义替换图片路径，但必须存在

---

## ✅ 示例兼容前端

- Open WebUI
- Postman / curl
- FastAPI / Vue / 自定义界面

---

## 📂 推荐目录结构

```
.
├── gemma3_api.py
├── Gemma3_API.bat
├── README.md
├── gemma3_api_doc.md  👈 当前文件
├── .gitignore
├── F:\Models\*.gguf
└── F:\input\641.png
```
