# Infer openai —— 客服助手


## 📢 News

+ 【2024.01.10】 V0.1版本，支持 离线Embedding模型，completions使用gpt


---

**主要特性**：

此项目为开源大模型的推理实现统一的后端接口，与 `OpenAI` 的响应保持一致，具有以下特性：

+ ✨ 以 `OpenAI ChatGPT API` 的方式调用大模型


+ 📖 实现文本嵌入模型，为知识问答提供上下文
 

+ 🙌 只需要简单的修改环境变量即可将开源模型作为 `chatgpt` 的替代模型，为应用提供后端支持



## 🤖 使用方式

### 启动

+ `推理`: python infer_embeding.py

+ `界面`: streamlit run main_webui.py

### 修改配置

+ config.py修改模型、路径、参数等






## 🐼 Todo
+ 接入离线大模型
+ 多线程调用
+ 🦜️ 支持大规模语言模型开发工具 [`langchain` ](https://github.com/hwchase17/langchain) 的各类功能


## 🚧 References

+ [文心一言模型调用](https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Nlks5zkzu)

+ [api-for-open-llm](https://github.com/xusenlinzy/api-for-open-llm)

+ [LangChain: Building applications with LLMs through composability](https://github.com/hwchase17/langchain)
