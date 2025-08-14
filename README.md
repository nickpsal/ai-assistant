# FRIDAY – Έξυπνος Ψηφιακός Βοηθός στα Ελληνικά

Ο **FRIDAY** είναι ένας προηγμένος, σαρκαστικός αλλά ευγενικός ψηφιακός βοηθός εμπνευσμένος απο την σειρά ταινιών 
Iron Man, κατασκευασμένος με το [LiveKit Agents SDK](https://docs.livekit.io/agents/) και Google Realtime LLM API.  
Υποστηρίζει φωνητική και Video Call, εκτελεί εντολές, και αλληλεπιδρά αποκλειστικά στα Ελληνικά.

## ✨ Χαρακτηριστικά
- 🎤 **Live φωνητική αλληλεπίδραση** μέσω LiveKit
- 🤖 **Google Realtime Model** για επεξεργασία εντολών και συζητήσεων
- 🛠 **Custom εργαλεία:**
  - **`get_weather`** → Επιστρέφει τον καιρό για οποιαδήποτε πόλη
  - **`search_web`** → Web αναζήτηση με DuckDuckGo
  - **`send_email`** → Στέλνει email μέσω Gmail SMTP (με App Password)
  - **`open_application`** → Ανοίγει τοπικές εφαρμογές (π.χ. `notepad`, `calc`, `chrome`)
- 🎭 **Ελληνικό στυλ επικοινωνίας** – μιλάει σαν εκλεπτυσμένος Βρετανός μπάτλερ που μεγάλωσε στην Αθήνα
- 📜 **Custom prompts** για ακριβή εκτέλεση εντολών

## 🗂 Δομή Project
```
project/
├── agent.py             # Ορισμός Assistant και LiveKit session
├── prompts.py           # Οδηγίες ύφους και εκτέλεσης
├── online_tools.py      # Εργαλεία (καιρός, αναζήτηση, email, άνοιγμα εφαρμογών)
├── local_tools.py       # (προαιρετικά) Εργαλεία για τοπικές λειτουργίες
├── requirements.txt     # Python dependencies
├── .env                 # Περιβάλλον με API Keys και Gmail credentials
```

## 🔧 Εγκατάσταση

1. **Κλωνοποίησε το repo**
   ```bash
   git clone https://github.com/username/friday-assistant.git
   cd friday-assistant
   ```

2. **Δημιούργησε Python virtual env & εγκατέστησε τα requirements**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows

   pip install -r requirements.txt
   ```

3. **Ρύθμισε το `.env`**
   ```env
   LIVEKIT_URL=wss://YOUR_INSTANCE.livekit.cloud
   LIVEKIT_API_KEY=YOUR_API_KEY
   LIVEKIT_API_SECRET=YOUR_API_SECRET

   GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY

   GMAIL_USER=your_email@gmail.com
   GMAIL_APP_PASSWORD=your_gmail_app_password
   ```

## ▶️ Εκτέλεση
```bash
python agent.py
```
Ο FRIDAY θα συνδεθεί στο LiveKit room και θα ξεκινήσει να αλληλεπιδρά.

## 🗣 Παραδείγματα εντολών
- «Τι καιρό θα κάνει στην Αθήνα;» → Επιστρέφει καιρό
- «Ψάξε στο web για τεχνητή νοημοσύνη» → DuckDuckGo αναζήτηση
- «Στείλε email στον Νίκο με θέμα Καλημέρα» → Στέλνει email
- «Άνοιξε notepad» → Ανοίγει το Notepad στα Windows

## ⚙️ `open_application` Εργαλείο
Υποστηρίζει:
- **Windows** → `subprocess.Popen([app_name])`
- **macOS** → `open -a app_name`
- **Linux** → Εκτέλεση ονόματος εφαρμογής

## 📜 Άδεια
MIT License
