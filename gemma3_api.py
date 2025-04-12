from flask import Flask, request, jsonify
import subprocess
import threading
import base64
import os

app = Flask(__name__)

# 路径配置
LLAMA_EXECUTABLE = r"F:\llama-cpp-ipex-llm-2.2.0-win\llama-gemma3-cli.exe"
MODEL_PATH = r"F:\Models\gemma-3-27b-it-Q4_K_M.gguf"
MMPROJ_PATH = r"F:\Models\mmproj-model-f16.gguf"
IMAGE_PATH = r"F:\input\641.png"
MODEL_NAME = "gemma3-27b-it"

# 锁用于防止并发访问
lock = threading.Lock()

@app.route('/v1/completions', methods=['POST'])
def completions():
    data = request.get_json()
    prompt = data.get('prompt', '')
    return completions_internal(prompt)

@app.route('/v1/models', methods=['GET'])
def list_models():
    return jsonify({
        "data": [
            {"id": MODEL_NAME, "object": "model"}
        ],
        "object": "list"
    })

@app.route('/models', methods=['GET'])
def compatibility_models():
    return jsonify([{"id": MODEL_NAME, "object": "model"}])


@app.route('/v1/chat/completions', methods=['POST'])
def chat_completions():
    data = request.get_json()
    messages = data.get('messages', [])

    system_prompt = ''
    prompt = ''
    image_base64 = None

    for msg in messages:
        role = msg.get("role")
        content = msg.get("content", "")

        # --- System Prompt ---
        if role == "system":
            if isinstance(content, str):
                system_prompt = content.strip()
            continue

        # --- Assistant / User 对话历史拼接 ---
        role_tag = "用户" if role == "user" else "助手"
        
        if isinstance(content, str):
            prompt += f"{role_tag}：{content.strip()}\n"
        elif isinstance(content, list):  # 多模态（图文）
            for part in content:
                if part.get("type") == "text":
                    prompt += f"{role_tag}：{part.get('text', '').strip()}\n"
                elif part.get("type") == "image_url":
                    url = part.get("image_url", {}).get("url", "")
                    if url.startswith("data:image"):
                        image_base64 = url.split(",")[1]
    
    final_prompt = system_prompt + "\n\n" + prompt if system_prompt else prompt

    # ✅ 调试输出 prompt 到控制台
    print("="*30)
    print("[完整 Prompt 传入模型]")
    print("="*30)
    print(final_prompt)
    print("="*30 + "\n")



    return completions_internal(final_prompt, image_base64=image_base64)




def completions_internal(prompt, image_base64=None):
    img_path = IMAGE_PATH  # 默认图片路径（F:\input\641.png）

    # 如果 Open WebUI 传入了 base64 图像
    if image_base64:
        img_path = "F:\\input\\webui_uploaded.png"
        try:
            with open(img_path, "wb") as f:
                f.write(base64.b64decode(image_base64))
        except Exception as e:
            print(f"[图片保存失败]: {e}")
            # 回退使用默认图片
            img_path = IMAGE_PATH

    cmd = [
        LLAMA_EXECUTABLE,
        "-m", MODEL_PATH,
        "--mmproj", MMPROJ_PATH,
        "-t", "8",
        "-ngl", "99",
        "--prompt", prompt,
        "--image", img_path  # ✅ 始终传入 --image 参数
    ]

    with lock:
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
            
                
            print("="*50)
            print("[模型原始输出]")
            print("="*50)
            print(result.stdout)
            print("="*50 + "\n")

            # 跳过前24行
            lines = result.stdout.strip().splitlines()
            filtered_output = "\n".join(lines[24:]) if len(lines) > 24 else ""

            return jsonify({
                "id": "chat-gemma3",
                "object": "chat.completion",
                "created": 1234567890,
                "model": MODEL_NAME,
                "choices": [
                    {"index": 0, "message": {"role": "assistant", "content": filtered_output}, "finish_reason": "stop"}
                ]
            })
        except subprocess.TimeoutExpired:
            return jsonify({'error': 'timeout'}), 504
        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=51093, debug=True)

