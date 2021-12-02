import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

class Translation(object):
    START_TEXT = f"""<b>Əsənliklər, Sayğılar,</b>
    
Mən bir <b>Mega Link İndirici</b> botuyam!

Sadəcə mega.nz bağlantınısını Göndərin, dosya/video şəkilndə Telegram'a Yükləyəcəm !

Daha çox bilgilər üçün /help düyməsini basın!

✨ @Dto_Bots """
    
    DOWNLOAD_START = "<b>indi sunucuma indirirəm📥</b> \n\n<code>Zəhmət olmasa gözləyin yükləmə ən qısa zamanda başlayacaq😇...</code>"
    UPLOAD_START = "İndi Telegram'a yüklənir 📤..."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS =  "<b>{}</b> saniyəyə İndirildi.\n\n<b>{}</b> saniyəyə yükləndi.\n\n "
    SAVED_CUSTOM_THUMB_NAIL = "Özəl kiçik rəsim Qeyd edildi. 📁.\n\n Əgər silmək istəyirsinizsə, istədiyiniz zaman\n /deletethumbnail göndərin!"
    DEL_ETED_CUSTOM_THUMB_NAIL = "Kiçik rəsim uğurla silindi "

    HELP_USER = f"""<b><u>🍁Salamlar Mən Mega Link İndirici Botuyam.. 🍁</u></b>
 
<u>Mən Nəcür İşləyirəm:-</u>

<b>Mənə bir mega.nz dosya bağlantısı göndersəniz yetərlidir !</b>

<b>⚠️Önəmli:-</b> 

- Klasör bağlantıları dəstəklənmir.

🆑 @DTO_Bots
"""
