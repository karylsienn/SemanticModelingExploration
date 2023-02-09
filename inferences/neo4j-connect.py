from neo4j import GraphDatabase


class App:

    @staticmethod
    def init_driver(uri, username, password):
        driver = GraphDatabase.driver(uri, auth=(username, password))
        driver.verify_connectivity()  # Verify if the connections is made
        return driver


if __name__=='__main__':

    App.init_driver(
        uri="bolt://localhost:7687",
        username="neo4j",
        password="neo")
