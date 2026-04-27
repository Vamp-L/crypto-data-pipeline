# 🚀 Crypto Data Pipeline

## 📌 Overview

Project ini merupakan implementasi sederhana data pipeline untuk mengambil, membersihkan, dan menyimpan data cryptocurrency menggunakan Python dan PostgreSQL.

Pipeline ini menggunakan konsep **Medallion Architecture (Bronze, Silver, Gold)** untuk mengelola data dari raw hingga siap dianalisis.

---

## 🧱 Architecture

* **Bronze** → Data mentah dari API
* **Silver** → Data hasil cleaning dan transformasi
* **Gold** → Data siap analisis (metrics, top coins)

---

## ⚙️ Tech Stack

* Python (Pandas)
* SQL (PostgreSQL)
* Excel (data checking)

---

## 🔄 Pipeline Flow

1. Mengambil data dari API
2. Menyimpan raw data ke Bronze layer
3. Melakukan cleaning di Silver layer
4. Membuat metrics & analytics di Gold layer

---

## 📁 Project Structure

```bash
data/
 ├── Bronze/
 ├── Silver/
 └── Gold/

src/
 ├── bronze_ingestion.py
 ├── silver_cleaning.py
 └── gold_analytics.py
```

---

## 🚧 Future Improvements

* Tambah scheduling (cron / Airflow)
* Tambah logging
* Integrasi ke dashboard

---

## 🎯 Goal

Membangun pemahaman end-to-end data pipeline sebagai langkah menuju Data Engineer.
