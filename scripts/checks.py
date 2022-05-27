import subprocess


def main():
    print("Running black...")
    subprocess.run(["black", "."])
    print("Running isort...")
    subprocess.run(["isort", "."])
    print("Running flake8...")
    subprocess.run(["flake8", "."])
    print("Running mypy...")
    subprocess.run(["mypy", "."])
    print("Running tests...")
    subprocess.run(["pytest", "."])
    print("Done!")


if __name__ == "__main__":
    main()
