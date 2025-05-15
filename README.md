# Phone Handling System

A simple command-line Python application to manage phone records—add, edit, delete entries—persisted in a JSON file.

## Table of Contents

* [Features](#features)
* [Tech Stack](#tech-stack)
* [Prerequisites](#prerequisites)
* [Getting Started](#getting-started)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [Configuration](#configuration)
* [Contributing](#contributing)


## Features

* **Add Phone**: Insert new phone records with attributes like brand, model, and price.
* **Edit Phone**: Update existing phone details.
* **Delete Phone**: Remove phone entries by ID.
* **List Phones**: Display all saved phone records in a formatted list.
* **Persistent Storage**: Data is saved and loaded from a JSON file (`phones.json`).
* **Command-Line Interface**: Interactive menu-driven UI in the terminal.

## Tech Stack

* **Language**: Python 3.6+
* **Data Storage**: JSON file

## Prerequisites

* Python 3.6 or higher installed on your system.
* (Optional) Virtual environment tool (`venv` or `virtualenv`).

## Getting Started

1. **Clone the repository**:

   ```bash
   git clone https://github.com/MadushanR/Python_Assignment4.git
   cd Python_Assignment4
   ```
2. **(Optional) Create and activate a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\\Scripts\\activate
   ```
3. **Install dependencies** (if any are listed in `requirements.txt`):

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script:

   ```bash
   python program.py
   ```
2. Use the menu options to:

   * **1**: List all phones
   * **2**: Add a new phone
   * **3**: Edit an existing phone
   * **4**: Delete a phone
   * **5**: Exit the application
3. All changes will be saved automatically to `phones.json`.

## Project Structure

```plaintext
Python_Assignment4/
├── program.py        # Main CLI application
├── models.py           # Phone data model and JSON handlers
├── utils.py            # Helper functions (input validation, file I/O)
├── phones.json         # Data file storing phone records (auto-generated)
├── requirements.txt    # Project dependencies (if any)
└── README.md # This file
```

## Configuration

* **Data File**: By default, the application uses `phones.json` in the project root.
* **Change Path**: To use a different file, update the `DATA_FILE` constant in `models.py`.

## Contributing

1. ⭐️ Fork the repository
2. 🔀 Create a new branch (`git checkout -b feature/YourFeature`)
3. 🛠️ Implement your feature or bug fix
4. 📄 Commit your changes (`git commit -m "Add feature"`)
5. 🚀 Push to your branch (`git push origin feature/YourFeature`)
6. 🔎 Open a Pull Request


---

> *Built with 🐍 and 📱 for simple phone record management!*
