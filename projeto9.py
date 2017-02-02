#!/usr/bin/python
#--coding:utf8--


import os, re, shutil

def Preenchendo(prefixo, extensao, caminho=""):
    if caminho == "":
        caminho = os.getcwd()

    os.chdir(caminho)

    a = 1
    l = 3
    regex = re.compile(r'^%s(\d+)' % prefixo)
    numList = []

    lista = os.listdir(caminho)

    for arquivo in lista:
        if arquivo.endswith(extensao):
            mo = regex.search(arquivo)
            if mo != None:
                renomeado = prefixo + str(a).zfill(l) + extensao
                shutil.move(arquivo, renomeado)
                numList.append(renomeado)
                a += 1
                print numList


caminho = ""
prefixo = "spam"
extensao = ".txt"

Preenchendo(prefixo, extensao, caminho)
