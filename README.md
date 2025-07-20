# 🌐 URL Safety Checker (Flask-based Web App)

This is a simple Flask web application that helps users determine whether a given website URL is **Safe**, **Spam**, or **Dangerous** based on predefined logic. It features a cyber-themed UI built with HTML and CSS for a sleek and modern look.

---

## 🚀 Features

- ✅ Simple URL safety logic (can be extended)
- 🎨 Cyberpunk-inspired UI with CSS animations
- 🔍 URL classification: Safe / Spam / Danger
- 🧠 Easy-to-understand code for beginners in Flask

---

## 📁 Project Structure

├── app.py # Flask backend logic
├── templates/
│ └── index.html # Frontend HTML form (create manually if missing)
├── static/
│ └── styles.css # Styling with a dark matrix-like theme
├── requirements.txt # Dependencies
└── README.md # Project description

---

## 🛠️ How It Works

- URLs starting with `https` are considered **Safe**.
- URLs containing the word `phishing` are marked **Danger**.
- All other URLs are labeled as **Spam**.

> **Note**: This logic is for demonstration only. For production use, consider integrating real threat intelligence APIs.

---

## 🔧 Installation & Usage

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/url-safety-checker.git
cd url-safety-checker

📸 UI Preview
Paste a URL into the text box

Click the "Check URL" button

Instantly see if it's Safe, Spam, or Danger

🧪 Testing URLs
Here are some sample test cases:

https://google.com → ✅ Safe

http://randomsite.com → ⚠️ Spam

https://phishing-site.com → 🚨 Danger

🧩 Future Improvements
Use machine learning or threat intelligence APIs

Add database support for tracking checked URLs

Improve detection logic for malicious domains

Add user authentication for tracking personal checks
<img width="1908" height="792" alt="Screenshot 2025-07-20 201615" src="https://github.com/user-attachments/assets/af126d37-0503-4658-adea-a08641928522" />
<img width="1908" height="792" alt="Screenshot 2025-07-20 201615" src="https://github.com/user-attachments/assets/6871240f-c3bf-4660-b3df-5bf7313d91b4" />
