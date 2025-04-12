from telegram.ext import Application, ChatJoinRequestHandler
import logging

# تفعيل التسجيل لتتبع الأخطاء
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# رمز التوكن الخاص بالبوت
TOKEN = "7604753743:AAHq-EZtQ5qKrkX_Odg4mnIgRqFFdJPomhY"  # استبدله بتوكن البوت

# معرف المشرف لتلقي الإشعارات
ADMIN_ID = 7037898496  # استبدله بمعرف المشرف، مثال: 123456789

async def accept_join_request(update, context):
    """الدالة التي تقبل طلبات الانضمام تلقائيًا"""
    try:
        join_request = update.chat_join_request
        chat_id = join_request.chat.id
        user_id = join_request.from_user.id
        user_username = join_request.from_user.username or "لا يوجد اسم مستخدم"

        # قبول طلب الانضمام
        await context.bot.approve_chat_join_request(chat_id, user_id)
        logger.info(f"تم قبول طلب انضمام المستخدم {user_id} إلى القناة {chat_id}")

        # جلب معلومات القناة
        try:
            chat = await context.bot.get_chat(chat_id)
            channel_username = chat.username or "لا يوجد اسم مستخدم للقناة"
            channel_title = chat.title or "لا يوجد عنوان للقناة"
            channel_id = chat.id  # معرف القناة

            # جلب معلومات المشرفين لتحديد صاحب القناة
            admins = await context.bot.get_chat_administrators(chat_id)
            owner_username = "غير معروف"
            owner_id = "غير معروف"
            for admin in admins:
                if admin.status == "creator":
                    owner_username = admin.user.username or "لا يوجد اسم مستخدم"
                    owner_id = admin.user.id  # معرف صاحب القناة
                    break

            # إرسال معلومات إلى المشرف
            message = (
                f"تم قبول طلب انضمام:\n"
                f"المستخدم: {user_username} (ID: {user_id})\n"
                f"القناة: {channel_title} ({channel_username}, ID: {channel_id})\n"
                f"صاحب القناة: {owner_username} (ID: {owner_id})"
            )
            await context.bot.send_message(chat_id=ADMIN_ID, text=message)
            logger.info(f"تم إرسال إشعار إلى المشرف {ADMIN_ID}")

        except Exception as e:
            logger.error(f"خطأ أثناء جلب معلومات القناة أو إرسال الإشعار: {e}")
            await context.bot.send_message(
                chat_id=ADMIN_ID,
                text=f"خطأ أثناء جلب معلومات القناة {chat_id}: {e}"
            )

    except Exception as e:
        logger.error(f"خطأ أثناء قبول طلب الانضمام للمستخدم {user_id}: {e}")
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"خطأ أثناء قبول طلب انضمام المستخدم {user_id}: {e}"
        )

def main():
    """تشغيل البوت"""
    # إنشاء التطبيق
    application = Application.builder().token(TOKEN).build()

    # إضافة معالج لطلبات الانضمام
    application.add_handler(ChatJoinRequestHandler(accept_join_request))

    # بدء البوت
    logger.info("البوت يعمل...")
    application.run_polling(allowed_updates=["chat_join_request"])

if __name__ == '__main__':
    main()
