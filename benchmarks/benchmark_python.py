"""
Benchmarking harness for Python AES-GCM encryptor utility.

Generated with the assistance of ChatGPT (GPT-5).
All generated code has been reviewed and adapted by the author.

This script benchmarks encryption and decryption times on test files
(1MB, 10MB, 100MB) using the existing encrypt/decrypt functions.
Results are printed to console and written to benchmarks/results.csv.
"""

import os
import time
import csv
from pathlib import Path

# Import your existing encrypt/decrypt functions
from src.crypto_functions import encrypt_file, decrypt_file

# Benchmark settings
TEST_FILES = [
    "benchmarks/test_1mb.bin",
    "benchmarks/test_10mb.bin",
    "benchmarks/test_100mb.bin",
    "benchmarks/test_500mb.bin",
]
RUNS_PER_FILE = 5
PASSWORD = "benchmark-password"  # fixed password for reproducibility
RESULTS_CSV = Path("benchmarks/results.csv")


def benchmark_file(file_path: str, runs: int = 5):
    """Run encrypt/decrypt benchmark for a single file."""
    file_path = Path(file_path)
    enc_path = file_path.with_suffix(".enc")
    dec_path = file_path.with_suffix(".dec")

    enc_times = []
    dec_times = []

    for i in range(runs):
        # --- Encryption ---
        start = time.perf_counter()
        encrypt_file(str(file_path), str(enc_path), PASSWORD)
        enc_time = time.perf_counter() - start
        enc_times.append(enc_time)

        # --- Decryption ---
        start = time.perf_counter()
        decrypt_file(str(enc_path), str(dec_path), PASSWORD)
        dec_time = time.perf_counter() - start
        dec_times.append(dec_time)

        # Clean up decrypted file (keep .enc to reuse for next run)
        if dec_path.exists():
            dec_path.unlink()

    # Clean up encrypted file at the end
    if enc_path.exists():
        enc_path.unlink()

    return {
        "file": file_path.name,
        "size_bytes": file_path.stat().st_size,
        "encrypt_avg": sum(enc_times) / len(enc_times),
        "decrypt_avg": sum(dec_times) / len(dec_times),
    }


def main():
    results = []

    print("Running Python benchmarks...\n")
    for test_file in TEST_FILES:
        res = benchmark_file(test_file, RUNS_PER_FILE)
        results.append(res)
        print(
            f"{res['file']}: "
            f"{res['size_bytes']/1e6:.1f} MB | "
            f"Encrypt {res['encrypt_avg']:.4f}s | "
            f"Decrypt {res['decrypt_avg']:.4f}s"
        )

    # Write to CSV
    RESULTS_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(RESULTS_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    print(f"\nBenchmark results saved to {RESULTS_CSV}")


if __name__ == "__main__":
    main()
