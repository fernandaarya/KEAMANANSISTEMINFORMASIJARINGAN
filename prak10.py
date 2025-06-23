from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

data_kartu = "4111111111111111|123|12/27"

data_terenkripsi = cipher.encrypt(data_kartu.encode())

data_terdeskripsi = cipher.decrypt(data_terenkripsi).decode()

print("Kunci Enkripsi:", key.decode())
print("Data Terenkripsi:", data_terenkripsi.decode())
print("Data Setelah Deskripsi:", data_terdeskripsi)