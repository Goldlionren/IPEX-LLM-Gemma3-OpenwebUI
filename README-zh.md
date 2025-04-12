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
