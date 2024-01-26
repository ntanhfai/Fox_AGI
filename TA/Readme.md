# Đã download weight và chạy thử

## EnViT5 Translation
State-of-the-art English-Vietnamese and Vietnamese-English Translation models trained on MTet, PhoMT.

https://huggingface.co/VietAI/envit5-translation
- Model `VietAI/envit5-translation`, dung lượng 1G
- Download weight : `C:\Users\TA\.cache\huggingface\hub\models--VietAI--envit5-translation\snapshots\840bc88104d5a4277af740eaedb024df8c3093e7`
- file chạy đã test: `H:\AGI-Projects\Transcribe_Translate\VietAI_Translation.py`

## SeamlessM4T
SeamlessM4T is our foundational all-in-one Massively Multilingual and Multimodal Machine Translation model delivering high-quality translation for speech and text in nearly 100 languages.

SeamlessM4T models support:

- 🎤 101 languages for speech input.
- 💬 96 Languages for text input/output.
- 🔈 35 languages for speech output.

This unified model enables multiple tasks without relying on multiple separate models:

- Speech-to-speech translation (S2ST)
- Speech-to-text translation (S2TT)
- Text-to-speech translation (T2ST)
- Text-to-text translation (T2TT)
- Automatic speech recognition (ASR).

### Inference with Translator:
Inference calls for the Translator object instantiated with a multitasking UnitY or UnitY2 model with the options:

- `seamlessM4T_v2_large`
- `seamlessM4T_large`
- `seamlessM4T_medium`

### GPT4All
Link gốc: `https://gpt4all.io/index.html`

Đã test với nối tiếp câu promt thì thấy chạy OK với tiếng Anh, __không support tiếng Việt__ 

GPT4All có cả ứng dụng cài đặt luôn cho Windows, có cho download models trong đó. 
Nó là 1 ứng dụng chat. xuất phát điểm từ: `https://github.com/nomic-ai/gpt4all/tree/main/gpt4all-chat`. Tải về từ đây: `https://gpt4all.io`

#### Code:

Sửa cái này: `from gpt4all.gpt4all import DEFAULT_MODEL_DIRECTORY` thành folder của mình
- `H:\AGI-Projects\GPT4All\main.py`
- `"H:\AGI-Projects\GPT4All\chat-windows-latest-avx2.exe"` file này chạy như ứng dụng chat GPT, chỉ cn cấu hình file weight vào là chạy.
- weight: 
  - `G:\AGI_Projects\GPT4All\gpt4all-6971cdbc-2f6f-4971-b6b0-f4a3544bdf1b.chat`
  - `"G:\AGI_Projects\GPT4All\all-MiniLM-L6-v2-f16.gguf"`
  - `"G:\AGI_Projects\GPT4All\ggml-vicuna-7b-1.1-q4_2.bin"`
  - `"G:\AGI_Projects\GPT4All\orca-mini-3b-gguf2-q4_0.gguf"`
