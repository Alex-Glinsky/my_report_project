class Report:
    """Базовый класс отчёта — легко расширять новыми."""

    def __init__(self, files: list[str]):
        self.files = files

    def load_data(self):
        raise NotImplementedError

    def generate(self):
        raise NotImplementedError
