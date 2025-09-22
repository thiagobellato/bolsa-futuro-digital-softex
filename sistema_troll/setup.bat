@echo off
echo Iniciando a brincadeira em 2 minutos...
echo Nao feche esta janela.

REM O comando "timeout" espera por 10 segundos (para testes)
timeout /t 10

echo Tempo de espera concluido! Executando o script Python...
REM O caminho deve incluir o nome do arquivo com a extensao .py
python "C:\Users\Aluno.LABINFO25\Desktop\troll.py"

echo Script executado!
pause