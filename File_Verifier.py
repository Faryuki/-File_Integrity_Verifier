import tkinter as tk
from tkinter import filedialog, messagebox
import hashlib

# Ganti ini dengan hash file yang asli
EXPECTED_HASH = "c10a5fda1fd1bcbac47e1c4a76d41e4d38c1f64a6e2cb3db6cc0e0c74a6d8b2b"

def calculate_file_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        messagebox.showerror("Error", f"Gagal membaca file:\n{e}")
        return None

def verify_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    file_hash = calculate_file_hash(file_path)
    if file_hash is None:
        return

    result_text.set(f"Hash File:\n{file_hash}")

    if file_hash == EXPECTED_HASH:
        messagebox.showinfo("Verifikasi Berhasil", "✅ File valid dan tidak dimodifikasi.")
    else:
        messagebox.showwarning("Verifikasi Gagal", "❌ File tidak valid atau telah dimodifikasi!")

# GUI
root = tk.Tk()
root.title("File Integrity Verifier")
root.geometry("500x300")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True)

label = tk.Label(frame, text="Klik tombol di bawah untuk memilih file yang akan diverifikasi:")
label.pack(pady=(0,10))

verify_button = tk.Button(frame, text="Pilih File", command=verify_file)
verify_button.pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(frame, textvariable=result_text, wraplength=450, justify="left")
result_label.pack(pady=(20, 0))

root.mainloop()
