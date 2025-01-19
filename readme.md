# Projeto de Inteligência Artificial

Este projeto implementa e executa experimentos com diferentes algoritmos de busca, incluindo DFS, BFS, A*, Busca Gulosa e Dijkstra. O objetivo é comparar o desempenho desses algoritmos em termos de custo, caminho encontrado, nós gerados e nós visitados.

## Estrutura do Projeto

- `main.py`: Arquivo principal que executa os experimentos com diferentes algoritmos de busca.
- `algorithms/`: Diretório contendo as implementações dos algoritmos de busca.
  - `dfs.py`: Implementação do algoritmo de busca em profundidade (DFS).
  - `bfs.py`: Implementação do algoritmo de busca em largura (BFS).
  - `aEstrela.py`: Implementação do algoritmo A*.
  - `busca_gulosa.py`: Implementação do algoritmo de busca gulosa.
  - `dijkstra.py`: Implementação do algoritmo de Dijkstra.
- `actionCost/`: Diretório contendo as funções de custo.
  - `c1.py`, `c2.py`, `c3.py`, `c4.py`: Diferentes funções de custo.
- `heuristic/`: Diretório contendo as funções heurísticas.
  - `h1.py`, `h2.py`: Diferentes funções heurísticas.

## Requisitos

- Python 3.x

## Instalação das dependências
As dependências do projeto (todas listadas no arquivo requirements.txt) podem ser instaladas separadamente com o comando `pip install <nome_da_dependencia>`. 

Muito provavelmente você terá a maioria das dependências instaladas, posto que algumas são nativas do Python. No entanto, se encontrar problemas de versão, pode instalar (ou ajustar) as dependências com o comando `pip install -r requirements.txt`.
Dessa forma, todas as dependências serão instaladas ou atualizadas de acordo com o arquivo requirements.txt.

## Testes

Para executar os experimentos, você pode descomentar a chamada da função correspondente no bloco if __name__ == "__main__": no arquivo main.py
Em seguida, execute o comando:
python main.py

Os resultados dos experimentos serão exibidos no console. Cada experimento imprime o estado inicial, o objetivo, o caminho encontrado, o custo do caminho, o número de nós gerados e o número de nós visitados.