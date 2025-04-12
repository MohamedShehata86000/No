import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ChatJoinRequestHandler, CallbackContext

# إعداد التسجيل لتصحيح الأخطاء
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# معرف المشرف (استبدله بمعرفك)
ADMIN_ID = 7037898496  # مثال: 123456789

# الدالة التي تستجيب للأمر /start
async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    logger.info(f"تم استلام أمر /start من المستخدم {user_id}")
    await update.message.reply_text("مرحبًا! أنا بوت إدارة طلبات الانضمام. أرسل /help لمزيد من المعلومات.")

# الدالة التي تستجيب للأمر /help
async def help_command(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    logger.info(f"تم استلام أمر /help من المستخدم {user_id}")
    await update.message.reply_text(
        "أنا بوت لإدارة طلبات الانضمام إلى القناة.\n"
        "الأوامر المتاحة:\n"
        "/start - بدء البوت\n"
        "/help - عرض المساعدة\n"
        "/status - التحقق من حالة البوت\n"
        "ملاحظة: أقوم بقبول الطلبات الجديدة تلقائيًا."
    )

# الدالة التي تستجيب للأمر /status
async def status(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    logger.info(f"تم استلام أمر /status من المستخدم {user_id}")
    await update.message.reply_text("البوت يعمل ويستقبل طلبات الانضمام الجديدة.")

# الدالة التي تتعامل مع طلبات الانضمام
async def handle_join_request(update: Update, context: CallbackContext) -> None:
    join_request = update.chat_join_request
    user = join_request.from_user
    chat = join_request.chat

    logger.info(f"طلب انضمام من {user.first_name} (ID: {user.id}) إلى القناة {chat.title} (ID: {chat.id})")

    try:
        await context.bot.approve_chat_join_request(
            chat_id=chat.id,
            user_id=user.id
        )
        logger.info(f"تم قبول طلب انضمام {user.first_name} (ID: {user.id}) بنجاح")
        try:
            await context.bot.send_message(
                chat_id=user.id,
                text=f"مرحبًا {user.first_name}! تم قبولك في القناة {chat.title}. استمتع!"
            )
        except Exception as e:
            logger.warning(f"فشل في إرسال رسالة ترحيب إلى {user.id}: {e}")
        try:
            await context.bot.send_message(
                chat_id=ADMIN_ID,
                text=f"تم قبول طلب انضمام من {user.first_name} (ID: {user.id}) في القناة {chat.title}."
            )
        except Exception as e:
            logger.warning(f"فشل في إرسال إشعار للمشرف {ADMIN_ID}: {e}")
    except Exception as e:
        logger.error(f"فشل في قبول طلب الانضمام لـ {user.id}: {e}")
        try:
            await context.bot.send_message(
                chat_id=ADMIN_ID,
                text=f"فشل في قبول طلب انضمام من {user.first_name} (ID: {user.id}): {e}"
            )
        except Exception as e2:
            logger.warning(f"فشل في إرسال إشعار فشل للمشرف {ADMIN_ID}: {e2}")

# الدالة الرئيسية لتشغيل البوت
def main() -> None:
    # استبدل "YOUR_BOT_TOKEN" بالتوكن الخاص بك
    application = Application.builder().token("7604753743:AAHq-EZtQ5qKrkX_Odg4mnIgRqFFdJPomhY").build()

    # إضافة معالجات الأوامر
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("status", status))
    application.add_handler(ChatJoinRequestHandler(handle_join_request))

    # تشغيل البوت بحلقة أحداث يدوية
    logger.info("بدء تشغيل البوت...")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(application.run_polling(allowed_updates=Update.ALL_TYPES))
    finally:
        loop.close()

if __name__ == "__main__":
    main()
