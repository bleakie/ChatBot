"""
#!/usr/bin/python3
-*- coding: utf-8 -*-
@Time    : 2023/2/23
@Author  : bleakie
@Email   : yangsai1991@163.com

"""
from easydict import EasyDict as edict

config = edict()
config.api_key = 'sk-xxxx'
config.max_token = 512
config.similarit = 0.75
config.top_k = 3
config.single_turn = False
config.memory_k = 4
config.top_p = 1
config.temperature = 0.3
config.presence_penalty = 0.5
config.frequency_penalty = 0.5
config.knowledge_db = './data/data_all.xlsx'
config.embedding_model = 'embedding_model_path'
config.completions_model = 'gpt-3.5-turbo'

config.create_prefix = """你是专属于xxx的AI客服“xx”，所以你需要将我的问题放在xxx背景下思考并做出友好、简洁的回答。
    
    已知信息：
    { {sources} }

    回答要求：
    - 回答要点分重点罗列；
    - 如果我的问题与已知信息有关，你需要提取出来并进行润色；
    - 如果我的问题与已知信息无关，你需要提取聊天记录中与我的问题有关的信息并进行润色；
    - 如果我的问题与聊天记录无关，那么你将只参考已知信息进行回答，不允许添加编造成分。

    我的问题：{question}"""

# {
#   "model": "gpt-3.5-turbo",  // model 类型，
#   "messages": [{"role": "user", "content": "Hello!"}],  // The role of the author of this message. One of system, user, or assistant.
#   "name": "abc007",
#   "max_tokens": 7,  // total length of input tokens and generated tokens limited
#   "temperature": 1,  // default 1, between 0 and 2. 越大越随机
#   "top_p": 1,  // default 1, between 0 and 2. 越大越多样
#   "n": 1,  // 产生几个候选回答
#   "presence_penalty": 0,  // 主题的重复度 default 0, between -2 and 2. 控制围绕主题程度，越大越可能谈论新主题。
#   "frequency_penalty": 0,  // 重复度惩罚因子 default 0, between -2 and 2. 减少重复生成的字。
#   "stream": false,
#   "logprobs": null,  // Modify the likelihood of specified tokens appearing in the completion.
#   "stop": "\n"  // 结束字符标记
# }
