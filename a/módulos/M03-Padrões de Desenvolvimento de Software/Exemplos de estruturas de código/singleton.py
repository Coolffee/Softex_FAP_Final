import logging

class Logger:
    __instance = None

    @staticmethod
    def get_instance():
        if Logger.__instance is None:
            Logger()
        return Logger.__instance

    def __init__(self):
        if Logger.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Logger.__instance = self
            logging.basicConfig(filename='app.log', level=logging.INFO,
                                format='%(asctime)s - %(levelname)s - %(message)s')

    def log(self, message):
        logging.info(message)


if __name__ == "__main__":
    logger1 = Logger.get_instance()
    logger2 = Logger.get_instance()

    logger1.log("Mensagem de log 1")
    logger2.log("Mensagem de log 2")

    #Verificar o arquivo app.log para ver os logs
    print("Logs gravados em app.log")
