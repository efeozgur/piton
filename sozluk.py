#coding: utf-8
import sqlite3 as sql 


baglan = sql.connect("sozluk.sqlite3")
im = sql.Cursor(baglan)

def kayitEkle(komut, tanim, kullanim):
    im.execute("insert into sozluk values (?,?,?)", (komut, tanim, kullanim))
    baglan.commit()
    baglan.close()
    print("Kayıt Yapıldı...!!!")

def kayitOku (komut):    
    veri = im.execute("select * from sozluk where komut='"+komut+"'")        
    for i,j,x in veri:
        print (i + "\t" + j + u"\nKullanımı =>  " + x)
        print("-"*25 + "by:Efe Özgür" + "-"*25)
    baglan.close()


#kayitEkle(komut="sqlite3", tanim="veritabanı modülüdür",kullanim="""sqlite3.connect('baglan.sqlite3')""")
#kayitOku("sqlite3")
