
class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for peep in people:
        result.append(Person(peep["name"], peep["age"]))
    for peep in people:
        person = Person.people[peep["name"]]
        if "wife" in peep and peep["wife"] is not None:
            person.wife = Person.people[peep["wife"]]
        if "husband" in peep and peep["husband"] is not None:
            person.husband = Person.people[peep["husband"]]

    return result
