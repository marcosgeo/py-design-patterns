# single responsability principal 

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    """
    the three methods bellow introduces another
    respo responsability (persistence) to the class
    and this is an anti-pattern
    """
    # def save(self, filename):
    #     file = open(filename, "w")
    #     file.write(str(self))
    #     file.close()

    # def load(self, filename):
    #     pass

    # def load_from_web(self, uri):
    #     pass

# better approach: responsability in another class
class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


if __name__ == "__main__":
    j = Journal()
    j.add_entry("I cried today")
    j.add_entry("I ate a bug")
    print(f"Journal entries:\n{j}")

    file_name = r"journal.txt"
    PersistenceManager.save_to_file(j, file_name)
