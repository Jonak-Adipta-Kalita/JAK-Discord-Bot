import firebase_admin
import firebase_admin.firestore
import firebase_admin.credentials
import credentials

app = (
    firebase_admin.initialize_app(credential=firebase_admin.credentials.Certificate(
    {
        "type": credentials.FIREBASE_TYPE,
        "project_id": credentials.FIREBASE_PROJECT_ID,
        "private_key_id": credentials.FIREBASE_PRIVATE_KEY_ID,
        "private_key": credentials.FIREBASE_PRIVATE_KEY,
        "client_email": credentials.FIREBASE_CLIENT_EMAIL,
        "client_id": credentials.FIREBASE_CLIENT_ID,
        "auth_uri": credentials.FIREBASE_AUTH_URI,
        "token_uri": credentials.FIREBASE_TOKEN_URI,
        "auth_provider_x509_cert_url": credentials.FIREBASE_AUTH_PROVIDER_X509_CERT_URL,
        "client_x509_cert_url": credentials.FIREBASE_CLIENT_X509_CERT_URL,
    }
))
    if not len(firebase_admin._apps)
    else firebase_admin.get_app()
)

db = firebase_admin.firestore.client(app=app)
