#!/usr/bin/env python3
from os import getlogin as expanduser
import customtkinter as tk
from functools import partial
import webbrowser
import threading
import requests
import bs4
from PIL import Image
from io import BytesIO
Nam=0
Gra=0
Ima=0
Ope=0
win=0
class imagefromweb:
    class WebImage:
     def __init__(self,url):
          u = requests.get(url)
          self.image = Image.open(BytesIO(u.content))
          self.height= self.image.height
          self.width=self.image.width
class Mountain_Project:
    def links(InputLink):
        rq=requests.get(InputLink)
        bee=bs4.BeautifulSoup(rq.content,'html.parser')
        fa=str(bee.find_all('div',class_='max-height max-height-md-0 max-height-xs-400'))
        bee2=bs4.BeautifulSoup(fa,'html.parser')
        fam=bee2.find_all('a')
        links=[]
        for ob in fam:
            rob=str(ob)
            if rob[3]=='h':
                roo=rob.split('"')[1]
                links.append(roo)
            pass
        pass
        return(links)
    pass
    class AreaContent():
        def __init__(self, InputLink: str):
            rqac=requests.get(InputLink)
            beeac=bs4.BeautifulSoup(rqac.content,'html.parser')
            #Description
            debac=beeac.find('div', class_='fr-view')
            cra=str(debac).replace('<p>','\n').split('<')
            de=[]
            for ob in cra:
                if '>' in ob:
                    obs=ob.split('>')[1]
                    de.append(obs)
            pass
            self.Description=''.join(de)
            #Name
            nabrc=str(beeac.find('h1'))
            self.Name=nabrc.replace('\n','').split('<s')[0][8:]
            #Total Climbs
            tcbrc=str(beeac.find('div',id='route-count-container'))
            ARealMadeUpName=bs4.BeautifulSoup(tcbrc,'html.parser')
            self.TotalClimbs=int(str(ARealMadeUpName.find('h2'))[4:][::-1][17:][::-1].replace(',',''))
    class RouteContent():
        def Grade(InputLink: str):
                rqe=requests.get(InputLink)
                beerc=bs4.BeautifulSoup(rqe.content,'html.parser')
                grbrc=beerc.find('span',class_='rateYDS')
                return(str(grbrc).split('>')[1].split('<')[0].replace(' ',''))
        def Type(InputLink: str):
                rqe=requests.get(InputLink)
                beerc=bs4.BeautifulSoup(rqe.content,'html.parser')
                rtab=bs4.BeautifulSoup(str(beerc.find('table',class_='description-details')),'html.parser')
                tybrc=str(rtab.find_all('td')[1]).replace('\n','')
                return(tybrc.replace(' ','').split('>')[1].split('<')[0])
        def Stars(InputLink: str):
                rid=InputLink.split('/')[4]
                rqe=requests.get(InputLink)
                beerc=bs4.BeautifulSoup(rqe.content,'html.parser')
                stbrc=beerc.find('span',id=f'starsWithAvgText-{rid}')
                return(str(stbrc).split('</span>')[1].replace('\n','').split(' ')[5])
        def FA(InputLink: str):
            rqe=requests.get(InputLink)
            beerc=bs4.BeautifulSoup(rqe.content,'html.parser')
            rtab=bs4.BeautifulSoup(str(beerc.find('table',class_='description-details')),'html.parser')
            fabrc=str(rtab.find_all('td')[3])
            return(fabrc.replace('\n','')[44:][::-1][41:][::-1])
        def PageViews(InputLink: str):
            rqe=requests.get(InputLink)
            beerc=bs4.BeautifulSoup(rqe.content,'html.parser')
            rtab=bs4.BeautifulSoup(str(beerc.find('table',class_='description-details')),'html.parser')
            pvbrc=str(rtab.find_all('td')[5])
            return(int(pvbrc.replace('\n','')[4:].replace(' ','').split('t')[0].replace(',','')))
        def SharedBy(InputLink: str):
            rqe=requests.get(InputLink)
            beerc=bs4.BeautifulSoup(rqe.content,'html.parser')
            rtab=bs4.BeautifulSoup(str(beerc.find('table',class_='description-details')),'html.parser')
            sbbrc=str(rtab.find_all('td')[7])
            return(sbbrc.replace('\n','').split('>')[2].split('<')[0])
        def Name(InputLink: str):
            rqe=requests.get(InputLink)
            beerc=bs4.BeautifulSoup(rqe.content,'html.parser')
            nabrc=str(beerc.find('h1'))
            return(nabrc.replace('\n','').split('<s')[0][8:].replace('  ',''))
        def Area(InputLink: str):
            rqe=requests.get(InputLink)
            beerc=bs4.BeautifulSoup(rqe.content,'html.parser')
            lin=str(beerc.find('div',class_='mb-half small text-warm'))
            belin=bs4.BeautifulSoup(lin,'html.parser')
            lin2=list(belin.find_all('a'))
            rear=[]
            for line1 in lin2:
                rlin=str(line1)
                href=rlin.split('"')[1]
                rear.append(href)
            pass
            return(rear)
        def Pictures(InputLink: str):
            rqe=requests.get(InputLink)
            beerc=bs4.BeautifulSoup(rqe.content,'html.parser')
            pibrc=beerc.find_all('img',class_='lazy')
            image=[]
            for img in pibrc:
                we=str(img)
                if 'src=' in we:
                    im=we.split('src=')[1].split('"')[1]
                    image.append(im)
                pass
            pass
            return(image)
        def Description(InputLink: str):
            rqe=requests.get(InputLink)
            beerc=bs4.BeautifulSoup(rqe.content,'html.parser')
            debrc=beerc.find('div', class_='fr-view')
            cra=str(debrc).replace('<p>','\n').split('<')
            de=[]
            for ob in cra:
                if '>' in ob:
                    obs=ob.split('>')[1]
                    de.append(obs)
            pass
            return(''.join(de))
        pass
    pass
    class AllInfo():
      def __init__(self,InputLink: str):
            rqe=requests.get(InputLink)
            beerc=bs4.BeautifulSoup(rqe.content,'html.parser')
            grbrc=beerc.find('span',class_='rateYDS')
            rid=InputLink.split('/')[4]
            rtab=bs4.BeautifulSoup(str(beerc.find('table',class_='description-details')),'html.parser')
            self.Grade=str(grbrc).split('>')[1].split('<')[0].replace(' ','')

            tybrc=str(rtab.find_all('td')[1]).replace('\n','')
            self.Type=tybrc.replace(' ','').split('>')[1].split('<')[0].replace('\n','')


            stbrc=beerc.find('span',id=f'starsWithAvgText-{rid}')
            self.Stars=str(stbrc).split('</span>')[1].replace('\n','').split(' ')[5]

            fabrc=str(rtab.find_all('td')[3])
            self.FA=fabrc.replace('\n','')[44:][::-1][41:][::-1]

            pvbrc=str(rtab.find_all('td')[5])
            self.PageViews=(int(pvbrc.replace('\n','')[4:].replace(' ','').split('t')[0].replace(',','')))

            sbbrc=str(rtab.find_all('td')[7])
            self.SharedBy=(sbbrc.replace('\n','').split('>')[2].split('<')[0])

            nabrc=str(beerc.find('h1'))
            self.Name=nabrc.replace('\n','')[8:].replace('  ','').split('<')[0]

            lin=str(beerc.find('div',class_='mb-half small text-warm'))
            belin=bs4.BeautifulSoup(lin,'html.parser')
            lin2=list(belin.find_all('a'))
            rear=[]
            for line1 in lin2:
                rlin=str(line1)
                href=rlin.split('"')[1]
                rear.append(href)
            pass
            self.Area=(rear)


            pibrc=beerc.find_all('img',class_='lazy')
            image=[]
            for img in pibrc:
                we=str(img)
                if 'src=' in we:
                    im=we.split('src=')[1].split('"')[1]
                    image.append(im)
                pass
            pass
            self.Pictures=(image)

            debrc=beerc.find('div', class_='fr-view')
            cra=str(debrc)[4:].replace('<p>','\n').split('<')
            de=[]
            for ob in cra:
                if '>' in ob:
                    obs=ob.split('>')[1]
                    de.append(obs)
            pass
            self.Description=(''.join(de))
            pass

