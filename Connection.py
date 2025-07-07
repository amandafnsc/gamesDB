import psycopg2
class Connection():
    @staticmethod
    def getConnection():
            return psycopg2.connect(
            user='postgres',
            password='levi123',
            host='localhost',
            port='5432',
            database='gamesDB2'
        )