class Participant:
    def __init__(self,numeparticipant,listanumere ):
        self.numeParticipant = numeparticipant
        self.listanumere = listanumere

    def getNume(self):
        return self.numeParticipant

    def getLista(self):
        return self.listanumere

    def __str__(self):
        return "Nume:" + str(self.numeParticipant) + " Lista Numere=" + str(self.listanumere)

    def __repr__(self):
        return "Nume:"+str(self.numeParticipant)+" Lista Numere="+str(self.listanumere)


