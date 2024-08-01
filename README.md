# Discord Bot

Bu proje, basit bir Discord botunun Python kullanılarak nasıl oluşturulacağını gösterir. Bu bot, belirli komutlara yanıt verir ve bazı temel işlevleri yerine getirir.

## Özellikler

- Botun başarılı bir şekilde giriş yaptığını gösteren bir mesaj.
- Hataların konsola yazdırılması.
- `/merhaba` komutuyla kullanıcılara yanıt verme.

## Başlangıç

Bu botu kendi makinenizde çalıştırmak için aşağıdaki adımları takip edin.

### Gereksinimler

- Python 3.8 veya daha üzeri
- `discord.py` kütüphanesi

### Kurulum

1. Projeyi klonlayın:
    ```sh
    git clone https://github.com/kullanıcı_adı/my-discord-bot.git
    cd my-discord-bot
    ```

2. Gerekli kütüphaneleri yükleyin:
    ```sh
    pip install discord.py
    ```

3. `bot.run('key')` kısmındaki `'key'` ifadesini kendi Discord botunuzun token'ı ile değiştirin.

### Kullanım

1. Botu çalıştırın:
    ```sh
    python bot.py
    ```

2. Bot giriş yaptığında konsolda şu mesajı göreceksiniz:
    ```sh
    Bot <bot_adı> olarak giriş yaptı!
    ```

3. Discord sunucunuzda `/merhaba` komutunu kullanarak botun yanıt verdiğini test edin:
    ```sh
    /merhaba
    ```
    Bot şu yanıtı verecektir:
    ```sh
    Merhaba!
    ```

## Katkıda Bulunun

Katkıda bulunmak istiyorsanız lütfen bir `issue` açın ya da bir `pull request` gönderin.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.
