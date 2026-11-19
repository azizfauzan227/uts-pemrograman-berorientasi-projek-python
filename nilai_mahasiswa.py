class matakuliah:
    def __init__(self, nama_mk, nilai):
        self.nama_mk = nama_mk
        self.__nilai = nilai

    @property
    def nilai(self):
        return self.__nilai

    @nilai.setter
    def nilai(self, angka):
        if 0 <= angka <= 100:
            self.__nilai = angka
        else:
            print("Nilai harus 0 - 100")

    @staticmethod
    def cek_grade(angka):
        if angka >= 85:
            return "A"
        elif angka >= 70:
            return "B"
        elif angka >= 55:
            return "C"
        else:
            return "D"


class mahasiswa:
    jumlah_mahasiswa = 0
    total_nilai = 0.0

    def __init__(self, nama, nim, mk):
        self.nama = nama
        self.nim = nim
        self.__mk = mk
        mahasiswa.jumlah_mahasiswa += 1
        mahasiswa.total_nilai += float(self.__mk.nilai)

    def info(self):
        grade = matakuliah.cek_grade(self.__mk.nilai)
        return f"{self.nama} ({self.nim}) - {self.__mk.nama_mk}: {self.__mk.nilai} ({grade})"

    @classmethod
    def jumlah(cls):
        return f"Jumlah mahasiswa: {cls.jumlah_mahasiswa}"

    @classmethod
    def rata_nilai(cls):
        return f"Rata-rata nilai mahasiswa: {cls.total_nilai / cls.jumlah_mahasiswa:.2f}"


mk1 = matakuliah("Python", 85)
mk2 = matakuliah("Basis Data", 70)
mk3 = matakuliah("Jaringan", 90)

mk2.nilai = 78

rina = mahasiswa("rina", 101, mk1)
riko = mahasiswa("riko", 102, mk2)
rizki = mahasiswa("rizki", 103, mk3)

print(rina.info())
print(riko.info())
print(rizki.info())
print(mahasiswa.jumlah())
print(mahasiswa.rata_nilai())