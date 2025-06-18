def check_imports():
    libraries = {
        "Core libraries": ["numpy", "pandas", "sklearn", "h5py"],
        "Visualization": ["matplotlib", "seaborn"],
        "PyTorch": ["torch", "torchvision", "torchaudio"],
        "Jupyter Notebook": ["notebook"]
    }

    for category, modules in libraries.items():
        print(f"\nChecking {category}...")
        for module in modules:
            try:
                __import__(module)
                print(f"✔ {module}")
            except ImportError as e:
                print(f"✘ {module} - Not installed")
            except Exception as e:
                print(f"⚠ {module} - Error: {e}")

if __name__ == "__main__":
    check_imports()
