import time
import random
import string
import sys
import gc

sys.setrecursionlimit(10_000_000)  # crescut pentru recursivitate adâncă

class SortingAlgorithms:
    @staticmethod
    def bubble_sort(arr):
        arr = arr.copy()
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr

    @staticmethod
    def insertion_sort(arr):
        arr = arr.copy()
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    @staticmethod
    def selection_sort(arr):
        arr = arr.copy()
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    @staticmethod
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = SortingAlgorithms.merge_sort(arr[:mid])
        right = SortingAlgorithms.merge_sort(arr[mid:])
        return SortingAlgorithms._merge(left, right)

    @staticmethod
    def _merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    @staticmethod
    def quick_sort(arr):
        if len(arr) <= 16:
            return SortingAlgorithms.insertion_sort(arr)
        pivot_index = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_index]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return SortingAlgorithms.quick_sort(left) + middle + SortingAlgorithms.quick_sort(right)

    @staticmethod
    def heap_sort(arr):
        arr = arr.copy()
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            SortingAlgorithms._heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            SortingAlgorithms._heapify(arr, i, 0)
        return arr

    @staticmethod
    def _heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            SortingAlgorithms._heapify(arr, n, largest)

    @staticmethod
    def timsort(arr):
        return sorted(arr)


def generate_data(size, data_type="random"):
    if data_type == "random":
        return [random.randint(0, 1_000_000) for _ in range(size)]
    elif data_type == "sorted":
        return list(range(size))
    elif data_type == "reverse":
        return list(range(size - 1, -1, -1))
    elif data_type == "almost_sorted":
        arr = list(range(size))
        num_swaps = int(size * 0.02)
        for _ in range(num_swaps):
            i, j = random.sample(range(size), 2)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
    elif data_type == "half_sorted":
        half = size // 2
        return list(range(half)) + [random.randint(half, size * 2) for _ in range(size - half)]
    elif data_type == "few_unique":
        return [random.randint(0, 9) for _ in range(size)]
    elif data_type == "floats":
        return [random.uniform(0, 1_000_000) for _ in range(size)]
    elif data_type == "strings":
        return [''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10)) for _ in range(size)]
    else:
        raise ValueError(f"Unknown data_type: {data_type}")


def test_algorithm(algo, arr):
    try:
        start = time.perf_counter()
        result = algo(arr)
        end = time.perf_counter()
        if len(arr) <= 100_000:
            assert result == sorted(arr)
        return end - start
    except Exception as e:
        print(f"      EROARE: {type(e).__name__} - {str(e)[:50]}")
        return None


def print_section(title):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def run_many_small_lists():
    print_section("MANY SMALL LISTS (100,000 lists)")
    print("Note: Now sorting 100,000 lists for ALL sizes (including size 100).")
    print(f"{'Algorithm':<15} {'Size 20 (100k)':>15} {'Size 30 (100k)':>15} {'Size 50 (100k)':>15} {'Size 100 (100k)':>15}")
    print("-" * 75)

    algorithms = ['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort', 'Timsort']
    # MODIFICARE AICI: size 100 are acum 100,000 liste în loc de 10,000
    sizes = [(20, 100000), (30, 100000), (50, 100000), (100, 100000)]

    for algo_name in algorithms:
        row = [algo_name]
        for size, num_tests in sizes:
            total_time = 0.0
            for _ in range(num_tests):
                arr = generate_data(size, "random")
                algo = getattr(SortingAlgorithms, algo_name.lower().replace(' ', '_'))
                t = test_algorithm(algo, arr)
                if t is not None:
                    total_time += t
                else:
                    total_time = float('inf')
                    break
            if total_time == float('inf'):
                row.append("ERROR")
            else:
                row.append(f"{total_time:.2f}s")
        print(f"{row[0]:<15} {row[1]:>15} {row[2]:>15} {row[3]:>15} {row[4]:>15}")


def run_medium_arrays():
    print_section("MEDIUM ARRAYS (random data) - ALL ALGORITHMS (including O(n²) for 50,000)")
    print(f"{'Algorithm':<15} {'1,000':>12} {'5,000':>12} {'10,000':>12} {'50,000':>12}")
    print("-" * 65)

    all_algorithms = ['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort', 'Timsort']
    sizes = [1000, 5000, 10000, 50000]

    for algo_name in all_algorithms:
        row = [algo_name]
        for size in sizes:
            arr = generate_data(size, "random")
            algo = getattr(SortingAlgorithms, algo_name.lower().replace(' ', '_'))
            t = test_algorithm(algo, arr)
            if t is not None:
                row.append(f"{t:.3f}s" if t < 1 else f"{t:.2f}s")
            else:
                row.append("ERROR")
        print(f"{row[0]:<15} {row[1]:>12} {row[2]:>12} {row[3]:>12} {row[4]:>12}")


def run_large_arrays():
    print_section("LARGE ARRAYS (random data) - ALL O(n log n) ALGORITHMS")
    print(f"{'Algorithm':<15} {'100,000':>12} {'500,000':>12} {'1,000,000':>12}")
    print("-" * 55)

    algorithms = ['Merge Sort', 'Quick Sort', 'Heap Sort', 'Timsort']
    sizes = [100_000, 500_000, 1_000_000]

    for algo_name in algorithms:
        row = [algo_name]
        for size in sizes:
            arr = generate_data(size, "random")
            algo = getattr(SortingAlgorithms, algo_name.lower().replace(' ', '_'))
            t = test_algorithm(algo, arr)
            if t is not None:
                row.append(f"{t:.2f}s")
            else:
                row.append("ERROR")
        print(f"{row[0]:<15} {row[1]:>12} {row[2]:>12} {row[3]:>12}")


