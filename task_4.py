# Timedelta function demonstration

from datetime import datetime, timedelta
import pprint

pp = pprint.PrettyPrinter(indent=2)


class Solution():
    def __init__(self, param):
        self.param = param

    def generate_ret(self):
        return {
            "base": {
                "status": 0,
                "message": 'success',
            }
        }

    def run(self):
        ret = self.generate_ret()
        ret.update({
            "jumlah_cuti_bersama": self.param["jumlah_cuti_bersama"],
            "tanggal_masuk": self.param["tanggal_masuk"],
            "tanggal_mau_cuti": self.param["tanggal_mau_cuti"],
            "durasi_cuti": self.param["durasi_cuti"],
        })

        print "\n----INPUT----"
        pp.pprint(self.param)
        print "----------------"

        # print '\nInput'
        # print 'Jumlah Cuti Bersama: {}'.format(self.param["jumlah_cuti_bersama"])
        # print 'Tanggal masuk: {}'.format(self.param["tanggal_masuk"])
        # print 'Tanggal Cuti: {}'.format(self.param["tanggal_mau_cuti"])
        # print 'Durasi Cuti: {}'.format(self.param["durasi_cuti"])

        waktu_sekarang = datetime.now()
        tanggal_tutup_buku_cuti = '31-12-{}'.format(waktu_sekarang.year)

        # Jumlah cuti pribadi adalah jumlah cuti kantor - cuti bersama.
        jumlah_cuti_pribadi = self.param["jumlah_cuti_kantor"] - self.param["jumlah_cuti_bersama"]

        try:
            tanggal_masuk = datetime.strptime(self.param["tanggal_masuk"], "%d-%m-%Y")
            tanggal_mau_cuti = datetime.strptime(self.param["tanggal_mau_cuti"], "%d-%m-%Y")
            tanggal_masuk_setelah180d = tanggal_masuk + timedelta(days=180)
        except Exception as e:
            # print '\nOutput \nMaaf, Format Tanggal Yang Anda Masukkan Salah!! \nContoh: 1-5-2021 atau 01-05-2021'
            ret["base"]["message"] = "error"
            ret["base"]["status"] = 1
            ret["base"]["err_msg"] = 'Format Tanggal Yang Anda Masukkan Salah!! \nContoh: 1-5-2021 atau 01-05-2021'
            return

        # hanya bisa cuti pada H + 180 dan sebelum tutup buku cuti tahunan
        belum_bisa_cuti = tanggal_masuk_setelah180d > tanggal_mau_cuti
        if belum_bisa_cuti:
            # print '\nOutout \nMaaf, Anda Belum Bisa Cuti Sebelum Tanggal {}:'.format(
            #     tanggal_masuk_setelah180d.strftime('%d-%m-%Y'))

            ret["base"]["message"] = "error"
            ret["base"]["status"] = 1
            ret["base"]["err_msg"] = 'Anda Belum Bisa Cuti Sebelum Tanggal {}:'.format(
                tanggal_masuk_setelah180d.strftime('%d-%m-%Y'))
            return ret
        tanggal_cuti_diluar_range = tanggal_mau_cuti > datetime.strptime(tanggal_tutup_buku_cuti, "%d-%m-%Y")
        if tanggal_cuti_diluar_range:
            # print '\nOutout \nMaaf, Anda Hanya Bisa Cuti Pada Tanggal {} sampai {}'.format(
            #     tanggal_masuk_setelah180d.strftime('%d-%m-%Y'), format(tanggal_tutup_buku_cuti))
            ret["base"]["message"] = "error"
            ret["base"]["status"] = 1
            ret["base"]["err_msg"] = 'Anda Hanya Bisa Cuti Pada Tanggal {} sampai {}'.format(
                tanggal_masuk_setelah180d.strftime('%d-%m-%Y'), format(tanggal_tutup_buku_cuti))
            return ret

        # print '\nJumlah Cuti Pribadi', jumlah_cuti_pribadi
        ret["jumlah_cuti_pribadi"] = jumlah_cuti_pribadi
        jumlah_hari = datetime.strptime(tanggal_tutup_buku_cuti, "%d-%m-%Y") - tanggal_masuk_setelah180d
        ret["jumlah_hari_kerja"] = jumlah_hari.days

        # print '\nJumlah Hari', jumlah_hari.days

        total_kuota_cuti = (jumlah_hari / 365 * jumlah_cuti_pribadi).days
        ret["total_kuota_cuti"] = total_kuota_cuti

        if total_kuota_cuti < self.param["durasi_cuti"]:
            # print '\nOutput'
            # print 'Gagal'
            # print 'Alasan: Karena Hanya Boleh Mengambil {} Hari Cuti'.format(total_kuota_cuti)
            # ret.update({"message": "error"})
            # ret.update({"base": {"message": "error"}})
            ret["base"]["message"] = "error"
            ret["base"]["status"] = 1
            ret["base"]["err_msg"] = 'Hanya Boleh Mengambil {} Hari Cuti'.format(total_kuota_cuti)
            return ret

        # print '\nOutput'
        # print 'Jumlah Cuti Pribadi Yang Bisa Diambil: {}'.format(total_kuota_cuti)

        return ret


def test_success():
    param = {
        "jumlah_cuti_kantor": 14,
        "jumlah_cuti_bersama": 7,
        "tanggal_masuk": '1-5-2021',
        "tanggal_mau_cuti": '28-10-2021',
        "durasi_cuti": 1,
    }

    solution = Solution(param=param)
    rsp = solution.run()
    if rsp:
        print "\n----OUTPUT----"
        pp.pprint(rsp)
        print "----------------"


def test_error():
    param = {
        "jumlah_cuti_kantor": 14,
        "jumlah_cuti_bersama": 7,
        "tanggal_masuk": '1-5-2021',
        "tanggal_mau_cuti": '27-10-2022',
        "durasi_cuti": 2,
        # "durasi_cuti": 1,
    }

    solution = Solution(param=param)
    rsp = solution.run()
    if rsp:
        print "\n----OUTPUT----"
        pp.pprint(rsp)
        print "----------------"


if __name__ == '__main__':
    test_success()
    test_error()
