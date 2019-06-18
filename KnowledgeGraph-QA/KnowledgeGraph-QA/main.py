# -*- coding: utf-8 -*-
from service.retrieval_service import RetrievalBot
from service.template_service import TemplateBot

if __name__ == '__main__':
    template_bot = TemplateBot()
    retrieval_bot = RetrievalBot()
    while 1:
        query = raw_input('Please enter a question：')
        answer = template_bot.reply(query)
        if not answer:
            answer = retrieval_bot.reply(query)
        print answer
