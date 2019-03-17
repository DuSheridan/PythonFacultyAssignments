class Repo:
    def __init__(self):
        self.l=[]

    def getAll(self):
        return self.l

    def add_repo(self, obiect):
        self.l.append(obiect)

    # Def:Searches for a certain object in a repo and if found returns it's index
    # In:The desired object
    # Out:The index or valueerror if not found

    def search_repo(self, obiect):
        for i in range(0, len(self.l)):
            if (self.l[i] == obiect):
                return i
        raise ValueError("Can't find object")

    def delete_object_repo(self, obiect):
        p = self.search_repo(obiect)
        del self.l[p]





