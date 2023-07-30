import bluetooth

# Configuration du serveur
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1

# Lier la socket à un port spécifique
server_sock.bind(("", port))

# Mettre la socket en mode écoute
server_sock.listen(1)
print("Serveur Bluetooth 4.0 démarré. En attente de connexions...")

# Accepter une connexion entrante
client_sock, client_info = server_sock.accept()
print("Client connecté :", client_info)

# Recevoir des données du client
data = client_sock.recv(1024)
received_data = data.decode()
print("Message reçu du client :", received_data)

# Envoyer une réponse au client
response = "Message reçu avec succès!"
client_sock.send(response.encode())

# Fermer la connexion avec le client
client_sock.close()
# Fermer la socket du serveurserver_sock.close()