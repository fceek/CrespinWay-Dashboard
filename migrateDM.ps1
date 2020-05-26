$appName = $args[0]

python manage.py makemigrations $appName

$newMigrationFile = Get-ChildItem -File ".\$appName\migrations" | Sort-Object LastWriteTime | Select-Object -last 1
$filePrefix = $newMigrationFile.BaseName.Substring(0,4)

python manage.py sqlmigrate $appName $filePrefix
python manage.py migrate