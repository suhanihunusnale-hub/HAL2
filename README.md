# ⚛ QSC Defence System (HAL2)

A quantum-inspired secure messaging demo built with Flask. Simulates BB84 quantum key distribution for generating encryption keys, then uses those keys to encrypt/decrypt messages between users. Includes a threat monitor and audit log.

## Features
- BB84 quantum key distribution simulation
- AES-based message encryption/decryption
- Role-based login (Administrator, Commander, Field Officer, Security Analyst)
- Sender/Receiver secure inbox
- Threat detection monitor
- Audit logging

## Setup

```bash
python3 -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
python app.py
```

Visit `http://127.0.0.1:5000`

## Demo Login Credentials

| Username | Password | Role |
|---|---|---|
| admin | admin123 | Administrator |
| commander01 | cmd123 | Commander |
| officer01 | off123 | Field Officer |
| analyst01 | ana123 | Security Analyst |

## Notes
- This is a demo/learning project — passwords are stored in plaintext, not for production use.
- Database (`database.db`) auto-creates on first run if missing.