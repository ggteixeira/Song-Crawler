# SongCrawler 💻

## Sumário

* [Introdução](https://github.com/guiemi/song-crawler#introdução)

* [Instalação](https://github.com/guiemi/song-crawler#instalação)

* [Como funciona](https://github.com/guiemi/song-crawler#como-ele-funciona)
* [Bibliografia](https://github.com/guiemi/song-crawler#bibliografia-usada)
* [O que eu aprendi](https://github.com/guiemi/song-crawler#o-que-eu-aprendi)

## Introdução


**SongCrawler** é um [crawler](https://en.wikipedia.org/wiki/Web_crawler) que tem como propósito listar nomes de canções de artistas. 

* A fonte de dados do crawler é o site de letras [Vagalume](https://www.vagalume.com.br). 

* O algoritmo é 100% *command-line-based*, o que significa que ele necessita apenas do shell para rodar.

  ***

  ![crawler-screenshot](https://github.com/guiemi/song-crawler/blob/master/media/crawler-screenshot.png)

## Instalação

**Instalação do Python**: SongCrawler é escrito em Python, ou seja, você precisa tê-lo instalado em seu computador. Para tal, sugiro [este](https://docs.python-guide.org/starting/installation/) guia (*The Hitchhiker's Guide to Python*) para Linux, macOS ou Windows.

**Git Clone**: primeiro passo é clonar este repositório na sua máquina através do seguinte comando:

`git clone https://github.com/guiemi/song-crawler.git`

Após o clone, acesse a pasta principal usando:

`cd song-crawler`

**Virtual Environment**: É enfaticamente recomendado que você crie e habilite um ***virtual environment*** antes do próximo passo. Se você não conhece ou ainda não sabe como usar, há vários tutoriais na internet, inclusive o guia da documentação oficial do [virtualenv/virtualenvwrapper](virtualenv/virtualenvwrapper). Em Português Brasileiro, recomendo [este](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais) guia (*Python e Virtualenv: como programar em ambientes virtuais*).

**Instalando os requisitos**: Com seu *virtual environment* ativado, execute o seguinte comando no seu *shell* para instalar os *requirements*:

`pip install -r requirements.txt`

O `pip install` instala os pacotes necessários à execução do código. A lista completa encontra-se [aqui](https://raw.githubusercontent.com/guiemi/song-crawler/master/requirements.txt).

## Como ele funciona

Para ver a lista de letras de canções do seu artista escolhido, basta utilizar a seguinte sintaxe:

`songcrawler.py nome_do_artista`

Por exemplo, você pode digitar formatos de nomes como:

`python songcrawler.py Queen`,
`python songcrawler.py Pearl Jam`,
`python songcrawler.py Canto dos Malditos na Terra do Nunca`,

e então o crawler entrará em funcionamento, perguntando, antes de printar a lista buscada, quantas canções você deseja:

![crawler-gif](https://github.com/guiemi/song-crawler/blob/master/media/crawler-gif.gif)

## Bibliografia usada

* **livro** *[Python 3 Object-Oriented Programming (2nd edition)](https://www.packtpub.com/application-development/python-3-object-oriented-programming-second-edition)* de [Dusty Phillips](https://github.com/dusty-phillips);

* **livro** [Pro Git](https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches) de [Schott Chacon](https://github.com/schacon);

* **tutorial** *[Como fazer scraping em páginas web com Beautiful Soup e Python 3](https://www.digitalocean.com/community/tutorials/como-fazer-scraping-em-paginas-web-com-beautiful-soup-and-python-3-pt)*, escrito por [Lisa Tagliaferri](https://lisatagliaferri.org);

* **tutorial** [Storing Images and Demos in your Repo](https://gist.github.com/joncardasis/e6494afd538a400722545163eb2e1fa5), escrito por [Jonathan Cardasis](https://gist.github.com/joncardasis);

* **tutorial** [Manually create a Markdown table of contents for your GitHub README](https://www.setcorrect.com/portfolio/work11/), escrito por [Hillary Fraley](https://github.com/hillaryfraley)

* **artigo** *[sys.argv - command line arguments in Python [Part 1]](https://www.kerneldev.com/2018/09/01/command-line-arguments-using-python-sys-argv-part1/)*, escrito por [Sapnesh Naik](https://github.com/SapneshNaik);

* **artigo** [Entendendo as funções lambda no Python](https://medium.com/@otaviobn/entendendo-as-funções-lambda-no-python-cbe3c5abb179), escrito por [Otavio Braga](https://github.com/OtavioBraga);

  

## O que eu aprendi neste projeto

* sys.argv
* map()
* expressões lambda
* ```python
  if __name__ == "__main__":
  main()
  ```
* git orphan branches
* Table of Contents (Markdown)
* exclusão de branches remotas