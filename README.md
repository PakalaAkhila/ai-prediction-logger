# AI Prediction Logger

A beginner-friendly Python command-line application for managing and storing AI prediction records using JSON files.

## Overview

This project demonstrates fundamental Python programming concepts through a practical prediction management system. Users can add predictions, view previously saved records and prevent duplicate URL entries.

## Features

- Interactive command-line menu
- Add and view prediction records
- Persistent JSON-based storage
- Duplicate URL prevention
- User input validation
- Confidence score validation between 0 and 1
- Missing file handling
- Corrupted JSON protection
- Basic data structure validation

## Technologies Used

- Python 3
- JSON
- Python Standard Library

## Project Structure

```text
ai-prediction-logger/
├── prediction_logger.py
├── predictions.json
└── README.md
```

## How to Run

Ensure Python 3 is installed on your system.

Run the following command from the project directory:

```bash
python prediction_logger.py
```

No external libraries are required.

## Example Usage

```text
===== AI Prediction Logger =====
1. Add prediction
2. View all predictions
3. Exit

Enter your choice: 1

Enter URL: https://example.com
Enter prediction: Legitimate
Enter confidence: 0.95

prediction added successfully
```

## Sample JSON Output

```json
[
    {
        "url": "https://example.com",
        "prediction": "Legitimate",
        "confidence": 0.95
    }
]
```

## Concepts Practiced

- Functions and modular programming
- Parameters and arguments
- Lists and dictionaries
- Conditional statements and loops
- File handling
- JSON serialization and deserialization
- Exception handling
- Input validation
- Debugging and manual testing

## Limitations

This application manages manually entered prediction records. It does not perform actual AI-based URL classification.

URL validation currently checks only for non-empty input, and JSON structure validation checks the top-level data type.

## Future Improvements

- Integration with a machine learning model
- Advanced URL validation
- Prediction timestamps
- Search and filtering functionality
- Automated unit testing
- Database integration

## Learning Objective

This project was developed as part of my Python-to-AI engineering learning journey to strengthen my programming fundamentals and practical problem-solving skills.
