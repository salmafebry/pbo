print("perpustakaan")
class Person:
    def _init_(self, nama, alamat):
        self.__nama = nama
        self.__alamat = alamat

    def get_nama(self):
        return self.__nama

    def get_alamat(self):
        return self.__alamat

    def tampilkan_info(self):
        return f"Nama: {self._nama}, Alamat: {self._alamat}"


class Anggota(Person):
    def _init_(self, nama, alamat, id_anggota):
        super()._init_(nama, alamat)
        self.__id_anggota = id_anggota
        self.__buku_dipinjam = []

    def pinjam_buku(self, buku):
        self.__buku_dipinjam.append(buku)

    def kembalikan_buku(self, buku):
        if buku in self.__buku_dipinjam:
            self.__buku_dipinjam.remove(buku)

    def tampilkan_info(self):
        info = super().tampilkan_info()
        buku_list = ', '.join([buku.tampilkan_info() for buku in self.__buku_dipinjam])
        return f"{info}, ID Anggota: {self.__id_anggota}, Buku Dipinjam: [{buku_list}]"


class Buku:
    def _init_(self, judul, penulis, tahun_terbit):
        self.__judul = judul
        self.__penulis = penulis
        self.__tahun_terbit = tahun_terbit
        self.__tersedia = True

    def is_tersedia(self):
        return self.__tersedia

    def pinjam(self):
        self.__tersedia = False

    def kembalikan(self):
        self.__tersedia = True

    def tampilkan_info(self):
        return f"Judul: {self._judul}, Penulis: {self.penulis}, Tahun Terbit: {self.tahun_terbit}, Tersedia: {'Ya' if self._tersedia else 'Tidak'}"


class SistemPerpustakaan:
    def _init_(self):
        self.__anggota_list = []
        self.__buku_list = []

    def tambah_anggota(self, anggota):
        self.__anggota_list.append(anggota)

    def tambah_buku(self, buku):
        self.__buku_list.append(buku)

    def pinjam_buku(self, id_anggota, judul_buku):
        anggota = next((a for a in self.__anggota_list if a.get_id_anggota() == id_anggota), None)
        buku = next((b for b in self.__buku_list if b.tampilkan_info().startswith(f"Judul: {judul_buku}")), None)

        if anggota and buku and buku.is_tersedia():
            anggota.pinjam_buku(buku)
            buku.pinjam()
            print(f"{anggota.get_nama()} berhasil meminjam buku '{buku.tampilkan_info()}'.")
        else:
            print("Peminjaman gagal. Pastikan anggota terdaftar dan buku tersedia.")

    def kembalikan_buku(self, id_anggota, judul_buku):
        anggota = next((a for a in self.__anggota_list if a.get_id_anggota() == id_anggota), None)
        buku = next((b for b in self.__buku_list if b.tampilkan_info().startswith(f"Judul: {judul_buku}")), None)

        if anggota and buku:
            anggota.kembalikan_buku(buku)
            buku.kembalikan()
            print(f"{anggota.get_nama()} berhasil mengembalikan buku '{buku.tampilkan_info()}'.")
        else:
            print("Pengembalian gagal.")


# Contoh penggunaan
if _name_ == "_main_":
    sistem = SistemPerpustakaan()

    # Menambahkan anggota
    anggota1 = Anggota("Alice", "Jl. A No. 1", "A001")
    sistem.tambah_anggota(anggota1)

    # Menambahkan buku
    buku1 = Buku("Belajar Python", "John Doe", 2020)
    sistem.tambah_buku(buku1)

    # Menampilkan informasi anggota dan buku
    print(anggota1.tampilkan_info())
    print(buku1.tampilkan_info())

    # Meminjam buku
    sistem.pinjam_buku("A001", "Belajar Python")

    # Mengembalikan buku
    sistem.kembalikan_buku("A001", "Belajar Python")
