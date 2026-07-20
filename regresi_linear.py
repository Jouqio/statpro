# UAS Statistik dan Probabilitas - Bagian B
# Regresi Linear Sederhana: Ukuran Dataset vs Waktu Eksekusi Algoritma Sorting
# Nama  : Syauqi Nuzul Abdi
# NIM   : 202512042 (Genap)
# Prodi : Teknik Informatika - Kelas Pagi

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Data NIM Genap (15 sampel pengujian algoritma sorting)
X = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])   # Ukuran Dataset (ribu data)
Y = np.array([1.2, 1.6, 2.1, 2.5, 2.9, 3.5, 3.8, 4.3, 4.7, 5.1, 5.6, 6.0, 6.4, 6.9, 7.3])  # Waktu Eksekusi (detik)

# a. Variabel independen (X) = Ukuran Dataset, variabel dependen (Y) = Waktu Eksekusi

# b. Scatter plot data mentah
plt.figure(figsize=(6, 4.5))
plt.scatter(X, Y, color='#2563eb', s=55, edgecolor='white', linewidth=0.8)
plt.xlabel('Ukuran Dataset (Ribu Data)')
plt.ylabel('Waktu Eksekusi (Detik)')
plt.title('Scatter Plot: Ukuran Dataset vs Waktu Eksekusi')
plt.grid(alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig('scatter_only.png', dpi=200, bbox_inches='tight', facecolor='white')

# c. Bangun model regresi linear sederhana
slope, intercept, r, p, se = stats.linregress(X, Y)
r2 = r ** 2

# d. Persamaan regresi
print(f"Persamaan regresi : Y = {intercept:.4f} + {slope:.4f} X")

# e. Koefisien determinasi (R^2)
print(f"Koefisien korelasi (r)     : {r:.4f}")
print(f"Koefisien determinasi (R^2): {r2:.4f}")
print(f"p-value (uji signifikansi slope): {p:.3e}")

# f. Prediksi waktu eksekusi untuk dataset 90 ribu data
pred_90 = intercept + slope * 90
print(f"Prediksi waktu eksekusi pada X = 90 ribu data: Y = {pred_90:.2f} detik")
print("Catatan: X = 90 berada di luar rentang data asli (10-80 ribu data), jadi hasil ini ekstrapolasi.")

# Visualisasi scatter + garis regresi + titik prediksi
plt.figure(figsize=(7, 5.5))
plt.scatter(X, Y, color='#2563eb', s=55, zorder=3, label='Data Aktual', edgecolor='white', linewidth=0.8)
xs = np.linspace(0, 95, 100)
ys = intercept + slope * xs
plt.plot(xs, ys, color='#dc2626', linewidth=2.2, label=f'Y = {intercept:.4f} + {slope:.4f}X', zorder=2)
plt.scatter([90], [pred_90], color='#16a34a', s=90, marker='D', zorder=4,
            label=f'Prediksi X=90 -> Y={pred_90:.2f}')
plt.xlabel('Ukuran Dataset (Ribu Data)')
plt.ylabel('Waktu Eksekusi (Detik)')
plt.title(f'Regresi Linear Sederhana\nUkuran Dataset vs Waktu Eksekusi Algoritma (R\u00b2={r2:.4f})')
plt.grid(alpha=0.3, linestyle='--')
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('regresi_dataset_waktu.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.show()
