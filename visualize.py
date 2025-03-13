import h5py
import sys
import argparse
import matplotlib.pyplot as plt


def parse_args():
    "Parse the command line arguments"
    parser = argparse.ArgumentParser()
    parser.add_argument("-num", type=int, default=0,
                        help="Which sample to pick. 0 to 699")
    parser.add_argument("-snr", type=int, default=0,
                        help="SNR: -20 to 18 in 2 step increments (if available)")
    parser.add_argument("-mod", default="PULSED",
                        help="Modulation options: PULSED, FMCW, BPSK, AM-DSB, AM-SSB, ASK")
    parser.add_argument("-sig", default="Airborne-detection",
                        help="Signal type options: Airborne-detection, Airborne-range, Air-Ground-MTI, Ground mapping, Radar-Altimeter, SATCOM, AM radio, short-range")
    return parser.parse_args()


def main():
    args = parse_args()

    # Convert arguments to match dataset format
    mod = args.mod.upper()  # Match case in dataset
    sig = args.sig
    snr = str(args.snr)  # Ensure it's a string
    num = str(args.num)  # Ensure it's a string

    print(f"Looking for: mod={mod}, sig={sig}, snr={snr}, num={num}")

    found_data = None

    with h5py.File('RadComOta2.45GHz.hdf5', 'r') as f:
        # Print some sample keys to see the structure
        keys = list(f.keys())
        print(f"File has {len(keys)} keys. First 5 sample keys:")
        for i, key in enumerate(keys[:5]):
            print(f"- {key} (type: {type(key)})")

        # If keys are strings that look like tuples
        if len(keys) > 0 and isinstance(keys[0], str) and keys[0].startswith("("):
            search_key = f"('{mod}', '{sig}', '{snr}', '{num}')"
            if search_key in f:
                found_data = f[search_key][:]

    if found_data is None:
        print("Failed to find matching data in the HDF5 file.")
        return False

    # Determine real and imaginary parts based on data shape
    if len(found_data.shape) == 1:
        # If data is a 1D array, split in half for real and imaginary
        middle = len(found_data) // 2
        real = found_data[:middle]
        imag = found_data[middle:]
    else:
        # Adjust based on actual data structure
        print(f"Note: Multi-dimensional data found. Adjusting processing.")
        # Adjust these indices based on actual structure
        real = found_data[0, :]
        # Adjust these indices based on actual structure
        imag = found_data[1, :]

    # Equal length arrays
    min_len = min(len(real), len(imag))
    real = real[:min_len]
    imag = imag[:min_len]

    # Plot and visualize the selected sample
    plt.figure(figsize=[8, 6])
    plt.plot(real, '-go', label="Real")
    plt.plot(imag, '-bo', label="Imaginary")
    plt.legend()
    plt.title(f"Mod: {mod}, Sig: {sig}, SNR: {snr}, Num: {num}", fontsize=16)
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.show()

    return True


if __name__ == "__main__":
    sys.exit(not main())
