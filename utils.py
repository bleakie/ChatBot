"""
#!/usr/bin/python3
-*- coding: utf-8 -*-
@Time    : 2023/2/23
@Author  : bleakie
@Email   : yangsai1991@163.com

"""
import numpy as np
import openai
import pandas as pd
import time
import joblib
import argparse
from loguru import logger
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import backoff


class CHATBOT:
    def __init__(self, ):
        openai.api_key = config.api_key
        self.embedding_db = self.create_vector_store(config.knowledge_db)
        self.max_token = config.max_token
        self.top_k = config.top_k
        self.similarit = config.similarit
        self.top_p = config.top_p
        self.single_turn = config.single_turn
        self.memory_k = config.memory_k
        self.temperature = config.temperature
        self.presence_penalty = config.presence_penalty
        self.frequency_penalty = config.frequency_penalty
        self.completions_model = config.completions_model
        self.embedding_model = SentenceTransformer(config.embedding_model)
        self.create_prefix = config.create_prefix
        self.historys = []

    def create_vector_store(self, excel_path):
        knowledge_base_df = pd.read_excel(excel_path)
        embeddings, contexts = [], []
        for text in knowledge_base_df.values:
            merge = '问题：%s\n答案：%s' % (text[0], text[1])
            contexts.append(merge)
            embeddings.append(self.text2embedding(merge))
        embedding_db = {'embeddings': np.array(embeddings), 'contexts': contexts}
        return embedding_db

    @backoff.on_exception(backoff.expo, openai.error.RateLimitError)
    def get_embedding(self, text):
        embeddings = self.embedding_model.encode(text)  # openai_embedding
        return embeddings

    @backoff.on_exception(backoff.expo, openai.error.RateLimitError)
    def get_chat_answer(self, messages={}, stream=True):
        return openai.ChatCompletion.create(
            model=self.completions_model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_token,
            top_p=self.top_p,
            presence_penalty=self.presence_penalty,
            frequency_penalty=self.frequency_penalty,
            stream=stream
        )  # ["choices"][0]["message"]

    def caculate_similarity(self, query):
        query_embedding = self.text2embedding(query).reshape(1, -1)
        content_sims = cosine_similarity(query_embedding, self.embedding_db['embeddings'])[0]
        return content_sims

    def get_top_context(self, user_input):
        content_sims = self.caculate_similarity(user_input)
        content_rank = np.argsort(-content_sims)[:self.top_k].tolist()
        top_content, count = '', 0
        for tmp, index in enumerate(content_rank):
            if content_sims[index] > self.similarit:
                count += 1
                top_content += "%s\n" % (self.embedding_db['contexts'][index])
                if tmp != len(content_rank): top_content += "\n"

        if count < 1: top_content = '空'
        return top_content

    def output_content(self, user_input):
        top_context = self.get_top_context(user_input)
        query_prompt = config.create_prefix.replace("{sources}", top_context).replace("{question}", user_input)
        if self.single_turn:
            massage = []
            for tmp in self.historys:
                massage.append(tmp)
            massage.append(query_prompt)
        else:
            massage = [{"role": "user", "content": query_prompt}]
        result_content = self.get_chat_answer(massage)["choices"][0]["message"]["content"]
        self.historys.append({"role": "user", "content": user_input})
        self.historys.append({"role": "assistant", "content": result_content})
        self.historys = self.historys[-self.memory_k:] if len(self.historys) >= self.memory_k else self.historys
        return result_content