pass
class Mountain_project_finder:
    def findclimbs(link):
        global wow
        if '/area/' in link:
            lks=Mountain_Project.links(link)
            for links in lks:
                Mountain_project_finder.findclimbs(links)
            pass
        elif '/route/' in link:
            wow=Mountain_Project.AllInfo(link)
            if len(wow.Pictures)>0:
                pic=wow.Pictures[0]
            else:
                pic='None'
            disk=wow.Description.replace('\n','')
            file.write(f'{wow.Name}///{wow.Grade}///{link}///{wow.Stars}///{pic}///{wow.Type}///{disk}///{wow.FA}///{wow.SharedBy}\n')
            threading.Thread(target=Mountain_project_finder.configu).start()
        pass
    pass
    def startmpf(fn,inp):
        global file,config,tota,config2
        config=tk.CTkLabel(window,font=('arial',30),text='')
        config.pack(anchor='center')
        config2=tk.CTkLabel(window,font=('arial',30),text='')
        config2.pack(anchor='center')
        tota=Mountain_Project.AreaContent(inp).TotalClimbs
        fr.place_forget()
        thing.place_forget()
        file=open(fn,'w')
        file.close()
        file=open(fn,'a')
        Mountain_project_finder.findclimbs(inp)


        config.configure(text='Done',text_color='light green')
        file.close()
    pass
    def UIthingy(Name,Link,filenam):
        global exist,label1,grid
        if exist:
            label1.pack_forget()
            grid.pack_forget()
        pass
        exist=1
        label1=tk.CTkLabel(thing,text=f'What to do with {Name}')
        label1.pack(anchor='center')
        grid=tk.CTkFrame(thing)
        grid.pack_propagate(True)
        grid.columnconfigure(0)
        Button1=tk.CTkButton(grid,text='Update',command=lambda: threading.Thread(target=partial(Mountain_project_finder.startmpf,filenam,Link)).start())
        Button1.grid(column=0,row=0)
        Button2=tk.CTkButton(grid,text='Delete',fg_color='red',command=lambda: Mountain_project_finder.Delete(Link,f'/home/{expanduser()}/.local/share/applications/MPS/Searchpybuttons.txt'))
        Button2.bind('<Enter>',lambda event: Button2.configure(text_color='red',fg_color='white'))
        Button2.bind('<Leave>',lambda event: Button2.configure(text_color='white',fg_color='red'))
        Button2.grid(column=1,row=0)
        grid.pack(pady=10)

    pass
    def Delete(Lin,fin):
        file=open(fin,'r')
        file.readlines()
        file=open(fin,'w')
        for line in lines:
            if Lin not in line:
                file.write(line)
            pass
        pass
        file.close()
        Mountain_project_finder.resetbuttons()
        print(f'Removed Button')
    pass
    def configu():
        global tota,win
        win=win+1
        config.configure(text=wow.Name)
        config2.configure(text=f'{win}/{tota}   {round(win/tota*100)}%')
    pass
    def resetbuttons():
        global buttons
        for b in buttons:
            b.pack_forget()
        pass
        buttons=[]
        searchpybuttons=open(f'/home/{expanduser()}/.local/share/applications/MPS/Searchpybuttons.txt')
        lines=searchpybuttons.readlines()
        for line in lines:
            spl=line.split('///')
            pt=partial(Mountain_project_finder.UIthingy,spl[0],spl[2],spl[1])
            buttons.append(tk.CTkButton(fr,text=spl[0],command=pt))
        pass
        for l in buttons:
            l.pack(pady=10)
        pass
        addbutton.pack_forget()
        addbutton.pack(pady=10)
        searchpybuttons.close()
    pass
    def realadd(N,F,L):
        global variable1
        if variable1.get():
            open(F,'x').close()
            print('Creating File')
        pass
        searchpybuttons=open(f'/home/{expanduser()}/.local/share/applications/MPS/Searchpybuttons.txt','a')
        searchpybuttons.write(f'{N}///{F}///{L}\n')
        searchpybuttons.close()
        Mountain_project_finder.resetbuttons()
    pass
    def add():
        global exist,label1,grid,variable1
        if exist:
            label1.pack_forget()
            grid.pack_forget()
        pass
        exist=1
        variable1=tk.Variable(window)
        label1=tk.CTkLabel(thing,text='Enter button info')
        label1.pack(anchor='center')
        grid=tk.CTkFrame(thing,fg_color='transparent')
        grid.pack_propagate(True)
        grid.columnconfigure(0)
        NameAdd=tk.CTkEntry(grid,justify='center')
        NameAdd.grid(column=0,row=0)
        FilenameAdd=tk.CTkEntry(grid,justify='center')
        FilenameAdd.grid(column=0,row=1)
        CheckbodAdd=tk.CTkCheckBox(grid,text='New File?',variable=variable1)
        CheckbodAdd.grid(column=1,row=1)
        LinkAdd=tk.CTkEntry(grid,justify='center')
        LinkAdd.grid(column=0,row=2)
        ButtonAdd=tk.CTkButton(grid,text='Add',command=lambda: Mountain_project_finder.realadd(NameAdd.get(),FilenameAdd.get(),LinkAdd.get()))
        ButtonAdd.grid(column=0,row=3)
        NameAdd.delete(0,'end')
        FilenameAdd.delete(0,'end')
        LinkAdd.delete(0,'end')
        NameAdd.insert(0,'Name')
        FilenameAdd.insert(0,'Filename')
        LinkAdd.insert(0,'Link')
        grid.pack()
    pass
    def start():
        global exist,buttons,window,fr,searchpybuttons,lines,line,addbutton,thing
        exist=0
        buttons=[]
        window=tk.CTk()
        window.title('Mountain Project Button Editor')
        window.geometry('500x500')
        fr=tk.CTkScrollableFrame(window,height=490,width=150)
        searchpybuttons=open(f'/home/{expanduser()}/.local/share/applications/MPS/Searchpybuttons.txt','r')
        lines=searchpybuttons.readlines()
        for line in lines:
            spl=line.split('///')
            pt=partial(Mountain_project_finder.UIthingy,spl[0],spl[2],spl[1])
            buttons.append(tk.CTkButton(fr,text=spl[0],command=pt))
        pass
        for l in buttons:
            l.pack(pady=10)
        pass
        searchpybuttons.close()
        addbutton=tk.CTkButton(fr,text='[ADD BUTTON]',command=Mountain_project_finder.add)
        addbutton.pack(pady=10)
        fr.place(x=0,y=0)
        thing=tk.CTkFrame(window,width=330,height=500)
        thing.pack_propagate(False)
        thing.place(x=170,y=0)
        window.mainloop()
