# Mock Data Services
Request'te gönderilen datalar dosya sistemine kaydedilip daha sonrasında tekrar ulaşılmak istendiğinde request atılarak alına bilen bir sistemdir.
## Api Listesi
- Request atılarak mock data kayıt edilen api service **http://<host>:<port>/api/set-json-type** tır. Gönderilmesi gereken request body aşağıdaki gibidir.
    ```
    Type: GET
    Body: {
        "type": "Deneme1",
        "content": {
            "firstname": "Giray",
            "lastname": "AKKAYA",
            "age": 28
        }
    }
    ```
    Yukarıda **type** mock data key'idir. **Context** ise mock data objesidir.
- Request atılarak mock datayı almak için kullenılan api **http://<host>:<port>/api/get-json-type** dir. Gönderilmesi gereken request body aşağıdaki gibidir.
    ```
    Type: GET
    Body: {
        "type": "Deneme1",
    }
    ```
     Yukarıda **type** mock data key'idir. Keye göre daha önce kaydedilen datayı geri getirir yok ise 400 hatası ile birlikte **msg** objesi geri döner. 


## Kurulum
Docker dosyası ile ayağı kaldırmak için aşağıdaki komut çalıştırılmalıdır.
```bash
docker-compose up -d
```