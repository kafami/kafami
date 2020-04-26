x= ' ';
class userService:

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.data = {
                "kaffakel38@gmail.com" : {
                    "email"     : "kaffakel38@gmail.com",
                    "password"  : "12345",
                    "role"      : "'user Gold'",
                    "daftar barang yang dibeli"      : "minyak 1 kg, beras 5 kg, speaker JBl murah, celana training pria,"+56*x+"casing smartphone samsungn a50, parker ballpoint"
                },

                "haikalkel38@gmail.com" : {
                    "email"     : "haikalkel38@gmail.com",
                    "password"  : "12345",
                    "role"      : "'user Platinum'",
                    "daftar barang yang dibeli"      : "binder 20 ring, kertas binder 20 ring, pakan ikan cupang provit,"+56*x+"earphone bluetooth tws56, mousepad steelseries qck"

                }
                }
        
    def login(self):
        get_data = self.checkCredentials()
        if get_data:

                print("login terverifikasi: ",get_data['email'])
                print("selamat datang kembali")
                print("sementara akun anda masih",get_data['role'])
                print("riwayat belanja online yang anda lakukan : ", get_data['daftar barang yang dibeli'])
        else:
                print("\nInvalid Login!\n")

    def checkCredentials(self):
            for value in self.data:
                if value == self.email:
                    get_data_user = self.data[value]
                    if self.password == get_data_user['password']:
                        return get_data_user
                    else:
                        return False
                