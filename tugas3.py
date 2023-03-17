# class Persegipanjang184220007:
#     #atribut statis
#     counter = 0

#     def __init__(self,p,l):
#         #menaikan nilai atribut statis
#         Persegipanjang184220007.counter += 1
#         #atribut - atribut non-statis
#         self.panjang = p
#         self.lebar = l

#     def ubahPanjang (self,p):
#         self.panjang = p

#     def ubahLebar(self,l):
#         self.lebar = l

#     def hitungLuas(self):
#         return self.panjang * self.lebar
    
#     def hitungKeliling(self):
#         return 2 * (self.panjang + self.lebar)
    
#     def cetakLuas(self):
#         print('Luas persegi panjang = %.2f' % self.hitungLuas())

#     def cetakKeliling(self):
#         print('Keliling persegi panjang=% .2f' % self.hitungKeliling())

# #membuat objek dari persegipanjang
# kolin = Persegipanjang184220007(12, 6)
# paulina = Persegipanjang184220007(16, 8)
# olin = Persegipanjang184220007(30, 15)
# #memanggil atribut counter melalui kelas
# print(Persegipanjang184220007.counter)
# print(kolin.counter)
# olin.cetakLuas()
# kolin.cetakKeliling()
# lelah = Persegipanjang184220007(45,15)
# print(lelah.counter)
# print(Persegipanjang184220007.counter)
# print(kolin.counter, paulina.counter, lelah.counter)


# class segitiga:
#     def __init__(self,alas,tinggi):
#         self.alas = alas
#         self.tinggi = tinggi

#     def ubahAlas (self,alas):
#         self.alas = alas

#     def ubahTinggi(self,tinggi):
#         self.tinggi = tinggi

#     def hitungLuas (self):
#         return (self.alas * self.tinggi)/2
    
#     def cetakLuas (self):
#         print('luas segitiga = %.2 ' % self.hitungLuas())

# olin = segitiga(2, 5)
# olin.cetakLuas()

#no.1 mendefenisiskan 
# class persegi184220007:
#     def __init__(self,sisi):
#         #mendefenisikan atribut - atribut kelas
#         self.s = sisi
        
#     def ubahsisi(self, sisi):
#         self.s = sisi

#     def Luas(self):
#         return (self.s) ** 2
    
#     def Keliling(self):
#         return self.s * 4
    
#     def cetakluas (self):
#         print('luas persegi adalah = %.2f' % self.Luas())
    
#     def cetakkeliling(self):
#         print('keliling persegi adalah = %.2d' % self.Keliling())
# #membuat objek dari kelas persegi
# itu = persegi184220007(4)
# #memanggil objek dari kelas persegi
# itu.cetakluas()
# itu.cetakkeliling()
# print()

# iti = persegi184220007(8)
# iti.cetakluas()
# iti.cetakkeliling()

# class persegi184220007:
#     def __init__(self,sisi):
#         #mendefenisikan atribut - atribut kelas
#         self.s = sisi

#     def Luas(self):
#         return self.s ** 2
    
# lali = persegi184220007(8)
# lila =persegi184220007(6)
# print(lali.Luas())
# print(lila.Luas())

# #metode Statis
# class Aritmatika:
#     @staticmethod
#     def penjumlahan(x, y):
#         return x + y
    
#     @staticmethod
#     def pengurangan(x, y):
#         return x - y
    
#     @staticmethod
#     def perkalian(x, y):
#         return x * y
    
#     @staticmethod
#     def pembagian(x, y):
#         return x / y
    
#     @staticmethod
#     def bagi(x, y):
#         return x // y
    
#     @staticmethod
#     def sisabagi(x, y):
#         return x % y
    
#     @staticmethod
#     def pangkat (x, y):
#         return x ** y
    
