# DEMC Homework

Foobar is a Python library for dealing with word pluralization.

## Kurulum

### 1) Python ve Araclarin Kurulumu

Kurulum icin [pip](https://pip.pypa.io/en/stable/) paket yukleyicisini kurun.

Proje icin virtual environment siddetle onerilir:

```bash
python3 -m venv venv
```

Asagidaki kod kurulum icin ihtiyaciniz olan kutuphanelerin kurulumunu yapacaktir.

```bash
pip install -r requirements.txt
```

```bash
brew install --cask mysql-connector-python
```

### 1) MySQL Kurulumu

Mac cihazlar icin en kolay MySQL kurulumu brew uzerinden yapilmaktadir.

1. MySQL Kurulumu ve servisin baslatilmasi:

```bash
brew install mysql
brew services start mysql
mysql_secure_installation
```

### 3) Docker Kurulumu

```python
foobar.singularize('phenomena') # returns 'phenomenon'
```

### 4) Heroku Deployment

```python
import foobar

```

## Kullanim

### 1) Verilerin Indirilmesi ve Dosya Hazirliklari

IMDb Datasetleri [linkten](https://datasets.imdbws.com/) indirilebilir.

1. Indirilen dosyalari extract etmek icin:

```bash
python3 -m datasets/unzip_files.py
```

### 2) Tablolarin Olusturulmasi ve Verilerin Aktarimi

1. MySQL Arayuzune giris:

```bash
mysql -u root -p
```

2. Database'i yaratin ve tablolari olusturun:

```bash
source /Users/mertcobanoglu/Repos/demc-homework/database/initialize_tables.sql
```

3. Verileri tablolara import edin

```bash
source /Users/mertcobanoglu/Repos/demc-homework/database/import_data.sql
```

### 3) Webapp Flask ve Heroku

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
