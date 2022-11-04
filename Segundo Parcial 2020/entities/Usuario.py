class Usuario:
    def __init__(self, mail: str, contenido_visto: list) -> None:
        self._mail = mail
        self._contenido_visto = [contenido_visto]

    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, mail):
        self._mail = mail

    @property
    def contenido_visto(self):
        return self._contenido_visto

    @contenido_visto.setter
    def contenido_visto(self, contenido_visto):
        self._contenido_visto = contenido_visto
