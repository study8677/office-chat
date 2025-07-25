# Office Chat

Office-Chat 致力于把生成式 AI 深度嵌入 Office 三大核心场景 —— 演示、表格、文档 —— 让用户通过对话即刻完成内容构思、编辑排版、智能分析与协同分享，显著降低学习门槛、提升创作与决策效率。

本仓库提供一个使用 [Google Gemini](https://ai.google.dev/) 的简易聊天 API 实现。
除了普通对话外，还演示如何根据提示生成简单的 Word/Excel/PowerPoint 文档。

## 快速开始

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 在项目根目录创建 `.env` 文件，并写入你的 Gemini API Key：
   ```bash
   echo "GOOGLE_API_KEY=你的Key" > .env
   ```
3. 运行服务：
   ```bash
   python app.py
   ```
4. 发送 POST 请求到 `http://localhost:8000/chat`，请求体格式如下：
   ```json
   { "message": "你的问题" }
   ```
   你可以使用 `curl` 调用：
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"message":"你好"}' http://localhost:8000/chat
   ```
   服务会返回 Gemini 生成的回复。

5. 通过 `/document` 接口生成 Office 文件：
   ```json
   { "kind": "word|excel|ppt", "prompt": "你想生成的内容说明" }
   ```
   例如生成 Word 文档：
   ```bash
   curl -X POST -H "Content-Type: application/json" \
        -d '{"kind":"word","prompt":"写一段关于 AI 的介绍"}' \
        http://localhost:8000/document
   ```
   执行后会在当前目录生成 `output.docx` 等文件。

