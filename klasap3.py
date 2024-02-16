import random
import os

class Recnik():
    def __init__(self,engleska_rec,srpska_rec):
        self.engleska_rec = engleska_rec
        self.srpska_rec = srpska_rec
    def __str__(self):
        return '{}!{}'.format(self.engleska_rec,self.srpska_rec)
    
class Participanti():
    def __init__(self,takmicar,bodovi):
        self.takmicar = takmicar
        self.bodovi = bodovi
    def __str__(self):
        return '{}!{}'.format(self.takmicar,self.bodovi)
    
class Igrica():
    def __init__(self):
        self.recnik = []
        self.takmicari = []
        self.provera = False
        self.brojac = 0

    def ucitaj(self):
        datoteka_recnik = os.path.join(os.path.dirname(__file__), 'recnikp3.txt')
        a = [line.strip() for line in open(datoteka_recnik,encoding = 'utf-8')]
        for i in a:
            r = i.split('!')
            e = Recnik(r[0],r[1])
            self.recnik.append(e)

        datoteka_username = os.path.join(os.path.dirname(__file__), 'usernamep3.txt')
        b = [line.strip() for line in open(datoteka_username, encoding = 'utf-8')]
        for i in b:
            r1 = i.split('!')
            u = Participanti(r1[0],r1[1])
            self.takmicari.append(u)
            
    def usernamebox(self):
        c = []
        self.takmicari.sort(key = lambda i: int(i.bodovi), reverse = True)
        for i in self.takmicari:
            c.append(i.takmicar + ' poeni: ' + str(i.bodovi))
        return c
    
    def wordbox(self):
        d = []
        for i in self.recnik:
            d.append(i.srpska_rec)
        return d
    
    def dodaj_rec(self,engleska_rec,srpska_rec):
        for i in self.recnik:
            if i.engleska_rec == engleska_rec:
                return 'Ova rec vec postoji u recniku'
        if engleska_rec == '' or srpska_rec == '':
            return 'Popuni sva polja'
        if engleska_rec.isalpha()== False or srpska_rec.isalpha() == False:
            return 'Rec mora da sadrzi samo slova!'
        e=Recnik(engleska_rec,srpska_rec)
        self.recnik.append(e)
        self.update_recnik()
        return 'Rec je uspesno dodata'
    
    def update_recnik(self):
        f = open('recnikp3.txt','w',encoding = 'utf-8')
        for i in self.recnik:
            print(i,file = f)
        f.close()
        
    def update_takmicari(self):
        f1 = open('usernamep3.txt','w',encoding = 'utf-8')
        for i in self.takmicari:
            print(i,file = f1)
        f1.close()
        
    def rekord(self):
        bod = 0
        for i in self.takmicari:
            if int(i.bodovi) > bod:
                bod = int(i.bodovi)
        return 'Rekord: {}'.format(bod)
    
    def provera_znanja(self,engleska_rec,srpska_rec):
        if srpska_rec == '':
            return 'Popuni sva polja'
        for i in self.recnik:
            if i.engleska_rec == engleska_rec:
                if i.srpska_rec == srpska_rec:
                    self.niz = True
                    self.brojac += 1
                    return 'Bravo,to je tacan odgovor!'
                        
                else:
                    self.provera = True
                    return 'Odgovor nije tacan. \n Tacan odgovor je: {}'.format(i.srpska_rec)
    def dodaj_nalog(self,takmicar,bodovi):
        if takmicar == '':
            return 'Unesite svoje ime'
        p = Participanti(takmicar,bodovi)
        self.takmicari.append(p)
        f2 = open('usernamep3.txt','w',encoding = 'utf-8')
        for i in self.takmicari:
            print(i, file = f2)
        f2.close()
        return 'Uspesno si se dodao na rang listu'
    
    def dodaj_izmene(self,srpska_rec,nova_engleska_rec,nova_srpska_rec):
        if nova_engleska_rec == '' or nova_srpska_rec == '':
            return 'Popuni sva polja'
        for i in self.recnik:
            if i.srpska_rec == srpska_rec:
                i.srpska_rec = nova_srpska_rec
                i.engleska_rec = nova_engleska_rec
            
        self.update_recnik()
        return 'Uspesno ste izmenili rec u recniku'
        
            
    def random_eng(self,slucajna_rec):
        r = []
        for i in self.recnik:
            r.append(i.engleska_rec)
        random_rec = random.choices([word for word in r if word != slucajna_rec])  
        return ''.join(random_rec)
    
    def prva_rec(self):
        m = []
        for i in self.recnik:
            m.append(i.engleska_rec)
        random_rec1=random.choices(m)
        return ''.join(random_rec1)



R=Igrica()
R.ucitaj()















        
            
        
        
        
