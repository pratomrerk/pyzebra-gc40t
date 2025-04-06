
# 🖨️ Zebra GC420t USB Direct ZPL Printing (No Windows Spooler)

A low-level Python script to send **ZPL (Zebra Programming Language)** directly to **Zebra GC420t** via USB.  
**No need to install Windows printer drivers or use the Windows Print Spooler.** This approach is ideal for embedded systems, automation, kiosks, or developer-focused deployments.

---

## ✅ Features

- Raw USB communication with Zebra GC420t
- Send ZPL commands directly via `pyusb` + `libusb`
- No `win32print`, no Windows spooler required
- Easy to automate and customize
- Supports text, barcodes, QR codes (if printer supports it)

---

## ⚙️ Requirements

### 1. Python 3.x

Install via Chocolatey or manually:

```bash
choco install -y python3
```

### 2. Python dependencies

```bash
pip install pyusb
```

### 3. Install `libusb` backend

Download from:  
🔗 https://github.com/libusb/libusb/releases

- Extract the archive
- Copy `libusb-1.0.dll` from `MS64\dll` (or MS32 for 32-bit) to:
  - `C:\Windows\System32`

### 4. Replace USB driver with `libusbK` (Zadig)

Download Zadig: https://zadig.akeo.ie/

1. Run Zadig
2. Go to **Options → List All Devices**
3. Select **Zebra GC420t**
4. Change driver from `USB Printing Support` → `libusbK`
5. Click **Replace Driver**

> ⚠️ After doing this, Windows will no longer recognize the printer as a normal printing device.

---

## 🎨 Design ZPL Label Online

Use: [https://labelary.com/viewer.html](https://labelary.com/viewer.html)

This allows you to preview and design ZPL labels easily.

---

## 📁 Project Structure

```
.
├── zebra-gc40t.py       # Main Python script
├── install.bat          # Auto-setup (Python, libusb, Zadig instructions)
├── run.bat              # One-click launcher
├── requirements.txt
└── README.md
```

## 👨‍💻 Author

**Pratomrerk B.**  
*"Fu*k Windows Print Spooler. Go raw."*

---

## 🤖 Thank you

Github Copilot