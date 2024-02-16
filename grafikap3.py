from klasap3 import *
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedStyle


root=Tk()

style = ThemedStyle(root)
style.set_theme("blue")
root.geometry('900x500')
root.title('Vocabulary_Game')

zatvoren_t1 = False
zatvoren_t2 = False
otvoren_t2 = False

def dodaj():
    global b
    t = Toplevel(root)
    tl = Label(t,text = 'Engleska rec').pack()
    et = ttk.Entry(t)
    et.pack()
    tl1 = Label(t,text = 'Srpska rec').pack()
    et1 = ttk.Entry(t)
    et1.pack()
    tb = ttk.Button(t,text = 'Sacuvaj',command = lambda:[tl2.configure(text=R.dodaj_rec(et.get(),et1.get())),obnovi_lb1(),isprazni_entri(tl2,et,et1)]).pack()
    tl2 = Label(t,text = '')
    tl2.pack()
    t.protocol("WM_DELETE_WINDOW", lambda: [b.config(state=NORMAL),t.destroy()])
    
def isprazni_entri(tl2,et,et1):
    if tl2.cget('text') == 'Rec je uspesno dodata':
        et.delete(0,END)
        et1.delete(0,END)
        
def numerisi(lb,c):
    for index,i in enumerate(c,start=1):
        formatirano = '{}. mesto: {}'.format(index,i)
        lb.insert(END, formatirano)
        
def provera():
    global b1, slucajna_rec, t1b, t1b1,zatvoren_t1,zatvoren_t2,otvoren_t2
    slucajna_rec = R.prva_rec()
    t1 = Toplevel(root)
    t1.geometry('300x300')
    t1l = Label(t1,text = slucajna_rec)
    t1l.grid(row = 1,column = 1)
    t1l1 = Label(t1,text = 'Upisi prevod na srpski').grid(row = 2,column = 1)
    t1e = ttk.Entry(t1)
    t1e.grid(row = 3,column = 1)
    t1b1 = ttk.Button(t1,text='Sledeca rec',command = lambda :[sledeca_rec(t1l, t1e,t1l2),t1b.config(state=NORMAL)])
    t1b1.grid(row = 4,column = 2)
    t1b = ttk.Button(t1,text = 'Proveri',command = lambda: [t1l2.configure(text = R.provera_znanja(slucajna_rec,t1e.get())),t1l4.configure(text=R.brojac),regulator_dugmeta(t1b,t1l2),dodaj_nal()])
    t1b.grid(row = 4,column = 1)
    t1l2 = Label(t1,text = '')
    t1l2.grid(row=5,column = 1)
    t1l3 = Label(t1,text='Vatreni niz').grid(row = 1,column = 2)
    t1l4 = Label(t1,text = str(R.brojac),bg = 'red',width = 3,fg = 'black',relief = 'solid')
    t1l4.grid(row = 2,column = 2)
    t1.protocol('WM_DELETE_WINDOW',lambda: [zatvaranje_t1(),zatvaranje(t1)])
    
def regulator_dugmeta(t1b,t1l2):
        if t1l2.cget('text') == 'Bravo,to je tacan odgovor!':
            t1b.config(state=DISABLED)
       
        
def sledeca_rec(label, entry,obrisi):
    global slucajna_rec
    slucajna_rec = R.random_eng(slucajna_rec)
    label.configure(text = slucajna_rec)
    entry.delete(0, END)
    obrisi.configure(text='')
        
def dodaj_nal():
    global l, t1b, t2b, t1b1,zatvoren_t1,zatvoren_t2,otvoren_t2

    if R.provera == True:
        otvoren_t2 = True
        t1b.config(state = DISABLED)
        t1b1.config(state = DISABLED)
        t2 = Toplevel(root)
        t2l = Label(t2,text = 'Vise srece drugi put. Tvoj broj bodova je: {}'.format(R.brojac)).pack()
        t2l1 = Label(t2,text = 'Upisi svoje ime za rang listu').pack()
        t2e = ttk.Entry(t2)
        t2e.pack()
        t2b = ttk.Button(t2,text = 'Potvrdi',command = lambda:[t2l2.configure(text = R.dodaj_nalog(t2e.get(),R.brojac)),obnovi_lb(),l.configure(text = R.rekord()),t2b.config(state = DISABLED)])
        t2b.pack()
        t2l2 = Label(t2,text = '')
        t2l2.pack()
        t2.protocol('WM_DELETE_WINDOW',lambda: [zatvaranje_t2(t2),[b1.config(state=NORMAL)] if zatvoren_t1 and zatvoren_t2 else False])
        
