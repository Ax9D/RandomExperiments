import os;
 
def unzip(n):
    while(n!=""):
        comex("unzip "+'"'+n+'"');
        n=n[0:len(n)-2];
     
     
def comex(x):
    os.system(x);
    

unzip("password.x.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.a.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p");
