from string import ascii_uppercase as alfabet

data_rotor = {
    "I": ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),
    "II": ("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
    "III": ("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
}

reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

plugboard = {
    "V": "H", "H": "V",
    "G": "K", "K": "G",
    "O": "X", "X": "O"
}

urutan_rotor = ["I", "III", "II"]

ring_setting = [
    alfabet.index("D"),
    alfabet.index("T"),
    alfabet.index("Z")
]

posisi_awal = [
    alfabet.index("F"),
    alfabet.index("T"),
    alfabet.index("B")
]

ciphertext = "XOVGHFPUQVPEIEZZVEXLQEPXHZMTIZJUCTHDTHFZXOK"

informasi_rotor = []

for nama_rotor in urutan_rotor:
    wiring, huruf_notch = data_rotor[nama_rotor]

    jalur_maju = [alfabet.index(h) for h in wiring]
    jalur_mundur = [0] * 26

    for indeks, tujuan in enumerate(jalur_maju):
        jalur_mundur[tujuan] = indeks

    informasi_rotor.append((jalur_maju, jalur_mundur, alfabet.index(huruf_notch)))


def tukar_plugboard(huruf):
    return plugboard.get(huruf, huruf)


def putar_rotor(posisi):
    rotor_kanan, rotor_tengah, rotor_kiri = posisi

    kanan_di_notch = rotor_kanan == informasi_rotor[0][2]
    tengah_di_notch = rotor_tengah == informasi_rotor[1][2]

    if tengah_di_notch:
        rotor_kiri = (rotor_kiri + 1) % 26
        rotor_tengah = (rotor_tengah + 1) % 26
    elif kanan_di_notch:
        rotor_tengah = (rotor_tengah + 1) % 26

    rotor_kanan = (rotor_kanan + 1) % 26

    return [rotor_kanan, rotor_tengah, rotor_kiri]


def dekripsi_enigma(teks):
    posisi_rotor = posisi_awal[:]
    hasil = ""

    for huruf in teks:
        posisi_rotor = putar_rotor(posisi_rotor)

        huruf = tukar_plugboard(huruf)
        indeks_huruf = alfabet.index(huruf)

        for nomor_rotor in range(3):
            jalur_maju, jalur_mundur, notch = informasi_rotor[nomor_rotor]

            indeks_huruf = (indeks_huruf + posisi_rotor[nomor_rotor] - ring_setting[nomor_rotor]) % 26
            indeks_huruf = jalur_maju[indeks_huruf]
            indeks_huruf = (indeks_huruf - posisi_rotor[nomor_rotor] + ring_setting[nomor_rotor]) % 26

        indeks_huruf = alfabet.index(reflector[indeks_huruf])

        for nomor_rotor in [2, 1, 0]:
            jalur_maju, jalur_mundur, notch = informasi_rotor[nomor_rotor]

            indeks_huruf = (indeks_huruf + posisi_rotor[nomor_rotor] - ring_setting[nomor_rotor]) % 26
            indeks_huruf = jalur_mundur[indeks_huruf]
            indeks_huruf = (indeks_huruf - posisi_rotor[nomor_rotor] + ring_setting[nomor_rotor]) % 26

        hasil += tukar_plugboard(alfabet[indeks_huruf])

    return hasil


print("=== HASIL DEKRIPSI ENIGMA ===")
print(dekripsi_enigma(ciphertext))