# print(Aritmatika.penjumlahan(465, 837))
# print(Aritmatika.pengurangan(852, 388))
# print(Aritmatika.perkalian(37, 28))
# print(Aritmatika.pembagian(863, 3))
# print(Aritmatika.bagi(957, 32))
# print(Aritmatika.sisabagi(784, 2))
# print(Aritmatika.pangkat(63, 7))

# kolin = Aritmatika()
# print(kolin.penjumlahan(347, 735))
# print(kolin.perkalian(74, 7476))

# #pewaris
# #membuat kelas turunan dari kelas list
# class Stringlist07(list):
#     def __init__(self):
#         self.data = []

#     def __repr__(self):
#         return str(self.data)
#     #ovveride metode append()
#     def append(self, objek):
#         if not isinstance(objek, str):
#             raise TypeError('objek harus bertipe string')
#         self.data.append(objek)

#     #override metode insert()
#     def insert(self,indeks,objek):
#         if indeks >= len(self.data) or \
#                 indeks <- len(self.data):
#             raise IndexError('indeks diluar rentang')
#         if not isinstance(objek, str):
#             #override metode append()
#             raise TypeError('objek harus bertipe string')
    
#         self.data.insert(indeks,objek)

# #membuat objek dari kelas stringlist07
# lisa = Stringlist07()
# #membuat data menggunakan metode append
# lisa.append('matahati')
# lisa.append('malam')
# lisa.append('indah')
# print(lisa)
# #menambahkan data menggunakan metode insert()
# lisa.insert(1, 'terbit')
# lisa.insert(-2, 'senja')
# print(lisa)
# lisa.append('terbenam')
# print(lisa)
# print()
# lisa.append(99)
# print(lisa)
# lisa.insert(3,897)  
# print(lisa)
# lisa.insert(-9,'terbenam')
# print(lisa)

# #metode abstrak dan kelas abstrak
# from abc import ABCMeta, abstractmethod
# #kelas abstrak
# class Duadimensi(metaclass=ABCMeta):
#     @abstractmethod
#     def luas (self):
#         pass

# #kelas segi empat turun dari kelas duadimensi
# class segiempat(Duadimensi):
#     def __init__(self, panjang, lebar):
#         self.p = panjang
#         self.l = lebar
#     #mengimplementasikan metode luas ()
#     def luas(self):
#         return self.p * self.l
# #kelas segitiga turun dari kelas duadimensi
# class segitiga(Duadimensi):
#     def __init__(self, a, t):
#         self.alas = a
#         self.tinggi = t
#     #mengimplementasikan metode luas()
#     def luas(self):
#         return (self.alas * self.tinggi)/2
# #kelas turunan dari kelas duadimensi
# class lingkaran(Duadimensi):
#     def __init__(self, r):
#         self.radius = r
#     #mengimplementasikan metode luas()
#     def luas(self):
#         import math
#         return math.pi*(self.radius**2)
      
# olin = segiempat(45, 10).luas()
# print(olin)
# eni = segiempat(34, 85)
# eni.luas()
# print(eni)
# ida = segitiga(5, 20).luas()
# print(ida)
# indi = lingkaran(250).luas()
# print(indi)

# #polinomeis
# from abc import ABCMeta, abstractmethod
# #kelas abstrak
# class Duadimensi(metaclass=ABCMeta):
#     @abstractmethod
#     def luas (self):
#         pass
# #kelas segi empat turun dari kelas duadimensi
# class segiempat(Duadimensi):
#     def __init__(self, panjang, lebar):
#         self.p = panjang
#         self.l = lebar
#     #mengimplementasikan metode luas ()
#     def luas(self):
#         return self.p * self.l
# #kelas segitiga turun dari kelas duadimensi
# class segitiga(Duadimensi):
#     def __init__(self, a, t):
#         self.alas = a
#         self.tinggi = t
#     #mengimplementasikan metode luas()
#     def luas(self):
#         return (self.alas * self.tinggi)/2
# #kelas turunan dari kelas duadimensi
# class lingkaran(Duadimensi):
#     def __init__(self, r):
#         self.radius = r
#     #mengimplementasikan metode luas()
#     def luas(self):
#         import math
#         return math.pi*(self.radius**2)
# #memuat list kosong
# List1 = []
# print(List1)
# #menambahkan objek segiempat kedalam list
# List1.append(segiempat(21,9))
# List1.append(segiempat(8,3))

