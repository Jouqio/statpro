# UAS Statistik dan Probabilitas - Bagian A
# Korelasi Pearson & Heatmap: Faktor Kualitas Kode vs Jumlah Bug
# Nama  : Syauqi Nuzul Abdi
# NIM   : 202512042 (Genap)
# Prodi : Teknik Informatika - Kelas Pagi

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Data NIM Genap (15 sampel pengujian modul)
data = {
    'LOC': [8, 10, 12, 15, 17, 18, 20, 22, 24, 25, 28, 30, 32, 35, 38],
    'Cyclomatic Complexity': [10, 13, 15, 18, 20, 22, 23, 26, 28, 29, 31, 34, 35, 37, 40],
    'Unit Test Coverage': [90, 88, 85, 82, 80, 76, 74, 70, 68, 66, 63, 60, 58, 55, 50],
    'Jumlah Bug': [12, 15, 18, 22, 25, 29, 30, 35, 37, 39, 42, 46, 49, 53, 57],
}
df = pd.DataFrame(data)

# 1. Hitung matriks korelasi Pearson
corr = df.corr(method='pearson')
print("Matriks Korelasi Pearson:")
print(corr.round(4))

print("\nKorelasi terhadap Jumlah Bug:")
for kolom in ['LOC', 'Cyclomatic Complexity', 'Unit Test Coverage']:
    r = df[kolom].corr(df['Jumlah Bug'])
    print(f"  {kolom:22s} -> r = {r:.4f}  (r^2 = {r**2:.4f})")

# 2. Visualisasi heatmap
plt.figure(figsize=(7, 6))
sns.heatmap(
    corr,
    annot=True,
    fmt='.3f',
    cmap='RdYlBu_r',
    vmin=-1, vmax=1,
    square=True,
    linewidths=1.2,
    linecolor='white',
    cbar_kws={'label': 'Koefisien Korelasi Pearson (r)'},
    annot_kws={'size': 12, 'weight': 'bold'},
)
plt.title('Heatmap Korelasi Pearson\nFaktor Kualitas Kode vs Jumlah Bug', fontsize=13, fontweight='bold', pad=15)
plt.xticks(rotation=30, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig('heatmap_korelasi.png', dpi=200, bbox_inches='tight', facecolor='white')
plt.show()
