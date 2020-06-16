# desafioserasa
Olá!
Este repositório é referente ao desafio proposto pelo processo seletivo do SERASA com a PROWAY.

Tecnologias utilizadas: Python 3.8.3 (linguagem) e tkinter (interface gráfica).

Para rodar o projeto, execute o arquivo Main.py (pode ser feito através do comando "py -u Main.py" dentro do diretório /src)
    --> Inclui um arquivo .BAT na pasta /src que executa este comando automaticamente.

Ao executar o projeto, o mesmo irá gerar automaticamente 18 empresas com a sua pontuação neutra (50) como descrito na especificação do projeto.

Na tela inicial existem dois botões: Carregar Dados e Consultar Ranking.

  --> Carregar Dados: Este botão abrirá uma tela adicional onde o usuário deve selecionar uma das empresas já cadastradas no sistema através da ComboBox presente. Após selecionar uma das opções, basta clicar em Carregar Dados para selecionar um arquivo .TXT de entrada, que contém o seguinte formato:
  
    +3,-2
   
   Onde: '+3' indica que a empresa em questão tem 3 Notas Fiscais e '-2' que a empresa tem 2 débitos em aberto. A vírgula é um separador essencial para o funcionamento da leitura da entrada.
 
 Caso seja do interesse do usuário, na tela de Carregar Dados é possível clicar no botão Gerar Entrada para que o sistema gere um arquivo de entrada com valores aleatórios para fins de teste. Este arquivo será gerado e salvo na pasta 'entradas' na raiz do projeto.
 Após selecionar um arquivo de entrada, o mesmo será processado e os valores já estarão atualizados para consulta.
 
 --> Consultar Ranking: Este botão abrirá uma tela adicional onde o usuário pode visualizar o estado atual das empresas cadastradas no sistema. Para fazer a consulta basta clicar no botão "Consultar" para gerar o relatório.
 Este relatório exibe de forma ordenada e decrescente o ranking das empresas cadastradas de acordo com sua pontuação calculada com base nas entradas efetuadas, assim como o número de notas fiscais e débitos da empresa em questão. Caso nenhuma entrada tenha sido feita, o valor exibido será o valor padrão inicial (50).
 
O arquivo de testes unitários se encontra na pasta 'src', com nome de 'Empresas_test.py'. Este arquivo pode ser executado para avaliar o funcionamento das principais funções do sistema.

O projeto se resume à isto, espero que se apresente de forma clara e intuitiva para os usuários. Quaisquer dúvidas estou à disposição!

Atenciosamente, Heitor Silveira.

E-mail: heitorsilveirafurb@gmail.com
