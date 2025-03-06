toDolist=[]
def gorevEkle(toDolist):
    gorev=input("Yapılacak olan görevi giriniz:")
    toDolist.append(gorev)
    print("Görev ekleme doğru şekilde yapıldı")
def gorevGöster(toDolist):
    print("Yapılacak olan görevler")
    sırasayisi=0
    for i in toDolist:
       sırasayisi+=1
    print(sırasayisi"-"+1)
    def gorevsil(toDolist):
      gorev=input("Silinecek olan görevi giriniz:")  
      if gorev in toDolist:
       print("Görev sileme doğru şekilde yapıldı")  
      else:
         print("Görev bulunamadı"...)   
    While True:
    print("\nSeçenekler:")
    print("1. Görevleri listele")
    print("2. Bir görevi tamamlandı olarak işaretle")
    print("3. Çıkış yap")