def run_massive_arrays():
    print_section("MASSIVE ARRAYS (random data)")
    print("⚠️  These tests require a lot of RAM and time.")
    print("    - 10M / 100M: Merge Sort, Quick Sort, Heap Sort, Timsort")
    print("    - 1B:         Timsort only (implementările pure Python ar dura ore)")
    print()

    # --- 10M și 100M: toți algoritmii O(n log n) ---
    algorithms_full = ['Merge Sort', 'Quick Sort', 'Heap Sort', 'Timsort']
    sizes_full = [10_000_000, 100_000_000]

    print(f"{'Algorithm':<15} {'10,000,000':>15} {'100,000,000':>15}")
    print("-" * 50)

    for algo_name in algorithms_full:
        row = [algo_name]
        for size in sizes_full:
            print(f"  Running {algo_name} on {size:,} elements...", end="", flush=True)
            try:
                arr = generate_data(size, "random")
                algo = getattr(SortingAlgorithms, algo_name.lower().replace(' ', '_'))
                t = test_algorithm(algo, arr)
                row.append(f"{t:.2f}s" if t is not None else "ERROR")
                del arr
                gc.collect()
            except MemoryError:
                row.append("MEMORY ERROR")
                print(" MEMORY ERROR")
                continue
            except Exception as e:
                row.append(f"ERROR: {str(e)[:20]}")
                print(f" {str(e)[:50]}")
                continue
            print(" done")
        print(f"{row[0]:<15} {row[1]:>15} {row[2]:>15}")

    # --- 1B: doar Timsort ---
    print()
    print(f"{'Algorithm':<15} {'1,000,000,000':>15}")
    print("-" * 35)

    print(f"  Running Timsort on 1,000,000,000 elements...", end="", flush=True)
    try:
        arr = generate_data(1_000_000_000, "random")
        t = test_algorithm(SortingAlgorithms.timsort, arr)
        result = f"{t:.2f}s" if t is not None else "ERROR"
        del arr
        gc.collect()
        print(" done")
    except MemoryError:
        result = "MEMORY ERROR"
        print(" MEMORY ERROR")
    except Exception as e:
        result = f"ERROR: {str(e)[:20]}"
        print(f" {str(e)[:50]}")

    print(f"{'Timsort':<15} {result:>15}")


def run_data_structures():
    print_section("DATA STRUCTURES (1,000,000 elements) - O(n log n) only")
    print(f"{'Algorithm':<15} {'Random':>12} {'Sorted':>12} {'Reverse':>12} {'98% Sorted':>12} {'Few Unique':>14}")
    print("-" * 80)

    algorithms = ['Merge Sort', 'Quick Sort', 'Heap Sort', 'Timsort']
    structures = ['random', 'sorted', 'reverse', 'almost_sorted', 'few_unique']

    for algo_name in algorithms:
        row = [algo_name]
        for struct in structures:
            arr = generate_data(1_000_000, struct)
            algo = getattr(SortingAlgorithms, algo_name.lower().replace(' ', '_'))
            t = test_algorithm(algo, arr)
            if t is not None:
                row.append(f"{t:.2f}s")
            else:
                row.append("ERROR")
        print(f"{row[0]:<15} {row[1]:>12} {row[2]:>12} {row[3]:>12} {row[4]:>12} {row[5]:>14}")


def run_half_sorted():
    print_section("HALF SORTED (1,000,000 elements) - O(n log n) only")
    print(f"{'Algorithm':<15} {'Time':>12}")
    print("-" * 30)
    algorithms = ['Merge Sort', 'Quick Sort', 'Heap Sort', 'Timsort']
    for algo_name in algorithms:
        arr = generate_data(1_000_000, "half_sorted")
        algo = getattr(SortingAlgorithms, algo_name.lower().replace(' ', '_'))
        t = test_algorithm(algo, arr)
        if t is not None:
            print(f"{algo_name:<15} {t:.2f}s")
        else:
            print(f"{algo_name:<15} ERROR")


def run_data_types():
    print_section("DATA TYPES (100,000 elements) - ALL ALGORITHMS")
    print(f"{'Algorithm':<15} {'Integers':>12} {'Floats':>12} {'Strings':>12}")
    print("-" * 55)
    algorithms = ['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort', 'Timsort']
    types = ['integers', 'floats', 'strings']
    type_map = {'integers': 'random', 'floats': 'floats', 'strings': 'strings'}

    for algo_name in algorithms:
        row = [algo_name]
        for tname in types:
            arr = generate_data(100_000, type_map[tname])
            algo = getattr(SortingAlgorithms, algo_name.lower().replace(' ', '_'))
            t = test_algorithm(algo, arr)
            if t is not None:
                row.append(f"{t:.2f}s")
            else:
                row.append("ERROR")
        print(f"{row[0]:<15} {row[1]:>12} {row[2]:>12} {row[3]:>12}")


def main():
    random.seed(42)
    run_many_small_lists()
    run_medium_arrays()
    run_large_arrays()
    run_massive_arrays()
    run_data_structures()
    run_half_sorted()
    run_data_types()

    print_section("FINAL CONCLUSIONS")
    print("All tests completed successfully.")


if __name__ == "__main__":
    main()