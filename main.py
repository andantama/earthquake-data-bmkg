"""
Application of Latest Earthquake Data in Indonesia
"""


def data_extract():
    """
    Tanggal: 03 Februari 2022
    Waktu: 02:29:18 WIB
    Magnitudo: 4.9
    Kedalaman: 45 km
    Lokasi: LU=0.83 BT=98.50
    Pusat Gempa: Berada di laut 81 km Timur Laut Nias Selatan
    Keterangan: Dirasakan (Skala MMI) II Pangautan
    :return:
    """
    outcome = dict()
    outcome['date'] = 'February 03, 2022'
    outcome['time'] = '02:29:18 GMT+7'
    outcome['magnitude'] = 4.9
    outcome['location'] = {'LU': 0.83, 'BT':98.50}
    outcome['EQ Center'] = '81 km in the Northeast of South Nias'
    outcome['Note'] = 'EQ shaking intensity II Pangautan (MMI Scale)'
    return outcome


def show_data(result):
    print('Latest Earthquake Data in Indonesia')
    print(result)


if __name__ == "__main__":
    print("Main Application")
    result = data_extract()
    show_data(result)
