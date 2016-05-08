#!/usr/bin/python2
# -*- coding: utf-8 -*

# Import des modules

import socket
import hashlib
import sys
import pickle
import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def crypterScoreAttente(dico_score):

    # Tout ce qui est dans ce bloc correspond au cryptage symétrique
    # On prépare la clé Fernet qui permet de crypter et de décrypter
    #--------------------------------------------------------------------------
    mot_de_passe = "1234123412341234"
    cle_16o = "1234123412341234"

    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                     length=32,
                     salt=cle_16o,
                     iterations=100000,
                     backend=default_backend())
    cle = base64.urlsafe_b64encode(kdf.derive(mot_de_passe))
    cle_fernet = Fernet(cle)
    #--------------------------------------------------------------------------

    checksum = hashlib.md5(open(sys.argv[0], "rb").read()).hexdigest()
    liste = [checksum, dico_score]

    fichier_temp = open("../score/temp.tmp", "wb")
    mon_pickler = pickle.Pickler(fichier_temp)
    mon_pickler.dump(liste)
    fichier_temp.close()

    with open("../score/temp.tmp", "rb") as fichier_temp:
        texte = fichier_temp.read()
    os.remove("../score/temp.tmp")

    texte_crypte = cle_fernet.encrypt(texte)
    fichier_score_attente = open("../scores/en_attente.db", "a")
    fichier_score_attente.write(texte_crypte + "||||||||||")
    fichier_score_attente.close()

def envoyerScoreAttente():
    pass
#     client_to_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_to_serv.connect(("localhost", 25565))

#     msg_recu = ""
#     while msg_recu[-4:] != "\end":
#         msg_recu += client_to_serv.recv(1024)
#     msg_recu = msg_recu[:-4]
#     print(msg_recu)

#     if msg_recu == "OK":
#         client_to_serv.send("PUSH\end")

#         msg_recu = ""
#         while msg_recu[-4:] != "\end":
#             msg_recu += client_to_serv.recv(1024)
#         msg_recu = msg_recu[:-4]
#         print(msg_recu)
#         if msg_recu == "OK":

#             # On envoie le score
#             client_to_serv.send(score + "\end")

#             msg_recu = ""
#             while msg_recu[-4:] != "\end":
#                 msg_recu += client_to_serv.recv(1024)
#             msg_recu = msg_recu[:-4]
#             print(msg_recu)

#             if msg_recu == "OK":
#                 return True

def recupererScore():
    pass
#     client_to_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_to_serv.connect(("localhost", 25565))

#     msg_recu = ""
#     while msg_recu[-4:] != "\end":
#         msg_recu += client_to_serv.recv(1024)
#     msg_recu = msg_recu[:-4]
#     print(msg_recu)

#     if msg_recu == "OK":
#         client_to_serv.send("PULL\end")

#         msg_recu = ""
#         while msg_recu[-4:] != "\end":
#             msg_recu += client_to_serv.recv(1024)
#         msg_recu = msg_recu[:-4]
#         print(msg_recu)
#         if msg_recu == "OK":

#             msg_recu = ""
#             while msg_recu[-4:] != "\end":
#                 msg_recu += client_to_serv.recv(1024)
#             msg_recu = msg_recu[:-4]
#             print(msg_recu)

#             # msg_recu correspond à la DB récupérée