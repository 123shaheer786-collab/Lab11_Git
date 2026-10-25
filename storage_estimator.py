# Storage Estimator
# Converts a file size in MB to KB and bytes.

def main():
    print("Storage Estimator")
    size_mb = float(input("Enter file size in MB: "))

    size_kb = size_mb * 1024
    size_bytes = size_kb * 1024
    print(size_mb, "MB =", round(size_kb, 2), "KB")
    print(size_mb, "MB =", round(size_bytes, 2), "bytes")

  main()