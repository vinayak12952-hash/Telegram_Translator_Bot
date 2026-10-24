import argostranslate.translate

installed_languages = argostranslate.translate.get_installed_languages()

print("Checking installed translation models...\n")

if not installed_languages:
    print("No translation models are installed.")

for language in installed_languages:
    print(f"Language: {language.name} ({language.code})")

english = next(
    (lang for lang in installed_languages if lang.code == "en"),
    None
)

if english:
    hindi = any(
        translation.to_lang.code == "hi"
        for translation in english.translations_from
    )

    if hindi:
        print("\nEnglish-to-Hindi model is installed!")
    else:
        print("\nEnglish-to-Hindi model is not installed.")
else:
    print("\nEnglish language is not installed.")