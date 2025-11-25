# Comandos Django

django-admin startproject bfdflix .
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser
python manage.py makemigrations
python -m django startapp "filme"

Comandos Git Terminal

git config user.name "Thiago" 
git config user.email "tfbellato@hotmail.com"
git config --unset user.name "Thiago"
git config --unset user.email "tfbellato@hotmail.com"

git config list
git clone
git status 
git add. /*Prepara os arquivos para o commit*/
git commit -m "NOME-DO-COMMIT-AQUI"
git push /*Envia o arquivo para o repositório*/
git pull /*Puxa o arquivo do repositório*/

git branch /*Mostra as branches*/
git branch nome-da-branch /*Cria uma branch*/
git checkout nome-da-branch /*Troca de branch*/
git checkout -b nome-da-branch /*Cria e troca de branch*/
git merge nome-da-branch /*Mescla a branch com a principal*/
git branch -d nome-da-branch /*Deleta a branch*/
