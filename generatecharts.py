import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 7)
plt.rcParams['font.size'] = 11

# ============================================================
# 1. MANY SMALL LISTS (100,000 lists for ALL sizes)
# ============================================================
data_small = {
    'Algorithm': ['Bubble', 'Insertion', 'Selection', 'Merge', 'Quick', 'Heap', 'Timsort'],
    'Size 20 (100k lists)': [0.85, 0.45, 0.53, 1.02, 0.51, 0.97, 0.05],
    'Size 30 (100k lists)': [1.81, 0.95, 1.03, 1.63, 0.88, 1.63, 0.09],
    'Size 50 (100k lists)': [4.86, 2.48, 2.55, 3.83, 1.71, 3.14, 0.17],
    'Size 100 (100k lists)': [19.07, 9.46, 9.32, 8.91, 4.14, 7.43, 0.38]
}

df_small = pd.DataFrame(data_small)
df_small = df_small.set_index('Algorithm')

# Create a figure with 4 subplots (2x2)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

sizes_info = [
    ('Size 20 (100k lists)', 'Size 20 (100,000 lists)'),
    ('Size 30 (100k lists)', 'Size 30 (100,000 lists)'),
    ('Size 50 (100k lists)', 'Size 50 (100,000 lists)'),
    ('Size 100 (100k lists)', 'Size 100 (100,000 lists)')
]

for idx, (col, title_name) in enumerate(sizes_info):
    ax = axes[idx]
    # Sortează pentru o vizualizare mai clară
    sorted_series = df_small[col].sort_values()
    sorted_series.plot(kind='bar', ax=ax, color='steelblue', edgecolor='black')
    ax.set_title(f'Small Lists - {title_name}', fontsize=12, fontweight='bold')
    ax.set_ylabel('Total Time (seconds)')
    ax.set_xlabel('Algorithm')
    ax.tick_params(axis='x', rotation=45)
    ax.grid(axis='y', alpha=0.3)

    # Adaugă valorile pe bare
    for i, (bar, val) in enumerate(zip(ax.patches, sorted_series)):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + max(df_small[col]) * 0.01,
                f'{val:.2f}s', ha='center', va='bottom', fontsize=9)