def zatvaranje_t1():
    global zatvoren_t1
    zatvoren_t1 = True
    
def zatvaranje_t2(t2):
    global zatvoren_t2
    zatvoren_t2 = True
    t2.destroy()
    
def zatvaranje(t1):
    global zatvoren_t1, zatvoren_t2,otvoren_t2
    if zatvoren_t1 and zatvoren_t2:
        b1.config(state = NORMAL)
    if otvoren_t2 == False:
        b1.config(state = NORMAL)
    t1.destroy()
      
def obnovi_lb():
    global lb
    lb.delete(0,END)
    for i in R.usernamebox():
        lb.insert(END,i)
        
def obnovi_lb1():
    global lb1
    lb1.delete(0,END)
    for i in R.wordbox():
        lb1.insert(END,i)
        
def povezi_listu(dogadjaj):
    if lb1.focus_get() == lb1:
        selektovana_rec = lb1.get(lb1.curselection())
        e1.delete(0,END)
        e1.insert(END, selektovana_rec)
        for i in R.recnik:
            if i.srpska_rec == selektovana_rec:
                e2.delete(0,END)
                e2.insert(END, i.engleska_rec)
    
def regulator():
    global zatvoren_t1,zatvoren_t2,otvoren_t2
    R.provera = False
    R.brojac = 0
    zatvoren_t1 = False
    zatvoren_t2 = False
    otvoren_t2 = False
    
    

frame_lb=ttk.Frame(root)
frame_lb.grid(row = 1,column = 1,rowspan = 4,padx = 10,pady = 10, sticky = 'nsew')

lb = Listbox(frame_lb,relief = 'flat',width = 35)
lb.grid(row = 0,column = 0,sticky = 'nsew')

scrollbar_lb = ttk.Scrollbar(frame_lb, orient = 'vertical',command = lb.yview)
scrollbar_lb.grid(row = 0,column = 1,sticky = 'ns')

lb['yscrollcommand'] = scrollbar_lb.set
c=[]
for i in R.usernamebox():
    c.append(i)
numerisi(lb,c)

frame_lb1 = ttk.Frame(root)
frame_lb1.grid(row = 1, column = 4, rowspan = 4,padx = 10, pady = 10, sticky = 'nsew')

lb1 = Listbox(frame_lb1, relief='flat', width = 25)
lb1.grid(row=0, column=0, sticky='nsew')

scrollbar_lb1 = ttk.Scrollbar(frame_lb1, orient='vertical', command = lb1.yview)
scrollbar_lb1.grid(row = 0, column = 1, sticky = 'ns')

lb1['yscrollcommand'] = scrollbar_lb1.set


for i in R.wordbox():
    lb1.insert(END,i)
lb1.bind('<<ListboxSelect>>', povezi_listu)
e1=ttk.Entry(root)
e1.grid(row = 1,column = 5,padx = 10,pady = 10)
e2=ttk.Entry(root)
e2.grid(row = 2,column = 5,padx = 10,pady = 10)

b = ttk.Button(root,text = 'Nova rec',command = lambda:[dodaj(),b.config(state = DISABLED)])
b.grid(row = 1,column = 2,padx = 10, pady = 10)

b1 = ttk.Button(root,text = 'Proveri znanje',command = lambda:[provera(),regulator(),b1.config(state = DISABLED)])
b1.grid(row=1,column=3)

b2=ttk.Button(root,text = 'Sacuvaj izmenu',command = lambda:[l1.configure(text = R.dodaj_izmene(lb1.get(ANCHOR),e2.get(),e1.get())),obnovi_lb1()]).grid(row = 3,column = 5)

l = Label(root,text = R.rekord(),relief = 'solid',padx=3)
l.grid(row = 2,column = 3)
l1 = Label(root,text = '')
l1.grid(row = 4,column = 5)


root.mainloop()













