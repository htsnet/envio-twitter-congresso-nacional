# envio-twitter-congresso-nacional
Envie rapidamente twittes aos deputados federais ou senadores de forma automática (mesmo conteúdo para cada um deles)


A tecnologia pode ajudar em muita coisa: entretenimento, cultura, esportes, comércio, medicina e muitas outras áreas. E pode ajudar também na política.

Eu vi, estarrecido, 2 reportagens de de capa na Revista Crusoé (setembro/2020) com graves denúncias contra o min. Toffoli, casos do passado recente e casos atuais, de estrema gravidade. E para minha surpresa, nem a grande mídia nem o senado parece terem se importado com isso.

Eu iniciei o envio de twittes aos senadores manualmente, através da lista dos senadores do site https://lnkd.in/dd4qW36. Mas é muito demorado e cansativo.

Então, que tal usar os conhecimentos adquiridos e criar uma automação para este processo? Assim posso enviar todo dia a todos os senadores, fazendo minha pressão sobre o assunto.

Criei um script em Python, com a biblioteca Selenium e o ChromeDriver. O script busca o mesmo site com todos os senadores, faz o login na minha conta no Twitter e dispara a mensagem que eu digito a cada um dos senadores.

Fiz um pequeno vídeo mostrando o script em ação: https://lnkd.in/dpzAtAT

________________________________________________________________________________________

Quer usar? Veja as orientações. Para preparar o ambiente você precisa:
1 - Ter o Python 3.x instalado
2 - Baixar o ChromeDriver (https://chromedriver.chromium.org/downloads) de acordo com o seu sistema e saber onde você o armazenou no seu aparelho 
3 - Ter uma conta no Twitter (id e senha)
4 - Baixar o arquivo "envioTwitterCongresso.py" (deste repositório)
5 - Editar as primeiras linhas do arquivo "envioTwitterCongresso.py" de acordo com suas informações

Uma vez preparado, a cada execução você deve:
1 - Abrir um terminal do Windows.
2 - Mude para a pasta onde você baixou o arquivo deste repositório
3 - Execute "python envioTwitterCongresso.py"
4 - Informe de acordo com as mensagens do programa
5 - Espere até o término da execução

________________________________________________________________________________________

#revistacrusoe #senado #python #stf #automacao
