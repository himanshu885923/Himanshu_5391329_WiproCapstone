import logging


class LogGen:

    @staticmethod
    def loggen():

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s : %(levelname)s : %(message)s"
        )

        return logging.getLogger()