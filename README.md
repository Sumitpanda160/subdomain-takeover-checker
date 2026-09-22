# 🔍 Subdomain Takeover Checker

A Python-based web reconnaissance tool that checks
subdomains for potential takeover vulnerability indicators.

## 📌 Project Overview

This project automates the process of checking a list
of subdomains for specific error signatures associated
with potential subdomain takeover vulnerabilities.

The tool searches for:
- NXDOMAIN
- NoSuchBucket

## 🚀 Features

- Read subdomains from a text file
- Send HTTP requests using Python Requests
- Search for takeover-related error signatures
- Generate a results report
- Simple command-line interface

## 🛠️ Technologies Used

- Python 3
- Requests Library
- Web Reconnaissance
- DNS Analysis
- Vulnerability Detection

## 📂 Project Structure

subdomain-takeover-checker/
│
├── src/
│   └── checker.py
│
├── screenshots/
├── logs/
├── evidence/
├── subdomains.txt
├── takeover_targets.txt
└── README.md

## ⚙️ Installation

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL

Navigate to the project:

cd subdomain-takeover-checker

Create virtual environment:

python3 -m venv venv

Activate environment:

source venv/bin/activate

Install dependencies:

pip install requests

## ▶️ Usage

Add authorized test subdomains to:

subdomains.txt

Run the checker:

python src/checker.py

Results will be saved to:

takeover_targets.txt

## 📊 Sample Output

Subdomain Takeover Checker Report

No matching signatures found.

## ⚠️ Limitations

This tool detects specific error signatures only.

Finding an error signature does not confirm
a subdomain takeover vulnerability.

Manual verification and DNS analysis are required.

The tool should only be used on authorized targets.

## 👨‍💻 Author

Sumit Kumar Panda

B.Tech Information Technology