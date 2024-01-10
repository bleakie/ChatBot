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
from utils import CHATBOT

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="densely extract the video frames and optical flows")
    parser.add_argument('--questions', default='./data/questions.xlsx', type=str)
    args = parser.parse_args()
    logger.add('./log/log.log', encoding='utf-8')
    questions = pd.read_excel(args.questions)
    charbot = CHATBOT()
    for user_input in questions["prompt"]:
        try:
            result = charbot.output_content(user_input)
        except BaseException as e:
            logger.error('Question: %s Error: %s' % (user_input, e))
