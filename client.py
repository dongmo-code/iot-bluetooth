import bluetooth

# Configuration du client
server_mac = "XX:XX:XX:XX:XX:XX" # Adresse MAC du serveur Bluetooth
port = 1

# Créer une socket client
client_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

# Se connecter au serveur
client_sock.connect((server_mac, port))
print("Connecté au serveur Bluetooth 4.0")

# Envoyer des données au serveur
message = "Hello, server!"
client_sock.send(message.encode())

# Recevoir la réponse du serveur
data = client_sock.recv(1024)
received_data = data.decode()
print("Réponse du serveur :", received_data)

# Fermer la connexion avec le serveur
client_sock.close()