# #menambahkan objek segitiga kedalam list
# List1.append(segitiga(20,30))

# #menambahkan Objek lingkaran kedalam list
# List1.append(lingkaran(9))

# #menelusuri seluruah elemen list dan memanggil metode luas
# for kolin in List1:
#     if not issubclass (kolin.__class__, Duadimensi):
#         raise TypeError ('Objek harus turunan Duadimensi')
#     if isinstance (kolin, segiempat):
#         print('luas segiempat = ', end='')
#     elif isinstance(kolin, segitiga):
#         print('luas segitiga = ', end='')
#     else:
#         print('luas lingkaran = ', end='')
#     print(kolin.luas())

# def print_details(kolin):
#     print("tipe objek = ", type(kolin))
#     print('panjang objek = ', len(kolin))
#     print('isi objek = ', kolin)

# print_details('indah,elok,permai,suci')
# print_details([1,2,3,6,7,8,9,8])
# print_details({"nama":'olin', "asal":'flores'})

    # def __init__(self,nama,asal,jurusan):
    #     self.nama = nama
    #     self.asal = asal
    #     self.jurusan = jurusan

# def detail(nama,asal,jurusan):
#     return(f'saya {nama} asal dari {asal} jurusan {jurusan}')

# print(detail('olin', 'flores', 'sains data'))
# print(detail('maysa','denpasar','sains data'))
# print(detail('siti','tasikmalaya','manajemen logistik'))
# print(detail('silva','bogor','manajemen bisnis'))

# def detail(nama,asal,jurusan):
#     print('nama saya = ',nama)
#     print('asal dari = ',asal)
#     print('jurusan = ',jurusan)

# print(detail('olin', 'flores', 'sains data'))
# print(detail('maysa','denpasar','sains data'))
# print(detail('siti','tasikmalaya','manajemen logistik'))
# print(detail('silva','bogor','manajemen bisnis'))

# from abc import ABC, abstractmethod

# class pagi(ABC):
#     @abstractmethod
#     def suara(self):
#         pass

# class kucing(pagi):
#     def suara(self):
#         return ('itu bagus')
    
# class beruang(pagi):
#     def suara(self):
#         return('cantik sekali')


# kolin = beruang().suara()
# print(kolin)

# ida = kucing().suara()
# print(ida)
    
#POLIMORFISME
class kucing():
    def __init__(self,nama):
        self.nama = nama
    
    def lengkap(self):
        return(f'nama saya {self.nama}')
    
class singa():
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
    
    def lengkap(self):
        return(f'nama saya {self.nama} umur {self.umur}')
    
p1 = kucing('lala')
p2 = singa('kasa','3 bulan')

for loli in (p1,p2):
    print(loli.lengkap())

def popo (kuku):
    print(kuku.lengkap())

popo(p1)
popo(p2)

class tiruanlist(list):
    def append(self):
        return 'berhasil'
    
mylist = tiruanlist()
print(mylist.append())

k = list()
k.append(3)
k.append(popo(p1))
k.append('lala')
print(k)
popo(p1)


# class mahasiswa():
#     #atributstatis
#     universitas = True
#     prodi = "sains data"

#     def __init__ (self,nama,asal):
#         #atributdinamis
#         self.nama = nama
#         self.asal = asal
#         print(f'nama saya {self.nama} berasal dari{self.asal} ')
# #membuat objek
# cin = mahasiswa('cintany','manggarai')
# sal = mahasiswa('caca','purwokerto')
# #memanggil objek
# print(cin.universitas, sal.prodi)
# print(cin.nama, sal.nama)
# print(cin.asal, sal.asal)

        

