'''
pesan.py
25 Juli 2018
khusus untuk pengelompokan pesan saat data:
1. berhasil ditambahkan;
2. berhasil diperbaharui;
3. berhasil dihapus.
'''
class Pesan:
    def __init__(self):
        self.success_add = "Data Berhasil ditambahkan. Yey!"
        self.success_update = "Data Berhasil diperbaharui. Yey!"
        self.success_delete = "Data Berhasil dihapus."

    def add(self):
        return self.success_add

    def update(self):
        return self.success_update

    def delete(self):
        return self.success_delete
