# Unequal Lenght Maze Game
Encontra um caminho desde o canto inferior esquerdo até ao canto superior direito, passando por cada quadrado branco exatamente uma vez. O caminho deve alternar segmentos horizontais e verticais, e dois segmentos consecutivos não podem ter o mesmo comprimento.

Temos scripts de python que criam, dão dicas e solucionam níveis pré-definidos do jogo, além da possibilidade de criar o seu próprio Maze e resolver.

## Bibliotecas necessárias:
### Para o jogo:
- ```pip install -r requirements.txt ```
- 
## Como abrir o jogo
Abrir a pasta dos scripts e correr o seguinte comando:
- ```python main.py ```
  
O jogo irá abrir-se automaticamente.

## Como jogar:
### Instruções níveis pré-selecionados:
- Depois de abrir o jogo, selecionar um nível. 
- Para jogar, pode andar usando as teclas de direção do teclado ou clicando no quadrado que deseja com o botão esquerdo do rato. 
- Para pedir uma dica, pode usar a tecla 'H' do teclado, ou carregar no respetivo botão. 
- Para pedir a um dos algoritmos para resolver, pode clicar no botão respetivo com o botão esquerdo do rato, ou pressionar a tecla de atalho de teclado indicada entre parênteses depois do nome do algoritmo.
- Se ganhar, irá aparecer no ecrã 'You Won!' e retornará ao menu principal.
- Se não houver solução para o puzzle ou o escolheu um caminho impossível de continuar, irá aparecer no ecrã 'Impossible Game!' e retornará ao ecrã principal.

### Instruções 'Build your own maze':
- Escolher no menu principal a opção 'Build your own maze'.
- Escolher as dimenções do Maze, introduzindo dois números separados por um espaço remetentes ao número de linhas (rows) e colunas (cols), depois premir a tecla Enter.
- Escolher onde colocar os obstáculos/paredes, carregando com o botão esquerdo do rato no quadrado desejado.
- Para retirar uma parede, carregar com o botão esquerdo do rato na parede que deseja retirar.
- Depois de ter as paredes desejadas selecionadas, clicar 'Done' ou premir a tecla 'Enter'.
- Jogar usando as instruções dadas para níveis pré-selecionados.
	
