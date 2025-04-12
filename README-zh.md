本项目旨在为基于 llama-gemma3-cli.exe 的本地多模态模型推理提供一个 OpenAI API 兼容接口，支持通过 Open WebUI 与 Gemma 3 系列模型（如 Gemma 3 27B）交互。

与传统的 CUDA/NVIDIA 显卡不同，本项目特别优化用于 Intel 显卡推理加速，支持以下系列：

Intel Arc A 系列（如 A770、A750）

Intel Arc B 系列

Intel Core Ultra 系列内置 GPU（如 140V、155H 等）

通过本接口，您可以轻松将 llama-gemma3-cli.exe 封装为 RESTful 服务，实现：

Open WebUI 图形界面调用

多轮对话（含 system prompt 记忆）

多模态支持（图片 + 文本）

自动日志记录

本地部署，无需联网

本项目依赖经过 Intel IPEX-LLM 加速兼容的 Gemma 3 模型文件（.gguf 格式）与多模态投影模型 mmproj-model-f16.gguf。

您可以通过以下方式获取模型：

✅ 模型准备步骤：
下载主模型（推荐量化版本）：

gemma-3-27b-it-Q4_K_M.gguf

建议使用 Q4_K_M 或 Q5_K_M 量化版本，适合内存有限的系统

下载多模态投影文件（如使用图像输入）：

mmproj-model-f16.gguf (Gemma3专用)

将文件放入模型目录，例如：

makefile
Copy
Edit
F:\Models\
├── gemma-3-27b-it-Q4_K_M.gguf
└── mmproj-model-f16.gguf
