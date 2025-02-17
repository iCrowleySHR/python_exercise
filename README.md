# python_exercise

## Dependências

- Para instalar o PyInstaller (Para transformar em .exe)
```
pip install pyinstaller
```

- Para transformar o projeto em .exe
```
pyinstaller --onefile script.py
```

- Para colocar icone o .exe
```
pyinstaller --onefile --icon=icone.ico script.py
```

## 1_exercise
Um projeto que recebe dois valores para fazer a soma, subtração, multiplacação e divisão.

### Saída
```
Digite o primeiro valor
50
Digite o segundo valor
30

Soma: 80.0
Subtração: 20.0
Vezes: 1500.0
Divisão: 1.6666666666666667


Pressione Enter para sair...
```

## 2_exercise
Um projeto que recebe o nome, e retorna com cada letras separada e com prefixos.

### Saída
```
Digite um nome
Gustavo

===== Cada Letra Separada =====
G
u
s
t
a
v
o
================================

===== Prefixos em Linhas =====
G
Gu
Gus
Gust
Gusta
Gustav
Gustavo
================================

===== Prefixos na Mesma Linha =====
G Gu Gus Gust Gusta Gustav Gustavo
```