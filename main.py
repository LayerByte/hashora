import hashlib
from pathlib import Path


SUPPORTED_ALGORITHMS = {
    "1": "md5",
    "2": "sha1",
    "3": "sha256",
    "4": "sha512",
}

CHUNK_SIZE = 8192


# --- Shows the app title and purpose.
def print_banner() -> None:
    print("=" * 56)
    print("hashora")
    print("Educational file hash checker for integrity verification.")
    print("School Purpose Only.")
    print("=" * 56)


# --- Gets a file path from the user.
def get_file_path() -> Path:
    while True:
        file_path = Path(input("Enter file path: ").strip().strip('"'))

        if file_path.is_file():
            return file_path

        print("File not found. Please enter a valid file path.")


# --- Displays the supported hash choices.
def show_algorithm_menu() -> None:
    print("\nSupported hash algorithms:")
    print("  1. MD5")
    print("  2. SHA1")
    print("  3. SHA256")
    print("  4. SHA512")
    print("  5. All algorithms")


# --- Lets the user choose one hash type or all of them.
def get_selected_algorithms() -> list[str]:
    while True:
        show_algorithm_menu()
        choice = input("Select an option: ").strip()

        if choice == "5":
            return list(SUPPORTED_ALGORITHMS.values())

        if choice in SUPPORTED_ALGORITHMS:
            return [SUPPORTED_ALGORITHMS[choice]]

        print("Invalid option. Please choose 1, 2, 3, 4, or 5.")


# --- Converts bytes into a readable file size.
def format_file_size(size_bytes: int) -> str:
    units = ["B", "KB", "MB", "GB", "TB"]
    size = float(size_bytes)

    for unit in units:
        if size < 1024 or unit == units[-1]:
            return f"{size:.2f} {unit}"
        size /= 1024

    return f"{size_bytes} B"


# --- Calculates one hash for the selected file.
def calculate_hash(file_path: Path, algorithm: str) -> str:
    hash_object = hashlib.new(algorithm)

    with file_path.open("rb") as file:
        while chunk := file.read(CHUNK_SIZE):
            hash_object.update(chunk)

    return hash_object.hexdigest()


# --- Calculates all requested hashes.
def calculate_hashes(file_path: Path, algorithms: list[str]) -> dict[str, str]:
    hashes = {}

    for algorithm in algorithms:
        print(f"Calculating {algorithm.upper()}...")
        hashes[algorithm] = calculate_hash(file_path, algorithm)

    return hashes


# --- Prints file details and calculated hashes.
def display_results(file_path: Path, hashes: dict[str, str]) -> None:
    file_size = file_path.stat().st_size

    print("\nFile information")
    print("-" * 56)
    print(f"Name: {file_path.name}")
    print(f"Path: {file_path}")
    print(f"Size: {format_file_size(file_size)} ({file_size} bytes)")

    print("\nCalculated hashes")
    print("-" * 56)
    for algorithm, hash_value in hashes.items():
        print(f"{algorithm.upper():<7}: {hash_value}")


# --- Compares a calculated hash with an expected one.
def compare_hash(hashes: dict[str, str]) -> None:
    answer = input("\nCompare with an expected hash? (y/n): ").strip().lower()

    if answer != "y":
        return

    if len(hashes) == 1:
        algorithm = next(iter(hashes))
    else:
        algorithm = choose_hash_for_comparison(hashes)

    expected_hash = input("Enter expected hash: ").strip().lower()
    calculated_hash = hashes[algorithm].lower()

    print("\nComparison result")
    print("-" * 56)
    print(f"Algorithm: {algorithm.upper()}")

    if calculated_hash == expected_hash:
        print("Result: MATCH")
        print("The file hash matches the expected value.")
    else:
        print("Result: NO MATCH")
        print("The file hash does not match the expected value.")


# --- Picks which calculated hash should be compared.
def choose_hash_for_comparison(hashes: dict[str, str]) -> str:
    algorithms = list(hashes.keys())

    while True:
        print("\nChoose a hash to compare:")
        for index, algorithm in enumerate(algorithms, start=1):
            print(f"  {index}. {algorithm.upper()}")

        choice = input("Select an option: ").strip()

        try:
            selected_index = int(choice) - 1
            if 0 <= selected_index < len(algorithms):
                return algorithms[selected_index]
        except (ValueError, IndexError):
            pass

        print("Invalid option. Please try again.")


# --- Runs the application.
def main() -> None:
    print_banner()

    try:
        file_path = get_file_path()
        algorithms = get_selected_algorithms()
        hashes = calculate_hashes(file_path, algorithms)

        display_results(file_path, hashes)
        compare_hash(hashes)
    except PermissionError:
        print("\nPermission error: this file cannot be read.")
    except OSError as error:
        print(f"\nFile error: {error}")
    except KeyboardInterrupt:
        print("\n\nCancelled by user.")


if __name__ == "__main__":
    main()
