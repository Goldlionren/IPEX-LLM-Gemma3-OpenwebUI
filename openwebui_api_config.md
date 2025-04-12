
## ⚙️ Open WebUI 配置说明 · How to Connect Open WebUI

如果您希望通过 Open WebUI 与本项目部署的本地 API 通信，请参考以下配置方法：

### 🧠 中文配置指南

在 Open WebUI 设置界面：

1. 添加新的自定义模型连接
2. 类型选择 **OpenAI Compatible API**
3. 在 `API Base URL` 中填写以下地址（根据部署方式选择）：

- 如果 Open WebUI 是通过 Docker 容器运行，并且与本项目部署在 **同一台物理主机** 上：

  ```
  http://host.docker.internal:[端口]/v1
  ```

  例如：

  ```
  http://host.docker.internal:51093/v1
  ```

- 如果 Open WebUI 与 API 不在同一主机，请填写 API 所在主机的局域网 IP 地址，例如：

  ```
  http://192.168.1.100:51093/v1
  ```

4. API Key 留空或填写任意值即可（不做校验）

5. 测试模型连接，保存设置，即可开始使用。

---

### 🧠 English Configuration Guide

To connect this local API with Open WebUI:

1. Go to Open WebUI Settings
2. Add a new model with **OpenAI Compatible API**
3. Set `API Base URL` depending on your setup:

- If Open WebUI runs in Docker **on the same host**:

  ```
  http://host.docker.internal:[PORT]/v1
  ```

  Example:

  ```
  http://host.docker.internal:51093/v1
  ```

- If running on a different machine:

  ```
  http://[IP-of-LLM-Host]:[PORT]/v1
  ```

4. Leave API Key empty or put anything (authentication not required)
5. Save and start chatting!
