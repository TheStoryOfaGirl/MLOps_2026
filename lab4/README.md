# Отчет по практическому заданию (DVC + Google Drive, датасет Iris)

Удаленное хранилище: Google Drive (настроен через client_id и client_secret)

Версии:
 - v1 - Исходный датасет Iris
 - v2 - Стандартизированные данные (StandardScaler)

Выполненные операции:
```
dvc init

dvc remote add storage gdrive://<ID_ПАПКИ_НА_GOOGLE_DRIVE>
dvc remote modify --local storage gdrive_client_id <client_id>
dvc remote modify --local storage gdrive_client_secret <client_secret>

# Создание версий
dvc add lab4/data
git commit -m "init dvc"
dvc push

dvc add lab4/data
git commit -m "standardize data"
dvc push

# Переключение между версиями
git checkout HEAD~1
dvc checkout

git checkout main
dvc checkout
```

Результаты:
- Git-репозиторий содержит метаинформацию (.dvc-файлы)
- Google Drive хранит обе версии датасета (разные хеши)
- Переключение между версиями работает корректно
