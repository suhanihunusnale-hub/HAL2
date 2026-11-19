# ⚛️ QSC Defence System
### Quantum-Inspired Secure Communication System

A Flask-based secure messaging demonstration that simulates the **BB84 Quantum Key Distribution (QKD) protocol** to generate encryption keys and uses AES-based encryption for secure message exchange.

The system demonstrates quantum-inspired cryptographic concepts through a role-based communication platform with threat monitoring and audit logging.

---

## 🚀 Key Features

- **BB84 Protocol Simulation:** Simulates quantum key distribution for encryption key generation.
- **AES Encryption:** Encrypts and decrypts messages using generated keys.
- **Role-Based Authentication:** Supports four user roles.
- **Secure Messaging:** Sender and receiver communication through a secure inbox.
- **Threat Monitoring:** Includes a threat detection monitoring interface.
- **Audit Logging:** Maintains activity records for monitoring system operations.

---

## 👥 User Roles

| Role | Access |
|---|---|
| Administrator | Administrative functions |
| Commander | Commander-level access |
| Field Officer | Field communication |
| Security Analyst | Security monitoring |

---

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Backend | Python, Flask |
| Database | SQLite |
| Cryptography | AES |
| Key Distribution | BB84 Simulation |
| Frontend | HTML, CSS, JavaScript |

---

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/suhanihunusnale-hub/HAL2.git
cd HAL2
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows:

```powershell
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

### 6. Open in browser

```text
http://127.0.0.1:5000
```

---

## 🏗️ System Workflow

1. User logs into the application.
2. The system identifies the user's role.
3. BB84 simulation generates a shared encryption key.
4. AES-based encryption is used for message protection.
5. The receiver accesses the message through the inbox.
6. Threat monitoring and audit logging support security observation.

---

## 🔐 Security Considerations

This is an educational demonstration, not a production-ready defence communication system.

- BB84 is simulated in software; no physical quantum hardware is used.
- Demo authentication uses plaintext passwords in the current implementation.
- Production deployment requires secure password hashing, protected key management, secure sessions and additional security testing.
- Do not use real military, classified or sensitive information.

---

## 🎯 Project Objective

The objective is to demonstrate how concepts from quantum key distribution can be combined with conventional encryption to explore secure communication architectures.

The project provides an educational environment for understanding BB84 simulation, AES-based encryption, authentication and security monitoring.

---

## 👩‍💻 Developer

**Suhani Hunusnale**

B.Tech Computer Science and Engineering  
Specialization: Data Science

GitHub: https://github.com/suhanihunusnale-hub

---

⭐ If you find this project interesting, consider giving the repository a star.