def route(link):
    global Nam,Gra,Ima,Ope,Stars,Disk
    if Nam:
        Nam.pack_forget()
        Gra.pack_forget()
        Disk.pack_forget()
        try:
            Ima.pack_forget()
        except:
            pass
        Ope.pack_forget()
        Stars.pack_forget()
    pass

    for line in lines:
        if link in line:
            print(line)
            rl=line
            break
        pass
    pass
    spl=line.split('///')
    Nam=tk.CTkLabel(rc,font=('arial',30),text=spl[0])
    Nam.pack(anchor='w')
    Gra=tk.CTkLabel(rc,font=('arial',25),text=spl[1])
    Gra.pack(anchor='w')
    Stars=tk.CTkLabel(rc,font=('arial',15),text=f'stars: {spl[3]}')
    Stars.pack(anchor='w')

    try:
        imlin=spl[4]
        img=imagefromweb.WebImage(imlin)
        Ima=tk.CTkLabel(rc,image=tk.CTkImage(img.image,size=(img.width,img.height)),text=None)
        Ima.bind('<Button-1>',lambda event:img.OpenInWindow())
        Ima.pack(anchor='w',padx=10)
    except:
        print('No Picture     x_x')
        pass
    Disk=tk.CTkLabel(rc,font=('arial',15),text=spl[6],justify='left',wraplength=320)
    Disk.pack(anchor='w',pady=20)
    Ope=tk.CTkButton(rc,text='Open Link',command= lambda: webbrowser.open(spl[2]))
    Ope.pack(anchor='sw')
