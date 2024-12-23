KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):

        self.kapasiteetti = self.check_list_parameter(kapasiteetti, "Kapasiteetti")
        self.kasvatuskoko = self.check_list_parameter(kasvatuskoko, "Kasvatuskoko")

        self.ljono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def check_list_parameter(self, param, param_type=str):
        if param is None:
            if param_type == "Kapasiteetti":
                return KAPASITEETTI
            return OLETUSKASVATUS
        elif not isinstance(param, int) or param < 0:
            raise Exception(f"{param_type} ei ole numero, tai se on negatiivinen!")
        return param

    def kuuluu(self, element):

        for i in range(0, self.alkioiden_lkm):
            if element == self.ljono[i]:
                return True
        return False

    def lisaa(self, element):
        if self.alkioiden_lkm == 0:
            self.ljono[0] = element
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True
        else:
            pass

        if not self.kuuluu(element):
            self.ljono[self.alkioiden_lkm] = element
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm % len(self.ljono) == 0:
                self.create_new_space()
                return True

        return False

    def create_new_space(self):
        taulukko_old = self.ljono
        self.kopioi_lista(self.ljono, taulukko_old)
        self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_lista(taulukko_old, self.ljono)

    def poista(self, element):
        index_to_delete = -1
        index_to_delete = self.find_index(element)
        if index_to_delete == None:
            return False

        self.ljono[index_to_delete] = 0
        self.move_elements(index_to_delete)
        return True

    def find_index(self, element):
        for i in range(0, self.alkioiden_lkm):
            if element == self.ljono[i]:
                return i
        return None

    def move_elements(self, start):
        for j in range(start, self.alkioiden_lkm - 1):
            tmp_value = self.ljono[j]
            self.ljono[j] = self.ljono[j + 1]
            self.ljono[j + 1] = tmp_value

        self.alkioiden_lkm = self.alkioiden_lkm - 1

    def kopioi_lista(self, original_list, new_list):
        for i in range(0, len(original_list)):
            new_list[i] = original_list[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(first_table, second_table):
        result_table = IntJoukko()
        ensimmainen_taulu = first_table.to_int_list()
        toinen_taulu = second_table.to_int_list()

        for i in range(0, len(ensimmainen_taulu)):
            result_table.lisaa(ensimmainen_taulu[i])

        for i in range(0, len(toinen_taulu)):
            result_table.lisaa(toinen_taulu[i])

        return result_table

    @staticmethod
    def leikkaus(first_table, second_table):
        result_table = IntJoukko()
        ensimmainen_taulu = first_table.to_int_list()
        toinen_taulu = second_table.to_int_list()

        for i in range(0, len(ensimmainen_taulu)):
            for j in range(0, len(toinen_taulu)):
                if ensimmainen_taulu[i] == toinen_taulu[j]:
                    result_table.lisaa(toinen_taulu[j])

        return result_table

    @staticmethod
    def erotus(first_table, second_table):
        result_table = IntJoukko()
        ensimmainen_taulu = first_table.to_int_list()
        toinen_taulu = second_table.to_int_list()

        for i in range(0, len(ensimmainen_taulu)):
            result_table.lisaa(ensimmainen_taulu[i])

        for i in range(0, len(toinen_taulu)):
            result_table.poista(toinen_taulu[i])

        return result_table

    def generate_string(self):
        tuotos = "{"
        for i in range(0, self.alkioiden_lkm - 1):
            tuotos = tuotos + str(self.ljono[i])
            tuotos = tuotos + ", "
        tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
        tuotos = tuotos + "}"
        return tuotos

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            return self.generate_string()
