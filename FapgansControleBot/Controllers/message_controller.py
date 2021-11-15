from telegram import Message, Update
from telegram.ext import Filters, MessageHandler, CallbackContext

from FapgansControleBot.Repository.i_unit_of_work import IUnitOfWork
from config import BotConfig
import logging

logger = logging.getLogger(__name__)


def is_fapgans(message: Message) -> bool:
    if message:
        if message.sticker:
            if message.sticker.file_unique_id == BotConfig.FAPGANS_STICKER_ID:
                return True
    return False


class MessageController:
    def __init__(self, unit_of_work: IUnitOfWork):
        self.unit_of_work = unit_of_work

    def handle_message(self, update: Update, context: CallbackContext):
        if update.message:
            if is_fapgans(update.message):
                user = update.message.from_user
                logger.info("%s (%s) send a Fapgans!", user.username, user.id, update.message.text)
