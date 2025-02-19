import pandas as pd


class CsvManager:
    """
    Classe que gerencia o processamento com pandas de um arquivo CSV.

    Esta classe permite a leitura, manipulação e armazenamento de dados
    contidos em um arquivo CSV. Utiliza a biblioteca pandas para facilitar
    operações com DataFrames, permitindo adicionar colunas, atualizar
    valores e verificar condições específicas nos dados.

    Attributes:
        file (str): O caminho para o arquivo CSV a ser processado.
        df (pandas.DataFrame): O DataFrame representando os dados do
        arquivo CSV.
    """

    def __init__(self, file):
        """
        Inicializa a classe CsvManager.

        Esta função configura o caminho do arquivo CSV e inicia a leitura
        do conteúdo do arquivo, carregando os dados em um DataFrame.

        Args:
            file (str): O caminho para o arquivo CSV a ser processado.
        """
        self.file = file
        self.df = None
        self._read_file()

    
    def _read_file(self):
        """
        Lê o arquivo CSV e carrega os dados em um DataFrame.

        Utiliza a função pd.read_csv() do pandas para ler o arquivo. 
        Caso ocorra um erro durante a leitura, uma exceção é lançada.
        """
        try:
            self.df = pd.read_csv(self.file, engine='python')
        except Exception as error:
            raise Exception(f'Erro ao ler o arquivo CSV: {error}')


    def add_column_status(self):
        """
        Adiciona uma coluna 'status' ao DataFrame se não existir.

        Inicializa todos os valores na nova coluna como 'pendente'.
        Verifica se o DataFrame foi carregado corretamente antes de
        realizar a operação.https://poe.com/chat/2x1z8fyiqnjhrk8s88f
        """
        if self.df is None or not isinstance(self.df, pd.DataFrame):
            raise ValueError("O DataFrame não está carregado corretamente.")
        if 'status' not in self.df.columns:
            self.df['status'] = 'pendente'


    def view_df(self):
        """
        Imprime o conteúdo do DataFrame no console.

        Essa função é útil para visualizar rapidamente os dados 
        carregados e suas colunas.
        """
        print(self.df)


        
    def get_row_by_id(self, id_row: int) -> pd.Series:
        """
        Retorna uma linha inteira a partir do ID utilizando iloc.

        Permite acessar dados de uma linha específica no DataFrame
        com base no índice fornecido.

        Args:
            id_row (int): Índice da linha do arquivo CSV para ser consumida.

        Returns:
            pd.Series: A linha correspondente ao índice fornecido.
        """
        row = self.df.iloc[id_row]
        return row


    def check_pending_lines(self) -> bool:
        """
        Verifica se ainda existem linhas com status igual a 'pendente'.

        Essa função permite identificar se há tarefas que ainda não foram
        concluídas, baseado na coluna 'status'.

        Returns:
            bool: Retorna True se existir linhas pendentes, False
            caso o contrário.
        """
        pendings = self.df[self.df['status'] == 'pendente']
        return not pendings.empty
    

    def update_value_by_id(self, id_row: int, column: str, value: str):
        """
        Atualiza o valor de uma coluna específica na linha especificada.

        Esta função é usada para alterar o valor de uma célula no DataFrame,
        identificando a linha pelo índice.

        Args:
            id_row (int): Índice da linha que vai ser atualizada.
            column (str): Nome da coluna que será atualizada.
            value (str): Novo valor a ser atribuído à célula.
        """
        self.df.at[id_row, column] = value

    
    def update_value_by_query(
            self, name_column: str, item_value: str, status: str, column: str
        ):
        """
        Atualiza o valor de uma coluna correspondente a uma condição.

        Procura no DataFrame a linha onde o valor de uma coluna específica
        corresponde ao valor fornecido. Se encontrar uma correspondência,
        o valor da coluna designada será atualizado.

        Args:
            name_column (str): O nome da coluna a ser pesquisado no DataFrame.
            item_value (str): Valor do item a ser pesquisado na coluna.
            status (str): O novo valor a ser atribuído à coluna correspondente.
            column (str): Nome da coluna onde o valor será alterado.
        """
        row_with_value = self.df[name_column] == item_value
        if row_with_value.any():
            self.df.loc[row_with_value, column] = status

    
    def save_file(self, path_file: str = None):
        """
        Salva o DataFrame modificado de volta para um arquivo CSV.

        Permite especificar um caminho para salvar o arquivo. Se nenhum caminho
        for fornecido, o arquivo será salvo no mesmo local do arquivo original.

        Args:
            path_file (str, optional): Caminho onde será salvo o arquivo.
        """
        if not path_file:
            path_file = self.file
        self.df.to_csv(path_file, sep=',', index=False)
        