import argostranslate.package

print("Fetching available translation models...")

argostranslate.package.update_package_index()

packages = argostranslate.package.get_available_packages()

english_to_hindi = [
    package
    for package in packages
    if package.from_code == "en" and package.to_code == "hi"
]

if english_to_hindi:
    package = english_to_hindi[0]

    print("\nEnglish-to-Hindi model found!")
    print("From:", package.from_name)
    print("To:", package.to_name)
    print("Version:", package.package_version)

    print("\nDownloading and installing the model...")
    argostranslate.package.install_from_path(package.download())

    print("\nModel installation completed!")

else:
    print("English-to-Hindi model not found.")
