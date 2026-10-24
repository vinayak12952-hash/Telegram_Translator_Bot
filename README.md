# Telegram_Translator_Bot
# 🌐 English-to-Hindi Telegram Translator

A Python-based Telegram bot that translates English text into Hindi using **Argos Translate**, an open-source, offline-capable machine translation library.

This project combines Python modules, input validation, a translation engine, and Telegram bot integration to provide a simple translation experience directly inside Telegram.

## ✨ Features

* **English-to-Hindi Translation:** Translates English text into Hindi using Argos Translate.
* **Telegram Integration:** Translate messages by sending them to your Telegram bot.
* **Input Validation:** Rejects empty text, whitespace-only input, and inputs exceeding the 5,000-character limit.
* **Modular Architecture:** Separates message handling, input validation, and translation logic into individual Python files.
* **Offline Translation Engine:** Uses a locally installed translation model, so translation itself does not require an external translation API.
* **Simple Interface:** Interact with the translator through Telegram without opening a separate application.

## 🛠️ Technologies Used

| Technology                   | Purpose                                    |
| ---------------------------- | ------------------------------------------ |
| Python                       | Core programming language                  |
| Argos Translate              | Machine translation                        |
| pyTelegramBotAPI (`telebot`) | Telegram bot integration                   |
| Telegram Bot API             | Communication between Telegram and the bot |

## 📁 Project Structure

```text
A_Translator_Ecosystem/
│
├── Telegram_Bot.py
├── Text_Check.py
├── Translator_Engine.py
├── download_model.py
├── Check.py
└── README.md
```

### File Descriptions

#### 1. `Telegram_Bot.py`

Handles communication with Telegram.

Responsibilities:

* Responds to `/start` and `/help`.
* Receives incoming messages.
* Sends text to the validation module.
* Returns the result to the user.
* Keeps the bot running through continuous polling.

#### 2. `Text_Check.py`

Validates incoming text before passing it to the translation engine.

Validation includes:

* Checking whether the input is a string.
* Rejecting empty or whitespace-only text.
* Enforcing a 5,000-character limit.

If the input is valid, the text is passed to `Translator_Engine.py`.

#### 3. `Translator_Engine.py`

Connects the application to Argos Translate.

Responsibilities:

* Identifies English as the source language.
* Identifies Hindi as the target language.
* Uses Argos Translate to translate the supplied sentence.
* Returns the translated text to the validation module.

#### 4. `download_model.py`

Finds the available English-to-Hindi translation package and downloads and installs it.

Run this script when setting up the project on a new environment, if the model is not already installed.

#### 5. `check_model.py`

Checks whether translation languages and the English-to-Hindi translation capability are installed.

Use it to verify the model installation before running the bot.

## ⚙️ Requirements

Before running the project, make sure you have:

* Python installed.
* A Telegram account.
* A Telegram bot token.
* The required Python packages.
* The English-to-Hindi Argos Translate model installed.

## 🚀 Installation and Setup

### Step 1: Clone the Repository

If the project is hosted on GitHub:

```bash
git clone <your-repository-url>
cd A_Translator_Ecosystem
```

Alternatively, download the project files and open the project folder in your terminal.

### Step 2: Create a Virtual Environment (Recommended)

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

A virtual environment keeps this project's Python dependencies separate from other projects.

### Step 3: Install Dependencies

Install the required packages:

```bash
python -m pip install argostranslate pyTelegramBotAPI
```

### Step 4: Configure the Telegram Bot

1. Open Telegram.
2. Search for the official `@BotFather` account.
3. Create a bot using `/newbot`.
4. Follow the instructions to choose a bot name and username.
5. Copy the generated bot token.
6. Configure your application to read the token securely.

**Security recommendation:** Do not publish your bot token in your source code or commit it to GitHub. Store it in an environment variable instead.

For example, on Windows Command Prompt:

```cmd
set TELEGRAM_BOT_TOKEN=your_token_here
```

Your Python application must read this environment variable to use this configuration.

### Step 5: Download the Translation Model

Run:

```bash
python download_model.py
```

This script should download and install the English-to-Hindi model through Argos Translate.

You generally only need to install the model once per Python environment and Argos Translate data installation.

The initial download requires an internet connection.

