import psycopg2
class Connection():
    @staticmethod
    def getConnection():
            return psycopg2.connect(
            user='postgres',
            password='090405',
            host='localhost',
            port='5432',
            database='gamesDB2'
        )