plt.suptitle('Figure 1: Many Small Lists - Total Time for 100,000 lists (ALL sizes including 100)',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('figure1_small_lists.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# 2. MEDIUM ARRAYS
# ============================================================
data_medium = {
    'Algorithm': ['Bubble', 'Insertion', 'Selection', 'Merge', 'Quick', 'Heap', 'Timsort'],
    '1,000': [0.284, 0.018, 0.022, 0.002, 0.001, 0.002, 0.000],
    '5,000': [7.50, 2.19, 2.22, 0.084, 0.083, 0.013, 0.001],
    '10,000': [22.60, 8.71, 8.51, 0.096, 0.090, 0.104, 0.001],
    '50,000': [100, 100, 100, 0.497, 0.309, 0.803, 0.082]  # O(n²) approximat
}

df_medium = pd.DataFrame(data_medium)
df_medium = df_medium.set_index('Algorithm')

# Split into O(n²) and O(n log n) for better visualization
o_n2 = df_medium.loc[['Bubble', 'Insertion', 'Selection']]
o_nlogn = df_medium.loc[['Merge', 'Quick', 'Heap', 'Timsort']]

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# O(n²) algorithms (log scale)
o_n2.T.plot(kind='line', marker='o', ax=axes[0], linewidth=2, markersize=6)
axes[0].set_title('O(n²) Algorithms - Medium Arrays', fontweight='bold')
axes[0].set_ylabel('Time (seconds) - Log Scale')
axes[0].set_xlabel('Array Size')
axes[0].set_yscale('log')
axes[0].grid(True, alpha=0.3)
axes[0].legend(title='Algorithm')

# O(n log n) algorithms
o_nlogn.T.plot(kind='line', marker='s', ax=axes[1], linewidth=2, markersize=6)
axes[1].set_title('O(n log n) Algorithms - Medium Arrays', fontweight='bold')
axes[1].set_ylabel('Time (seconds)')
axes[1].set_xlabel('Array Size')
axes[1].grid(True, alpha=0.3)
axes[1].legend(title='Algorithm')

plt.suptitle('Figure 2: Medium Arrays (Random Data)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('figure2_medium_arrays.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# 3. LARGE ARRAYS
# ============================================================
data_large = {
    'Algorithm': ['Merge', 'Quick', 'Heap', 'Timsort'],
    '100,000': [1.09, 0.70, 1.72, 0.02],
    '500,000': [7.00, 5.20, 12.29, 0.40],
    '1,000,000': [14.61, 11.18, 27.51, 0.91]
}

df_large = pd.DataFrame(data_large)
df_large = df_large.set_index('Algorithm')

fig, ax = plt.subplots(figsize=(10, 6))
df_large.T.plot(kind='line', marker='o', ax=ax, linewidth=2, markersize=8)
ax.set_title('Figure 3: Large Arrays (Random Data) - O(n log n) Algorithms', fontsize=14, fontweight='bold')
ax.set_ylabel('Time (seconds)')
ax.set_xlabel('Array Size')
ax.grid(True, alpha=0.3)
ax.legend(title='Algorithm', loc='upper left')

plt.tight_layout()
plt.savefig('figure3_large_arrays.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# 4. MASSIVE ARRAYS
# ============================================================
data_massive = {
    'Algorithm': ['Merge', 'Quick', 'Heap', 'Timsort'],
    '10,000,000': [22.89, 18.00, 47.22, 1.68],
    '100,000,000': [284.00, 246.53, 646.01, 22.36],
    '1,000,000,000': [0, 0, 0, 958.22]  # Estimated for others
}

df_massive = pd.DataFrame(data_massive)
df_massive = df_massive.set_index('Algorithm')

fig, ax = plt.subplots(figsize=(12, 7))

# Bar chart for massive arrays
x = np.arange(len(df_massive.columns))
width = 0.2
multiplier = 0

for algo, times in df_massive.iterrows():
    offset = width * multiplier
    bars = ax.bar(x + offset, times, width, label=algo, edgecolor='black')
    multiplier += 1

ax.set_xticks(x + width * 1.5)
ax.set_xticklabels(['10 Million', '100 Million', '1 Billion'])
ax.set_ylabel('Time (seconds) - Log Scale')
ax.set_xlabel('Array Size')
ax.set_title('Figure 4: Massive Arrays - O(n log n) Algorithms', fontweight='bold')
ax.set_yscale('log')
ax.legend(title='Algorithm', loc='upper left')
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('figure4_massive_arrays.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# 5. DATA STRUCTURES (1,000,000 elements)
# ============================================================
data_structures = {
    'Algorithm': ['Merge', 'Quick', 'Heap', 'Timsort'],
    'Random': [1.71, 1.35, 2.99, 0.14],
    'Sorted': [0.95, 1.05, 2.58, 0.01],
    'Reverse': [0.98, 1.12, 2.42, 0.01],
    '98% Sorted': [1.37, 1.03, 2.60, 0.03],
    'Few Unique': [1.42, 0.18, 2.21, 0.05]
}

df_struct = pd.DataFrame(data_structures)
df_struct = df_struct.set_index('Algorithm')

fig, ax = plt.subplots(figsize=(12, 6))
df_struct.T.plot(kind='bar', ax=ax, edgecolor='black', width=0.7)
ax.set_title('Figure 5: Performance on Different Data Structures (1,000,000 elements)', fontsize=14, fontweight='bold')
ax.set_ylabel('Time (seconds) - Log Scale')
ax.set_xlabel('Data Structure Type')
ax.set_yscale('log')
ax.legend(title='Algorithm', loc='upper left', bbox_to_anchor=(1.02, 1))
ax.tick_params(axis='x', rotation=45)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('figure5_data_structures.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# 6. HALF SORTED (1,000,000 elements)
# ============================================================
data_half = {
    'Algorithm': ['Merge', 'Quick', 'Heap', 'Timsort'],
    'Time': [1.25, 1.23, 2.86, 0.06]
}

df_half = pd.DataFrame(data_half)

fig, ax = plt.subplots(figsize=(8, 5))
colors = ['steelblue', 'lightblue', 'cornflowerblue', 'navy']
bars = ax.bar(df_half['Algorithm'], df_half['Time'], color=colors, edgecolor='black')
ax.set_title('Figure 6: Half Sorted Arrays (1,000,000 elements)', fontsize=14, fontweight='bold')
ax.set_ylabel('Time (seconds) - Log Scale')
ax.set_yscale('log')
ax.grid(axis='y', alpha=0.3)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:.2f}s', xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 5), textcoords="offset points", ha='center', va='bottom')

plt.tight_layout()
plt.savefig('figure6_half_sorted.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# 7. DATA TYPES (100,000 elements)
# ============================================================
data_types = {
    'Algorithm': ['Bubble', 'Insertion', 'Selection', 'Merge', 'Quick', 'Heap', 'Timsort'],
    'Integers': [220.70, 97.23, 87.78, 0.13, 0.10, 0.21, 0.01],
    'Floats': [219.27, 92.63, 81.69, 0.13, 0.09, 0.20, 0.01],
    'Strings': [269.43, 115.47, 124.33, 0.14, 0.13, 0.23, 0.01]
}

df_types = pd.DataFrame(data_types)
df_types = df_types.set_index('Algorithm')

# Separate O(n²) and O(n log n) for better scale
o_n2_types = df_types.loc[['Bubble', 'Insertion', 'Selection']]
o_nlogn_types = df_types.loc[['Merge', 'Quick', 'Heap', 'Timsort']]

# Plot O(n²) on left subplot, O(n log n) on right
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

o_n2_types.T.plot(kind='bar', ax=ax1, edgecolor='black')
ax1.set_title('O(n²) Algorithms', fontweight='bold')
ax1.set_ylabel('Time (seconds)')
ax1.set_xlabel('Data Type')
ax1.legend(title='Algorithm', loc='upper left')
ax1.tick_params(axis='x', rotation=0)
ax1.grid(axis='y', alpha=0.3)

o_nlogn_types.T.plot(kind='bar', ax=ax2, edgecolor='black')
ax2.set_title('O(n log n) Algorithms', fontweight='bold')
ax2.set_ylabel('Time (seconds)')
ax2.set_xlabel('Data Type')
ax2.legend(title='Algorithm', loc='upper left')
ax2.tick_params(axis='x', rotation=0)
ax2.grid(axis='y', alpha=0.3)

plt.suptitle('Figure 7: Performance on Different Data Types (100,000 elements)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('figure7_data_types.png', dpi=150, bbox_inches='tight')
plt.show()

# ============================================================
# 8. SUMMARY: Timsort vs Others (Normalized)
# ============================================================
fig, ax = plt.subplots(figsize=(12, 6))

# Comparison at 1M random data
x = ['Merge Sort', 'Quick Sort', 'Heap Sort', 'Timsort']
times = [14.61, 11.18, 27.51, 0.91]
normalized_to_timsort = [t / 0.91 for t in times]

colors = ['coral', 'orange', 'salmon', 'forestgreen']
bars = ax.bar(x, normalized_to_timsort, color=colors, edgecolor='black')
ax.set_title('Figure 8: Performance Ratio vs Timsort (1,000,000 random elements)', fontsize=14, fontweight='bold')
ax.set_ylabel('Times slower than Timsort (log scale)')
ax.set_yscale('log')
ax.grid(axis='y', alpha=0.3)

for bar, val in zip(bars, normalized_to_timsort):
    ax.annotate(f'{val:.1f}x', xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                xytext=(0, 5), textcoords="offset points", ha='center', va='bottom')

plt.tight_layout()
plt.savefig('figure8_normalized_comparison.png', dpi=150, bbox_inches='tight')
plt.show()

print("\n" + "=" * 60)
print("All figures have been generated successfully with UPDATED data!")
print("The 'Many Small Lists' figure now uses 100,000 lists for ALL sizes (including size 100).")
print("Generated files:")
print("  - figure1_small_lists.png (UPDATED)")
print("  - figure2_medium_arrays.png")
print("  - figure3_large_arrays.png")
print("  - figure4_massive_arrays.png")
print("  - figure5_data_structures.png")
print("  - figure6_half_sorted.png")
print("  - figure7_data_types.png")
print("  - figure8_normalized_comparison.png")
print("=" * 60)