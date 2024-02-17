


class Library:
     def __init__(self):
       self.dosya = open("books.txt", 'a+')
       
     def __del__ (self):
        self.dosya.close()
        
     def add_books(self):
       while True:
        self.title=input("Please enter the book title:")
        if not self.title:
           print("Book title cannot be empty. Please try again.")
           continue
        self.author=input("Please enter the author:")
        if not self.author:
            print("Author cannot be empty. Please try again.")
            continue
        self.year=input("Please enter the release year:")
        if not self.year:
            print("Release year cannot be empty. Please try again.")
            continue 
        from datetime import datetime
        now = datetime.now()
        try:
         self.year = int(self.year)
         if self.year < 868: #Ýlk kitap 868 yýlýnda yazýldýðý için 868 den küçük olamaz :)
            raise ValueError("Release year can not be earlier than 868.'First book released in 868 :)'")
         elif self.year > datetime.now().year: #Kitap yýlý þu anki yýldan daha büyük bir deðer alamaz
            raise ValueError("Release year can not be in the future.")
        except ValueError as ve:
         print("Error:", ve)
         print("The book could not be added to the library")
         continue
        self.pages=input("Please enter the number of pages:")
        if not self.pages:
             print("Number of pages cannot be empty. Please try again.")
             continue
        try:
            self.pages = int(self.pages)
            if self.pages <= 0:
                raise ValueError("Number of pages must be greater than 0.")
        except ValueError as ve:
            print("Error:", ve)
            print("The book could not be added to the library")
            continue
        string = f"{self.title},{self.author},{self.year},{self.pages}"
        with open("books.txt","a") as dosya:
         if dosya.tell()==0:
           dosya.write(string)
         else:
          dosya.write("\n"+string)
         print("The book has been successfully added to the library")
         break
        
        
     def list_books(self):
        with open("books.txt", "r") as file:
         string2 = file.read().splitlines()
         if not string2: #Dosya okununca stringe atýyoruz. Eðer string boþ ise kütüphanede hiçbir kitap yok demektir.
           print("There is no book in library!\n")
         else:
          gosterilecek_bilgiler = [line.split(",") for line in string2] #Kitaplarý listelerken sadece kitap adý ve yazar adýný göstermek için stringi virgül ile ayýrýp 0 ve 1. bilgileri ekrana yazdýrýyoruz. (ilk iki bilgi yani iistenen deðerler oluyor)
          for book_info in gosterilecek_bilgiler:
           print(f"Book:{book_info[0]} , Author:{book_info[1]}")
          
     def remove_books(self):
         silinecek_kitap=input("Please enter the book title which you want to delete:")
         with open("books.txt", "r") as file:
          lines = file.readlines()
         indeks = None
         for i, line in enumerate(lines): #Silinecek kitabýn hangi satýrda olduðunu bulmak için
          if silinecek_kitap in line:
            indeks = i
            break
         if indeks is not None:
          value=1
          del lines[indeks]  # Silinecek kitabýn olduðu satýrý kaldýr
          with open("books.txt", "w") as file:
           pass  # Dosyanýn içini tamamen silmek için

          with open("books.txt", "w") as file:
            for line in lines:
                file.write(line)  # Dosyayayý tekrardan silinen kitap dýþýnda yazdýrma
          print("The book has been successfully deleted from the library!")
                        
lib=Library()
while True:
 print("\n*****MENU*****")
 print("1) List Books")
 print("2) Add Book")
 print("3) Remove Book")
 print("4) Quit")
 print("**************")
 choice=input("Enter your choice (1-4):")
 if choice=="1":
  lib.list_books()
 elif choice=="2":
  lib.add_books()
 elif choice=="3":
  lib.remove_books()
 elif choice=="4":
  break
 else:
   print("You entered wrong digit. You can choice (1-4). Please try again\n")