pass
def thing(filetoopen):
    global spl,lines,sf,rc,thin
    file=open(filetoopen,'r')
    lines=file.readlines()
    scrol.place_forget()
    GradeFilter.place_forget()
    StarFilter.place_forget()
    NameFilter.place_forget()
    TypeFilter.place_forget()
    StyleFilter.place_forget()
    FAFilter.place_forget()
    res.place_forget()


    sf=tk.CTkScrollableFrame(window,height=500,width=150)
    sf.place(x=0,y=0)
    rc=tk.CTkScrollableFrame(window,height=490,width=310)
    rc.place(x=170,y=0)
    thin=[]
    Coollabel=tk.CTkLabel(sf,text='')
    Coollabel.pack(anchor='w')
    for line in lines:

        spl=line.split('///')
        doo=spl[2].replace('\n','')
        gf=GradeFilter.get()
        sta=StarFilter.get()
        Namef=NameFilter.get().lower()
        Ty=TypeFilter.get()
        sty=StyleFilter.get().lower()
        FiA=FAFilter.get().lower()
        Sha=ShaFilter.get().lower()
        if gf=='Grade Filter' or gf=='':
            gf=spl[1]
        if sta=='Star Filter' or sta=='':
            sta=spl[3]
        if Namef=='name filter':
            Namef=''
        if Ty=='Type Filter':
            Ty=''
        if sty=='style filter':
            sty=''
        if FiA=='fa filter':
            FiA=''
        if Sha=='shared by filter':
            Sha=''
        if spl[1]==gf and spl[3]==sta and Namef in spl[0].lower() and Ty in spl[5] and sty in spl[6].lower() and FiA in spl[7].lower() and Sha in spl[8].lower():
            print(doo)
            dee=partial(route,doo)
            ke=tk.CTkButton(sf,text=spl[0],command=dee)
            thin.append(ke)
            ke.pack(anchor='w',pady=5)
    Coollabel.configure(text=f'{len(thin)} Routes')
    pass
    tk.CTkButton(sf,text='[BACK]',command=back).pack(anchor='w')
    file.close()
