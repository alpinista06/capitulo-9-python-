# capitulo-9-python-

Este projeto se trata de um software na linguagem python , versão python 2.7, que encontra lacunas entre um determinado padrão de nomes de arquivos em uma pasta.
Como pré-requisito leia o capitulo 9 do livro intitulado acima. Neste caso o padrão a ser encontrado é “spam000.txt” sendo que no trecho ‘000’ podem haver qualquer digito numérico, e sempre que o programa encontrar uma lacuna na numeração (ex: spam001.txt, spam003.txt) ele irá renomear todos os outros arquivos de forma e preencher essa lacuna (no ex anterior teríamos spam001.txt, spam002.txt).

Segue o código completo do software, neste documento ele será explanado linha or linha e serão explicadas todas as técnicas usadas nele.

1. #!/usr/bin/python
2. #--coding:utf8--
3. 
4. import os, re, shutil
5. 
6. def Preenchendo(prefixo, extensao, caminho=""):
7.     if caminho == "":
8.         caminho = os.getcwd()
9.     os.chdir(caminho)
10. 
11.     a = 1
12.     l = 3
13.     regex = re.compile(r'^%s(\d+)' % prefixo)
14.     numList = []
15.     lista = os.listdir(caminho)
16. 
17.     for arquivo in lista:
18.         if arquivo.endswith(extensao):
19.             mo = regex.search(arquivo)
20.             if mo != None:
21.                 c = mo.group(0)
22.                 numList.append(c)
23.                 renomeado = prefixo + str(a).zfill(l) + extensao
24.                 shutil.move(arquivo, renomeado)
25.                 numList.append(renomeado)
26.                 a += 1
27.                 print numList
28. 
29. caminho = ""
30. prefixo = "spam"
31. extensao = ".txt"
32. Preenchendo(prefixo, extensao, caminho)


Nas linhas 1 e 2 temos as configurações de codificações para códigos-fonte em python, para entendê-los melhor basta acessar  https://www.python.org/dev/peps/pep-0263/, explicá-las neste momento fugiria um pouco do foco desde documento. 
Já na linha 4:
 import os, re, shutil 

é feita a importação dos módulos que serão necessário para desempenhar as atividade previstas para atingir o objetivo final. O módulo ’os’ sera necessário para navegar pelos diretórios, já ‘re’ será necessária na criação da regex(expressão regular) para encontrar o padrão de nome proposto pelo projeto e  o módulo ‘shutil’ será necessário para as alterações nos nomes dos arquivos para reorganizá-los para preencher as lacunas.
No trecho:

def Preenchendo(prefixo, extensao, caminho=""):
	 if caminho == "":
     		caminho = os.getcwd()
 	os.chdir(caminho)

O método ‘preenchendo’ que recebe os argumentos ‘prefixo, extensao, caminho="" ‘ testa se o argumento ‘caminho’ está vazio, caso esteja assim ele irá receber através do método ‘os.getcwd()’ o caminho do atual diretório de trabalho(onde está o arquivo do software) e através do método ‘os.chdir(caminho)’ vai escolher este diretório para executar o código. Quando se trabalha com o módulo ‘os’, como é o caso do trecho acima, é necessário entender que o caminho do diretório como um argumento é dado por uma string, Ex: ‘/home/usuário/pasta/’ e é estritamente necessário que o arquivo do software esteja na mesma pasta em que se espera que ele seja executado para realizar as alterações, do contrario ele não terá o resultado como esperado.
Nas linhas 11 e 12 valores são atribuídos a variáveis que serão necessárias mais adiante no código. No trecho da linha 13:

regex = re.compile(r'^%s(\d+)' % prefixo)

é definida a expressão regular(regex) e definido o padrão de nome dos arquivos a serem encontrados. “ r’ “ nos livra de ter de “fugir” dos caracteres especiais como neste caso ‘^’ que indica que o nome deve começar com o valor ‘%s’ da variável “prefixo” e logo após ela deve ter algum digito numérico ‘(\d+) e mais alguma coisa após isso.
Na linha 14 é definida uma lista vazia chamada numList , que será usada mais a frente. Na linha 15 o método ‘os.listdir(caminho)’  salva na variável ‘lista’ todos os arquivos presentes no atual diretório de trabalho, lembre-se bem deste trecho explicado acima, o trecho abaixo é totalmente dependente dos componentes comentados aqui.

No trecho:
    for arquivo in lista:
        if arquivo.endswith(extensao):
            mo = regex.search(arquivo)
            if mo != None:
                c = mo.group(0)
                numList.append(c)
                renomeado = prefixo + str(a).zfill(l) + extensao
                shutil.move(arquivo, renomeado)
                numList.append(renomeado)
                a += 1
                print numList

através do laço for o software caminha por todos os ‘arquivo’ na ‘lista’ que contém todos os arquivos do diretório atual, então ele faz o seguinte teste: se o nome do arquivo terminar com ‘extensão’, ele continua a executar o código, isso se dá através do método ‘.endwith(extensão)’. Caso passe do primeiro condicional, a variável “mo” verifica a correspondência entre o arquivo com o padrão exigido pela regex usando o método ‘regex.search(arquivo)’  e se a verificação for diferente de ‘Nulo’ o software realiza a o próximo bloco do código.
No bloco seguinte a variável ‘c’ recebe o arquivo que foi aprovado em todas as instancias anteriores com todo o seu nome através do método ‘mo.group(0)’ , esse método indica q deve ser atribuída à variável ‘mo’ a string toda da correspondência encontrada. Com o método ‘.append(c)’ a lista criada anteriormente, que estava vazia recebe a correspondência.
Na linha seguinte:

                   renomeado = prefixo + str(a).zfill(l) + extensao

a variável ‘renomeado’ recebe o novo nome do arquivo q é composto por ‘prefixo, numeração e extensão’. No trecho ‘str(a).zfill(l)’ esta método foma uma numeração que contém a string(a) precedida de ‘l’ zeros ( ‘.zfill(l)’). o método ‘z.fill’ pode ser melhor entendido acessando suas documentações em: https://docs.python.org/2/library/string.html , suas considerações se encontram bem no fim da seção.
No trecho:

shutil.move(arquivo, renomeado)

o método ‘shutil.move’ é usado para renomear o arquivo atual, seu nome muda de ‘arquivo’ para ‘renomeado’ , ambos são referencias aos valores contidos em si já que são apenas variáveis, feita a mudança a lista criada anteriormente recebe o arquivo renomeado e então a variável ‘a’ , que é um contador que controla a numeração arquivo atual, recebe um acréscimo e todo o laço é executado novamente, até que não existam mais arquivos a serem varridos.

Para realiza o teste é necessário baixar a pasta pasta-teste que pode ser obtida no github através do link https://github.com/alpinista06/capitulo-9-python nela estão contidos o código do software e os arquivos para teste. Neste caso o resultado esperado deve ser de que os arquivos:
 
spam001.txt
spam003.txt
spam005.txt

na pasta pasta-teste sejam alterados para:

spam001.txt
spam002.txt
spam003.txt

ou seja renomeando todos os arquivos existentes na pasta de forma a preencher a lacuna, como é proposto no livro .
