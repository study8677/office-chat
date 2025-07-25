# Office Chat

Office-Chat 致力于把生成式 AI 深度嵌入 Office 三大核心场景 —— 演示、表格、文档 —— 让用户通过对话即刻完成内容构思、编辑排版、智能分析与协同分享，显著降低学习门槛、提升创作与决策效率。

本仓库提供一个使用 [Google Gemini](https://ai.google.dev/) 的简易聊天 API 实现。

## 快速开始

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 设置环境变量 `GOOGLE_API_KEY` 为你的 Gemini API Key。
3. 运行服务：
   ```bash
   python app.py
   ```
4. 发送 POST 请求到 `http://localhost:8000/chat`，请求体格式如下：
   ```json
   { "message": "你的问题" }
   ```
   服务会返回 Gemini 生成的回复。

