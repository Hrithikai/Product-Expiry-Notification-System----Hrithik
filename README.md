# 🧾 Product Expiry Notification System -- Hrithik

An **automated product expiry tracking and alerting system** that monitors expiry dates in real time and sends **email notifications** when products are nearing expiration.  
Built using **Python**, **Firebase Firestore**, and the **Observer Design Pattern** for scalable notification management.

---

## 📖 Project Overview

The **Product Expiry Notification System** automates expiry tracking for products by connecting to **Firebase Firestore** and scheduling **email alerts** when items are about to expire within a defined threshold (default: 5 days).  
It’s ideal for retail, pharmacies, or inventory management systems requiring proactive expiry alerts.

---

## 🧩 Features

✅ Automated expiry date tracking  
✅ Email notifications before expiry  
✅ Firebase Firestore integration  
✅ Observer pattern for notification management  
✅ Easy setup with Excel-based data upload  
✅ Cross-platform scheduling (Cron / Task Scheduler)  

---

## 🗂️ File Structure & Description

| File | Description |
|------|--------------|
| `upload_excel_to_firestore.py` | Uploads product data from an Excel file (`data.xlsx`) to Firebase Firestore. |
| `send_notification.py` | Fetches products from Firestore, checks expiry dates, and sends email alerts. Implements the Observer pattern for modular notifications. |
| `data.xlsx` | Source data file containing product details (`name`, `expiry_date`, `user_email`). |

---

## 📦 Dataset Format

Example of `data.xlsx`:

| name | expiry_date | user_email |
|------|--------------|------------|
| Product A | 2025-11-01 | user@example.com |
| Product B | 2025-10-30 | another@example.com |

---

## ⚙️ Setup & Installation

### 🧰 Prerequisites
- Python **3.9+**
- Firebase project with **Firestore** enabled
- Gmail account with **App Password**
- Excel file with product data

### 🪜 Installation

```bash
pip install -r requirements.txt
```

---

## 🔥 Firebase Configuration

1. Create a Firebase project at [Firebase Console](https://console.firebase.google.com/)
2. Enable **Firestore Database**
3. Generate a **Service Account Key**:

   * Go to **Project Settings → Service Accounts → Generate New Private Key**
   * Save the file as `productexpirychecker-firebase-adminsdk.json`
   * Place it in your project directory

---

## 📧 Gmail Setup

1. Enable **2-Step Verification** on your Gmail account
2. Create an **App Password** → copy the 16-character code
3. Add credentials to `send_notification.py`:

```python
SENDER_EMAIL = "your-email@gmail.com"
SENDER_PASSWORD = "your-app-password"  # 16-character password
```

---

## 🚀 Usage

### Step 1: Upload Data to Firestore

```bash
python upload_excel_to_firestore.py
```

### Step 2: Run Notification System

```bash
python send_notification.py
```

---

## 🔄 System Workflow

### 🧮 Data Upload Flow

* Reads Excel data with **pandas**
* Converts expiry dates to Firestore timestamps
* Uploads to `products` collection in Firestore

### 📢 Notification Flow

* Fetches products from Firestore
* Calculates expiry threshold (`today + 5 days`)
* Sends personalized email alerts for items nearing expiry
* Uses the **Observer pattern** for modular alert handling

---

## 🧠 Design Pattern Used: Observer

**Classes:**

* `ExpiryNotifier` → Manages observers and dispatches expiry events
* `ExpiryObserver` → Handles email alert logic

Easily extendable for **SMS**, **Push Notifications**, or **Web Alerts**.

---

## 🧰 Configuration

| Parameter          | File                      | Description                                   |
| ------------------ | ------------------------- | --------------------------------------------- |
| `expiry_threshold` | `send_notification.py`    | Number of days before expiry to trigger alert |
| `subject` / `body` | `ExpiryObserver.update()` | Customize email template                      |

Example:

```python
expiry_threshold = today + timedelta(days=5)
subject = "⚠️ Product Expiry Alert"
body = f"Your product '{product_name}' is expiring soon!"
```

---

## 🕓 Automation

### Linux/Mac (Cron Job)

```bash
# Run daily at 9 AM
0 9 * * * /usr/bin/python3 /path/to/send_notification.py
```

### Windows (Task Scheduler)

* Trigger: Daily at 9:00 AM
* Action: `python send_notification.py`

---

## 🧱 Firestore Structure

```
products (collection)
 └── document_id (auto-generated)
      ├── name: string
      ├── expiry_date: timestamp
      └── user_email: string
```

---

## 🧩 Troubleshooting

**Email not sending?**

* Verify Gmail App Password (16 chars)
* Ensure 2FA is enabled
* Check network connectivity

**Firebase error?**

* Verify service key path
* Ensure Firestore is enabled
* Check database rules

**Excel upload fails?**

* Correct columns: `name`, `expiry_date`, `user_email`
* Ensure date format `YYYY-MM-DD`

---

## 🛡️ Security Notes

⚠️ **Never commit these files to GitHub:**

```
*.json
config.py
```

* Keep Firebase keys private
* Store credentials securely (e.g., environment variables)

---

## 💡 Future Enhancements

* SMS alerts via **Twilio**
* Web dashboard for expiry visualization
* Batch email optimization
* Product categories and custom rules
* Push notification support

---

## 🖼️ Add a Project Image

To display an image at the top of the README:

1. Create a folder named `assets` in your project root
2. Add your image (e.g., `banner.png`)
3. Insert this line at the top of your README:

```markdown
![Product Expiry System Banner](assets/banner.png)
```

---

## 🧑‍💻 Developer

**Developed by:** Hrithik Sai  
**GitHub:** [your-username](https://github.com/your-username)

---

## ⭐ Contribute

Pull requests are welcome!  
If you'd like to improve the project, feel free to fork it and submit a PR.

---

## 🪪 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
