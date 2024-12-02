print("perpustakaan")
class Person:
    def _init_(self, nama, alamat):
        # Enkapsulasi: atribut nama dan alamat disimpan sebagai privat
        self.__nama = nama
        self.__alamat = alamat

    # Getter untuk nama
    def get_nama(self):
        return self.__nama

    # Setter untuk nama
    def set_nama(self, nama):
        self.__nama = nama

    # Getter untuk alamat
    def get_alamat(self):
        return self.__alamat

    # Setter untuk alamat
    def set_alamat(self, alamat):
        self.__alamat = alamat

    # Metode untuk menampilkan informasi dasar
    def tampilkan_info(self):
        return f"Nama: {self._nama}, Alamat: {self._alamat}"


class Anggota(Person):
    def _init_(self, nama, alamat, id_anggota):
        # Pewarisan: memanggil konstruktor kelas dasar (Person)
        super()._init_(nama, alamat)
        self.__id_anggota = id_anggota
        self.__buku_dipinjam = []  # Daftar buku yang dipinjam

    # Getter untuk id_anggota
    def get_id_anggota(self):
        return self.__id_anggota

    # Metode untuk meminjam buku
    def pinjam_buku(self, buku):
        self.__buku_dipinjam.append(buku)

    # Metode untuk mengembalikan buku
    def kembalikan_buku(self, buku):
        if buku in self.__buku_dipinjam:
            self.__buku_dipinjam.remove(buku)

    # Polimorfisme: mengoverride metode tampilkan_info
    def tampilkan_info(self):
        info = super().tampilkan_info()  # Memanggil metode dari kelas dasar
        buku_list = ', '.join([buku.tampilkan_info() for buku in self.__buku_dipinjam])
        return f"{info}, ID Anggota: {self.__id_anggota}, Buku Dipinjam: [{buku_list}]"


class Buku:
    def _init_(self, judul, penulis, tahun_terbit):
        # Enkapsulasi: atribut judul, penulis, dan tahun terbit disimpan sebagai privat
        self.__judul = judul
        self.__penulis = penulis
        self.__tahun_terbit = tahun_terbit
        self.__tersedia = True  # Status ketersediaan buku

    # Getter untuk judul
    def get_judul(self):
        return self.__judul

    # Setter untuk judul
    def set_judul(self, judul):
        self.__judul = judul

    # Getter untuk penulis
    def get_penulis(self):
        return self.__penulis

    # Setter untuk penulis
    def set_penulis(self, penulis):
        self.__penulis = penulis

    # Getter untuk tahun terbit
    def get_tahun_terbit(self):
        return self.__tahun_terbit

    # Setter untuk tahun terbit
    def set_tahun_terbit(self, tahun_terbit):
        self.__tahun_terbit = tahun_terbit

    # Metode untuk memeriksa ketersediaan buku
    def is_tersedia(self):
        return self.__tersedia

    # Metode untuk meminjam buku
    def pinjam(self):
        self.__tersedia = False

    # Metode untuk mengembalikan buku
    def kembalikan(self):
        self.__tersedia = True

    # Metode untuk menampilkan informasi buku
    def tampilkan_info(self):
        return f"Judul: {self._judul}, Penulis: {self.penulis}, Tahun Terbit: {self.tahun_terbit}, Tersedia: {'Ya' if self._tersedia else 'Tidak'}"


class SistemPerpustakaan:
    def _init_(self):
        self.__anggota_list = []  # Daftar anggota
        self.__buku_list = []      # Daftar buku

    # Metode untuk menambah anggota
    def tambah_anggota(self, anggota):
        self.__anggota_list.append(anggota)

    # Metode untuk menghapus anggota
    def hapus_anggota(self, id_anggota):
        self._anggota_list = [anggota for anggota in self._anggota_list if anggota.get_id_anggota() != id_anggota]

        # Metode untuk menambah buku
    def tambah_buku(self, buku):
        self.__buku_list.append(buku)

    # Metode untuk menghapus buku
    def hapus_buku(self, judul_buku):
        self._buku_list = [buku for buku in self._buku_list if buku.get_judul() != judul_buku]

    # Metode untuk menampilkan daftar anggota
    def tampilkan_anggota(self):
        for anggota in self.__anggota_list:
            print(anggota.tampilkan_info())

    # Metode untuk menampilkan daftar buku
    def tampilkan_buku(self):
        for buku in self.__buku_list:
            print(buku.tampilkan_info())

    # Metode untuk meminjam buku
    def pinjam_buku(self, id_anggota, judul_buku):
        anggota = next((anggota for anggota in self.__anggota_list if anggota.get_id_anggota() == id_anggota), None)
        buku = next((buku for buku in self.__buku_list if buku.get_judul() == judul_buku), None)

        if anggota and buku and buku.is_tersedia():
            anggota.pinjam_buku(buku)
            buku.pinjam()  # Menandai buku sebagai tidak tersedia
            print(f"Buku '{judul_buku}' berhasil dipinjam oleh {anggota.get_nama()}.")
        else:
            print("Peminjaman gagal. Pastikan anggota dan buku tersedia.")

    # Metode untuk mengembalikan buku
    def kembalikan_buku(self, id_anggota, judul_buku):
        anggota = next((anggota for anggota in self.__anggota_list if anggota.get_id_anggota() == id_anggota), None)
        buku = next((buku for buku in self.__buku_list if buku.get_judul() == judul_buku), None)

        if anggota and buku:
            anggota.kembalikan_buku(buku)
            buku.kembalikan()  # Menandai buku sebagai tersedia
            print(f"Buku '{judul_buku}' berhasil dikembalikan oleh {anggota.get_nama()}.")
        else:
            print("Pengembalian gagal. Pastikan anggota dan buku valid.")


# Contoh penggunaan
if _name_ == "_main_":
    # Membuat sistem perpustakaan
    sistem = SistemPerpustakaan()

    # Menambah anggota
    anggota1 = Anggota("Alice", "Jl. Mawar No. 1", "A001")
    anggota2 = Anggota("Bob", "Jl. Melati No. 2", "A002")
    sistem.tambah_anggota(anggota1)
    sistem.tambah_anggota(anggota2)

    # Menambah buku
    buku1 = Buku("Belajar Python", "John Doe", 2020)
    buku2 = Buku("Pemrograman OOP", "Jane Smith", 2021)
    sistem.tambah_buku(buku1)
    sistem.tambah_buku(buku2)

    # Menampilkan anggota dan buku
    print("Daftar Anggota:")
    sistem.tampilkan_anggota()
    print("\nDaftar Buku:")
    sistem.tampilkan_buku()

    # Meminjam dan mengembalikan buku
    sistem.pinjam_buku("A001", "Belajar Python")
    sistem.kembalikan_buku("A001", "Belajar Python")

    # Menampilkan informasi setelah peminjaman dan pengembalian
    print("\nDaftar Anggota setelah peminjaman:")
    sistem.tampilkan_anggota()
    print("\nDaftar Buku setelah peminjaman:")
    sistem.tampilkan_buku()
