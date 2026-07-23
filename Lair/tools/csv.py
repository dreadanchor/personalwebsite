import csv

def load_quests(): # Lista de dicionários
    quests = []

    with open("data/quests.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for quest in reader:
            quests.append(quest)

    return quests

def save_quests(quests):
    with open("data/quests.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["titulo", "descricao"]
        )

        writer.writeheader()

        writer.writerows(quests)
