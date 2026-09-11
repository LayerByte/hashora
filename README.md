# hashora

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Hashing](https://img.shields.io/badge/Hashing-MD5%20%7C%20SHA1%20%7C%20SHA256%20%7C%20SHA512-0A66C2?style=for-the-badge)
![Integrity](https://img.shields.io/badge/File-Integrity-2EA44F?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**hashora** is a small Python file hash checker for educational integrity verification. It calculates cryptographic hashes for a selected file and can compare the result with an expected hash value.

School Purpose Only.

## 🧭 Overview

hashora helps users verify whether a file is unchanged by calculating its hash. A hash is a fixed-length fingerprint created from file contents. If even one byte in the file changes, the resulting hash should change too.

This project is intended for learning how file integrity checks work with Python's built-in `hashlib` module. It does not require any external packages.

## ✨ Features

| Feature | Description |
| --- | --- |
| 📁 File selection | Enter a local file path from the terminal |
| 📏 File size | Displays readable size and exact byte count |
| 🔐 Multiple hashes | Supports MD5, SHA1, SHA256, and SHA512 |
| ✅ Hash comparison | Compares a calculated hash with an expected value |
| 🧯 Error handling | Handles missing files, permission issues, and interruptions |
| 🧑‍🏫 Beginner-friendly code | Uses reusable functions and short comments |
| 📦 No dependencies | Uses only Python's standard library |

## 🔐 Supported Algorithms

| Algorithm | Common Use |
| --- | --- |
| MD5 | Legacy checksums and basic file identification |
| SHA1 | Legacy integrity checks |
| SHA256 | Modern file integrity verification |
| SHA512 | Stronger SHA-2 family hashing with longer output |

MD5 and SHA1 are included for educational and compatibility purposes. For modern integrity verification, SHA256 or SHA512 is usually preferred.

## 🧰 Requirements

- Python 3.9 or newer
- A terminal or command prompt
- A readable local file to check
- No third-party Python packages

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/LayerByte/hashora.git
cd hashora
```

Or download the project files and open a terminal inside the `hashora` folder.

## ▶️ Usage

Run the application:

```bash
python main.py
```

On Windows, if `python` is not available, try:

```bash
py main.py
```

Follow the prompts:

```text
Enter file path: example.txt
Select an option: 3
Compare with an expected hash? (y/n): y
Enter expected hash: 2cf24dba5fb0a30e26e83b2ac5b9e29e...
```

## 🖥️ Example Output

```text
========================================================
hashora
Educational file hash checker for integrity verification.
School Purpose Only.
========================================================
Enter file path: example.txt

Supported hash algorithms:
  1. MD5
  2. SHA1
  3. SHA256
  4. SHA512
  5. All algorithms
Select an option: 3
Calculating SHA256...

File information
--------------------------------------------------------
Name: example.txt
Path: example.txt
Size: 12.00 B (12 bytes)

Calculated hashes
--------------------------------------------------------
SHA256 : a948904f2f0f479b8f8197694b30184b0d2ed1c1cd2a1ec0fb85d299a192a447

Compare with an expected hash? (y/n): y
Enter expected hash: a948904f2f0f479b8f8197694b30184b0d2ed1c1cd2a1ec0fb85d299a192a447

Comparison result
--------------------------------------------------------
Algorithm: SHA256
Result: MATCH
The file hash matches the expected value.
```

## 🧪 Educational Explanation Of File Hashes

A file hash is created by passing file contents through a hash algorithm. The output is a string of letters and numbers that acts like a fingerprint for the file.

Hashes are commonly used to:

- Check whether a downloaded file was corrupted
- Confirm that a file has not changed
- Compare two files without reading them manually
- Publish software checksums for users to verify

Hashes are one-way values. They are useful for integrity checking, but they are not encryption and do not hide file contents.

## ⚠️ Disclaimer

This project is for educational integrity verification only. It should not be treated as a complete security platform or forensic tool. Always use trusted sources when comparing expected hashes, and prefer SHA256 or SHA512 for modern integrity checks.

## 📄 License

This project is released under the MIT License. You may use, modify, and share it according to the license terms.
