students = ["Omale", "Mohd", "Nur", "Alameen"]
alphabets = "ABCDEFGHIJKLMONPQRSTUVWXYZ"

people = []

for next in students:
    person = {
        "name":next,
        "characters":len(next),
        "firstChar": next[0],
        "lastChar": next[-1],
        "reversed": next[::-1],
        "containsA": 'a' in next,
        "lastIndex": len(next)-1
    }
    people.append(person)

print(people)