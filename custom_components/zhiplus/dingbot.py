
# Logging
import logging
_LOGGER = logging.getLogger(__name__)

#
_hass = None
_conf = None

#
from .zhibot import zhibotQuery
from .chatbot import ChatBotView

#
class dingbotView(ChatBotView):

    def check(self, data):
        return data['chatbotUserId'] == _conf['chatbotUserId']

    async def handle(self, data):
        return await zhibotQuery(_hass, data['text']['content'])

    def response(self, answer):
        return {'msgtype': 'text', 'text': {'content': answer}}
