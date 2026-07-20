<div align="center">

#  UAS Statistik dan Probabilitas

**Korelasi Pearson & Regresi Linear Sederhana**

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-3.0-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-2.4-013243?style=flat-square&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10-11557C?style=flat-square&logo=plotly&logoColor=white)
![Status](https://img.shields.io/badge/status-selesai-2ea44f?style=flat-square)

</div>

---

###  Identitas

| | |
|---|---|
| **Nama** | Syauqi Nuzul Abdi |
| **NIM** | 202512042 *(Genap)* |
| **Prodi** | Teknik Informatika — Kelas Pagi |
| **Mata Kuliah** | Statistik dan Probabilitas |
| **Dosen** | Sri Handani Widiastuti, S.Kom., M.Kom. |

---

###  Struktur

```
├── korelasi_heatmap.py         # Bagian A — korelasi Pearson + heatmap
├── regresi_linear.py           # Bagian B — regresi linear sederhana
├── poster_uas.pdf              # poster jawaban lengkap
├── heatmap_korelasi.png
├── scatter_only.png
├── regresi_dataset_waktu.png
├── requirements.txt
└── README.md
```

###  Menjalankan

```bash
pip install -r requirements.txt
python korelasi_heatmap.py
python regresi_linear.py
```

---

###  Hasil Singkat

**A — Korelasi Pearson** *(terhadap Jumlah Bug)*

| Faktor | r |
|---|---|
| LOC | `0.9983` |
| Cyclomatic Complexity | `0.9984` |
| Unit Test Coverage | `-0.9989` |

**B — Regresi Linear Sederhana**

```
Y = 0.3321 + 0.0873X          R² = 0.9995
```
Prediksi pada 90 ribu data → **≈ 8.19 detik** *(di luar rentang data asli, bersifat ekstrapolasi)*

---

<div align="center">

Detail perhitungan, script, dan interpretasi lengkap ada di `poster_uas.pdf`

</div>
