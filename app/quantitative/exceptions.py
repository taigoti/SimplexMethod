class ModelizacaoError(Exception):
    def __init__(self, message: str = "Ocorreu um erro na otimização do modelo."):
        self.message = message
        super().__init__(self.message)

class SolucaoInviavelError(ModelizacaoError):
    """Exceção lançada quando o modelo não possui uma região viável de solução."""
    def __init__(self, message: str = "O modelo é inviável. As restrições introduzidas contradizem-se."):
        self.message = message
        super().__init__(self.message)

class SolucaoIlimitadaError(ModelizacaoError):
    """Exceção lançada quando a função objetivo pode crescer infinitamente."""
    def __init__(self, message: str = "O modelo é ilimitado. Falta definir restrições para limitar o lucro."):
        self.message = message
        super().__init__(self.message)