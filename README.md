# IPEX-LLM-Gemma3-OpenwebUI
This project provides an OpenAI-compatible API wrapper for local inference using llama-gemma3-cli.exe, enabling smooth integration with Open WebUI to interact with Gemma 3 models such as Gemma 3 27B.

Unlike traditional inference solutions based on NVIDIA GPUs, this implementation is optimized for Intel GPU acceleration, supporting:

Intel Arc A-Series (e.g., A770, A750)

Intel Arc B-Series

Intel Core Ultra iGPUs (e.g., 140V, 155H)

Key features:

RESTful API interface for llama-gemma3-cli.exe

Fully compatible with Open WebUI

Multi-turn conversation memory and system prompt support

Multimodal input: text + image (base64)

Local deployment, no internet required

Auto-logging to log.txt

This project is designed for those looking to unleash full performance of Intel GPUs for local LLM inference and multimodal interaction.
