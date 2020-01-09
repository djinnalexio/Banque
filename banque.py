class compte:
    from random import randint
    ids = []
    def gen_id():
        return "".join([str(compte.randint(0,9)) for x in range(16)])
#1. randint(0,9) gives a random digit between 0 and 9
#2. str turns it into string object
#3. [... for x in range(16)]: creates a list by repeating #1 and #2 16 times
#4. .join turns the list into string. "" indicates we want no separator
#5. the string created by joining random digits together is turned into back
#integer type object
    def __init__(self, prenom, nom, age, adresse, travail, pwd, depot1 = 0):
        self.name = nom.upper(); self.first_name = prenom; self.age = age
        self.full_name = f"{prenom} {nom.upper()}"; self.address = adresse
        self.job = travail; self.id = compte.gen_id(); self.solde = depot1
        self.pwd = pwd
        while self.id in compte.ids:
            self.id = gen_id()#if id happens to be already in the system
#        , keep creating a random id
        compte.ids.append(self.id)


    def show_user(self):
        print (
        f"Nom du detenteur: {self.full_name}\n"
        f"Age: {self.age}\n"
        f"Adresse: {self.address}\n"
        f"Lieu de Travail: {self.job}\n"
        f"Numero de compte: {self.id}\n"
        f"Solde Debiteur: {self.solde} FCFA")

    def deposit(self):
        amount = float(input('Combien souhaitez-vous deposer?\n>'))
        self.solde += amount
        print (f'le montant de {amount} a ete ajoute au compte de {self.full_name}')

    def withdrawal(self):
        amount = float(input('Combien souhaitez-vous retirer?\v>'))
        if amount <= self.solde:
            self.solde -= amount
            print (f'le montant de {amount} a ete retire du compte de {self.full_name}')
        else:
            print ("Fonds insuffisants!")
