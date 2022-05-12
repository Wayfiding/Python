<h1 align="center">Bem vindo ao TaskMaster 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-Adding Readme -blue.svg?cacheSeconds=2592000" />
  <a href="On Test" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="<img alt=&#34;GitHub&#34; src=&#34;https://img.shields.io/github/license/wayfiding/ROCKETSEAT?color=MIT&logo=MIT&logoColor=MIT&#34;>" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

</div>

<div>
<div>
Línguas:

[English :us:](README.md)

</div>
</div>

# Sobre
> Este é um simples gerenciador de Tarefas desenvolvido no Flask, toda esta pequena aplicação foi desenvolvida no seguinte the [video](https://www.youtube.com/watch?v=Z1RJmh_OqeA&ab_channel=freeCodeCamp.org) do freecodecamp. Depois disso foi implantado no Heroku.

### **Pre-requisitos**
Para poder utilizar as tecnologias providas aqui, você necessitará de um editor e um computador com Linux, Windows ou Mac.

### **Pegar Some uma pasta**
Se você quer somente uma pasta deste repositório, você pode clicar na pasta que quer ou na tabela de conteúdo e lá você irá encontrar um README explicando como baixar somente esta pasta. 

Ou siga os seguintes passos:

1. Clique na Pasta;
2. Copie a URL da barra de endereço do seu navegador;
3. Substitua the 'tree/main' ou 'tree/master' with trunk;

Example:
> https://github.com/Usuário/NomeDoRepositório/tree/main/PastaEscolhida

> https://github.com/Usuário/NomeDoRepositório/trunk/PastaEscolhida

4. Vá para Linha de Comando do seu computador e pegue a pasta escolhida usando o comando SVN

```sh
    svn checkout https://github.com/Usuário/NomeDoRepositório/trunk/PastaEscolhida
```

## Como executar
- Para usuários de Windows será alertado o que fazer em cada etapa.
 - Usuários Windows precisam instalar pelo menos a versão 3.8 do Python, isto pode ser feito acessando o site do [Python](https://www.python.org/).
 - A maioria dos comandos para o Usuários Windows são feitas usando PowerShell.

1. Install > virtualenv :


```sh
$ pip install virtualenv
```

2. Abra o terminal na pasta raiz do projeto e execute os seguintes comandos:


```sh
$ virtualenv env
```
Para (Usuários Windows):
```sh
python -m venv venv
```
3. Então rode os seguintes comandos:

```sh
$ ./env/Scripts/activate
```

4. Then install the dependencies:

```sh
$ (env) pip install -r requirements.txt
```

5. Finalmente inicie o Servidor Web:
   
```sh
(env) python app.py
```
O servidor irá iniciar na Porta 5000 como padrão. Você pode alter isso no app.py, por mudar/adicionar as seguintes linhas:


```sh
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)

```
---- Usuários Windows ----


Se o Python Flask não está funcionando por causa das Políticas do Windows, você deve autorizar usando o seguintes comandos no PowerShell:
```ps1
Set-ExecutionPolicy RemoteSigned
```
or

```ps1
Set-ExecutionPolicy Unrestricted
```
And to check the Execution Policy 

```ps1
Get-ExecutionPolicy
```

More details you can find on [Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.2) website.

## Tecnologias
Neste repositório vocé irá encontrar as seguintes tecnologias usadas:

- Python 3.8
- Flask
- Heroku



## Autor

👤 **Alberto Junior**

* Github: [Alberto Júnior](https://github.com/wayfiding)
* LinkedIn: [Alberto Souza](https://linkedin.com/in/alberto-souza)

## 🤝 Contribuição

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](Teste). 

## Mostre seu Suporte

Give a ⭐️ if this project helped you!

## 📝 Licença
Copyright © 2021 [Alberto Júnior](https://github.com/Wayfiding).<br />

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.

***
This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator) and Alberto