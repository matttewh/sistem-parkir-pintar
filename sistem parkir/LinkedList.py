class Node:

    def __init__(self, data):

        self.data = data

        self.next = None


class LinkedList:

    def __init__(self):

        self.head = None


    def tambah(self, data):

        node_baru = Node(data)

        if self.head is None:

            self.head = node_baru

            return

        current = self.head

        while current.next:

            current = current.next

        current.next = node_baru


    def tampilkan(self):

        current = self.head

        while current:

            print(current.data)

            current = current.next


    def cari(self, plat):

        current = self.head

        while current:

            if current.data["plat"] == plat:

                return current.data

            current = current.next

        return None


    def hapus(self, plat):

        current = self.head

        prev = None

        while current:

            if current.data["plat"] == plat:

                if prev is None:

                    self.head = current.next

                else:

                    prev.next = current.next

                return True

            prev = current

            current = current.next

        return False


    def update(self, plat, pemilik_baru, jenis_baru):

        current = self.head

        while current:

            if current.data["plat"] == plat:

                current.data["pemilik"] = pemilik_baru

                current.data["jenis"] = jenis_baru

                return True

            current = current.next

        return False


    def to_list(self):

        data = []

        current = self.head

        while current:

            data.append(current.data)

            current = current.next

        return data