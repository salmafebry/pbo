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
        # Memanggil konstruktor kelas dasar (Person)
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
        self._anggota_list = [anggota for anggota in self.anggota_list if anggota.get_id