pass
def reset():
    global fel
    GradeFilter.delete(0,'end')
    StarFilter.delete(0,'end')
    NameFilter.delete(0,'end')
    TypeFilter.delete(0,'end')
    StyleFilter.delete(0,'end')
    FAFilter.delete(0,'end')
    ShaFilter.delete(0,'end')
    GradeFilter.insert(0,'Grade Filter')
    StarFilter.insert(0,'Star Filter')
    NameFilter.insert(0,'Name Filter')
    TypeFilter.insert(0,'Type Filter')
    StyleFilter.insert(0,'Style Filter')
    FAFilter.insert(0,'FA Filter')
    ShaFilter.insert(0,'Shared By Filter')
    for item in fel:
        item.pack_forget()
    pass
    addbutton.pack_forget()
    doohickey=open(f'/home/{expanduser()}/.local/share/applications/MPS/Searchpybuttons.txt')
    searchpybuttons=doohickey.readlines()
    for line in searchpybuttons:
        splia=line.split('///')
        wowee=partial(thing,splia[1].replace('\n',''))
        hick=tk.CTkButton(scrol,text=splia[0],command=wowee)
        fel.append(hick)
        hick.pack(anchor='w',pady=10)
    addbutton.pack(pady=10)
    window.geometry('500x500')
def back():
    for item in thin:
        item.destroy()
    sf.place_forget()
    rc.place_forget()
    scrol.place(x=0,y=0)
    GradeFilter.place(x=300,y=20)
    StarFilter.place(x=300,y=60)
    NameFilter.place(x=300,y=100)
    TypeFilter.place(x=300,y=140)
    StyleFilter.place(x=300,y=180)
    FAFilter.place(x=300,y=220)
    ShaFilter.place(x=300,y=260)
    res.place(x=450,y=470)
    if Nam:
        Nam.pack_forget()
        Gra.pack_forget()
        Ima.pack_forget()
        Ope.pack_forget()
    pass
doohickey=open(f'/home/{expanduser()}/.local/share/applications/MPS/Searchpybuttons.txt')
searchpybuttons=doohickey.readlines()
window=tk.CTk()
window.title('Mountain Project Search')
window.geometry('500x500')
scrol=tk.CTkScrollableFrame(window,width=150,height=490)
scrol.place(x=0,y=0)
fel=[]
for line in searchpybuttons:
    splia=line.split('///')
    wowee=partial(thing,splia[1].replace('\n',''))
    hick=tk.CTkButton(scrol,text=splia[0],command=wowee)
    fel.append(hick)
    hick.pack(anchor='w',pady=10)
addbutton=tk.CTkButton(scrol,text='[EDIT]',command=Mountain_project_finder.start)
addbutton.pack(pady=10)
GradeFilter=tk.CTkEntry(window,justify='center')
GradeFilter.insert(0,'Grade Filter')
GradeFilter.place(x=300,y=20)
StarFilter=tk.CTkEntry(window,justify='center')
StarFilter.insert(0,'Star Filter')
StarFilter.place(x=300,y=60)
NameFilter=tk.CTkEntry(window,justify='center')
NameFilter.insert(0,'Name Filter')
NameFilter.place(x=300,y=100)
TypeFilter=tk.CTkEntry(window,justify='center')
TypeFilter.insert(0,'Type Filter')
TypeFilter.place(x=300,y=140)
StyleFilter=tk.CTkEntry(window,justify='center')
StyleFilter.insert(0,'Style Filter')
StyleFilter.place(x=300,y=180)
FAFilter=tk.CTkEntry(window,justify='center')
FAFilter.insert(0,'FA Filter')
FAFilter.place(x=300,y=220)
ShaFilter=tk.CTkEntry(window,justify='center')
ShaFilter.insert(0,'Shared By Filter')
ShaFilter.place(x=300,y=260)
res=tk.CTkButton(window,text='reset',command=reset,width=50)
res.place(x=450,y=470)
window.mainloop()

