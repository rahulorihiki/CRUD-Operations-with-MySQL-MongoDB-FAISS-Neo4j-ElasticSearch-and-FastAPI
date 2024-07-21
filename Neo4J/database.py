from neo4j import GraphDatabase


class Neo4jConnection:
    def __init__(self, uri, user, pwd):
        self._driver = GraphDatabase.driver(uri, auth=(user, pwd))

    def close(self):
        self._driver.close()

    def create_student(self, student):
        with self._driver.session() as session:
            session.run(
                "CREATE (s:Student {id: $id, name: $name, age: $age, grade: $grade})",
                student,
            )

    def get_students(self):
        with self._driver.session() as session:
            result = session.run("MATCH (s:Student) RETURN s")
            return [record["s"] for record in result]

    def get_student_by_id(self, student_id):
        with self._driver.session() as session:
            result = session.run(
                "MATCH (s:Student {id: $id}) RETURN s", {"id": student_id}
            )
            return result.single()["s"]

    def update_student(self, student_id, data):
        with self._driver.session() as session:
            session.run(
                "MATCH (s:Student {id: $id}) SET s += $data",
                {"id": student_id, "data": data},
            )

    def delete_student(self, student_id):
        with self._driver.session() as session:
            session.run("MATCH (s:Student {id: $id}) DELETE s", {"id": student_id})
