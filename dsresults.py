import json
class Dsresults:
    def __init__(self,path):
        self.readDS_file(path)
        if not self.check_structure():
            print("pb de structure bareme du DS")
        if self.classe:
            self.load_students()
    def readDS_file(self,path):
        with open(path) as file:
            dico = json.load(file)
            # self.__dict__  = dico # ou pas
            self.structure = dico["structure"]
            self.bareme = dico["bareme"]
            self.bonus = dico["bonus"]
            self.classe = dico["classe"]
            self.notes = dico["notes"]

    def check_structure(self):
        pass
    def load_students(self):
        pass

if __name__ == '__main__':
    ds= Dsresults('DS1.json')
    print(ds.bonus)