import smtplib
import firebase_admin
from firebase_admin import credentials, firestore
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta

# Firebase Setup
cred = credentials.Certificate("productexpirychecker-firebase-adminsdk-fbsvc-773d9d8ff1.json")  # Replace with your JSON file
firebase_admin.initialize_app(cred)
db = firestore.client()

# Email Credentials
SENDER_EMAIL = "boostup2047@gmail.com"  # Replace with your Gmail
SENDER_PASSWORD = "hrit thik sai7 bhai"  # Replace with your generated App Password

# Observer Pattern Implementation
class ExpiryObserver:
    def update(self, product_name, expiry_date, user_email):
        subject = "⚠️ Product Expiry Alert"
        body = f"Dear User,\n\nYour product '{product_name}' is expiring on {expiry_date}.\nPlease take necessary action.\n\nBest Regards,\nmake it "
        send_email(user_email, subject, body)

class ExpiryNotifier:
    def __init__(self):
        self.observers = []
    
    def add_observer(self, observer):
        self.observers.append(observer)
    
    def notify_observers(self, product_name, expiry_date, user_email):
        for observer in self.observers:
            observer.update(product_name, expiry_date, user_email)

# Function to send email
def send_email(to_email, subject, body):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        server.quit()
        print(f"✅ Email sent successfully to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send email: {str(e)}")

# Fetching expiring products from Firebase
def check_expiry_and_notify():
    today = datetime.today().date()
    expiry_threshold = today + timedelta(days=5)
    products = db.collection("products").get()
    
    notifier = ExpiryNotifier()
    observer = ExpiryObserver()
    notifier.add_observer(observer)
    
    for product in products:
        data = product.to_dict()
        product_name = data.get("name", "Unknown Product")
        expiry_date_str = data.get("expiry_date")
        user_email = data.get("user_email")
        
        if expiry_date_str:
            try:
                if isinstance(expiry_date_str, datetime):  
                    expiry_date = expiry_date_str.date()
                else:
                    expiry_date = datetime.strptime(expiry_date_str, "%Y-%m-%d").date()
                
                if today <= expiry_date <= expiry_threshold:
                    if user_email:
                        notifier.notify_observers(product_name, expiry_date, user_email)
            except Exception as e:
                print(f"⚠️ Error processing product '{product_name}': {e}")

if __name__ == "__main__":
    check_expiry_and_notify()

