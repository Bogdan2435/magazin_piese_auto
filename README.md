
## Cum accesez interfata web pentru interactionarea cu baza de date?
- Creez in anaconda env python cu versiunea 3.8.13 si in mysql o schema noua cu denumirea "magpiese".</br>
- Creez un folder in care descarc tot ce este pe git </br>
- In folderul creat initializez virtual env cu comanda:
```
python -m venv env
```
- Activez virtual env cu comanda:
```
env\scripts\activate
``` 
- Apoi navighez in folderul cu aplicatia Django prin comanda: 
```
cd "mag_piese_auto_baze de date\magpiese"
```
- Instalez pachetele necesare ruland:
```
pip install -r requirements.txt
```
- In ```magpiese\settings.py``` trebuie modificata parola de pe linia 83 ```'PASSWORD': '12345678'``` cu parola de la mysql. </br>
- Apoi rulez urmatoarele comenzi:
```
python manage.py makemigrations
python manage.py migrate
python manage.py cratesuperuser
python manage.py runserver
```
- Acum pot accesa interfata cu succes in orice browser la adresa:  ```http://127.0.0.1:8000/```