### Step 6: Verify the Installation

Run:

```bash
python check_model.py
```

Confirm that English-to-Hindi translation is installed before proceeding.

### Step 7: Start the Telegram Bot

Run the bot's main Python file:

```bash
python Telegram_Bot.py
```

When the bot starts successfully, the terminal should display a message indicating that the bot is running.

## 💬 How to Use

1. Open Telegram.
2. Search for your bot using its username.
3. Open the chat and press **Start**, or send `/start`.
4. Send a message in English.
5. The bot passes the message through the validation module.
6. If the input is valid, the translation engine processes it.
7. The bot replies with the translated Hindi text.

### Example

**Input:**

```text
Hi, I am a coder.
```

**Output:**

The bot returns a Hindi translation of the supplied sentence.

Translation wording may vary depending on the installed model.

## 🔄 How It Works

The application follows a modular processing flow:

```text
             User sends a message
                      |
                      v
                Telegram Bot
                      |
                      v
                 Text_Check
                      |
                      v
              Input Validation
                      |
              +-------+-------+
              |               |
           Invalid           Valid
              |               |
              v               v
        Error Message    Translator_Engine
                              |
                              v
                       Argos Translate
                              |
                              v
                       Hindi Translation
                              |
                              v
                        Telegram Reply
```

This architecture separates the Telegram interface from the validation rules and translation logic, making the project easier to understand and maintain.

## 🌍 Translation and Internet Connectivity

The translation engine uses an installed Argos Translate model to process text locally.

This means that, once the required model is installed, **the translation operation itself can work without contacting an external translation service**.

However, the Telegram bot needs an internet connection to receive messages and send replies through Telegram.

The package setup script also needs internet access to retrieve the package index and download the model when required.

## ⚠️ Current Limitations

* **Translation direction:** English to Hindi only.
* **Input length:** The validation module enforces a 5,000-character limit.
* **Translation quality:** Results depend on the installed translation model.
* **Telegram connectivity:** The bot needs internet access to communicate with Telegram.
* **Message types:** The current message handler is designed primarily for text messages. Images, stickers, and other unsupported message types may require additional handling.
* **Error recovery:** More comprehensive handling of model failures and unexpected runtime errors can be added in future versions.
* **Availability:** The bot runs while its Python process is running. Continuous public availability requires hosting it on an appropriate server or platform.

## 🔒 Security

* Never share your Telegram bot token publicly.
* Keep credentials out of GitHub repositories.
* Use environment variables for sensitive configuration.
* Add `.env` files, virtual environments, and other local-only files to `.gitignore` when appropriate.
* If a real bot token is exposed, revoke it through BotFather and generate a replacement.

## 🧪 Testing

Before releasing a new version, test the following cases:

| Test Case                                          | Expected Result                     |
| -------------------------------------------------- | ----------------------------------- |
| A normal English sentence                          | Returns a Hindi translation         |
| A longer English paragraph                         | Attempts to translate the paragraph |
| Empty text passed to the validation function       | Returns an error message            |
| Whitespace-only text                               | Returns an error message            |
| Text exceeding 5,000 characters                    | Returns an error message            |
| Non-string input passed to the validation function | Returns an error message            |
| A sticker or image sent to the Telegram bot        | Should be handled safely            |
| Translation model unavailable                      | Should be handled gracefully        |

## 🔮 Possible Future Improvements

Ideas for future versions include:

* Support for Hindi-to-English translation.
* Support for additional language pairs.
* Improved handling of unsupported Telegram messages.
* More comprehensive exception handling.
* Automated unit tests.
* Translation history.
* A `/help` command with detailed instructions.
* Better feedback for long translations.
* Deployment to a server for continuous availability.

These are potential enhancements, not features currently claimed by this version.

## 🎯 Project Goals

This project was developed to practise and apply:

* Python functions and modules.
* Input validation.
* External library integration.
* Local machine translation.
* Telegram bot development.
* Modular application architecture.
* Error handling and debugging.

## 📜 License

No license has been specified yet.


## 👨‍💻 Author

**Vinayak**

Built with Python, Argos Translate, and the Telegram Bot API.

---

*An independent Python project exploring local machine translation and Telegram bot development.*
 
