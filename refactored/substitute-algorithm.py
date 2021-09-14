def find_person(people_list: list, candidates: list) -> str:
    for person in people_list:
        if person in candidates:
            return person
    return ""
    


candidates = ["Don", "John", "Kent"]
people_list = ["Von", "Don"]

find_person(people_list, candidates)