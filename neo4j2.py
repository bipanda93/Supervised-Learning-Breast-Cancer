from neo4j import GraphDatabase

# 1️⃣ Connexion Neo4j (ATTENTION à l'URI)
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "MonMotDePasseFort"))

# 2️⃣ Fonction de requête
def get_friends(tx, name):
    query = """
    MATCH (p:Person {nom: $name})-[:AMI_DE]->(friend)
    RETURN friend.nom AS nom
    """
    result = tx.run(query, name=name)
    return [record["nom"] for record in result]

# 3️⃣ Exécution
with driver.session() as session:
    friends = session.execute_read(get_friends, "Alice")
    print(f"Amis d’Alice : {friends}")

driver.close()



