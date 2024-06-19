# Paisabachao
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0.1-red)

## Overview
**paisabachao** is a price comparison extension built with Python and Flask. It helps users compare prices of different products across multiple websites, ensuring they get the best deal.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

## Installation

To set up paisabachao on your local machine, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/rishab1wnl/Paisabachao.git
    cd Paisabachao
    ```

2. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

    Make sure your `requirements.txt` contains the following libraries:

    ```text
    Flask
    requests
    beautifulsoup4
    sqlite3  # SQLite is usually bundled with Python, no need to install separately
    ```

## Usage

1. **Run the Flask application**:

    ```bash
    python app.py
    ```

2. **Open your browser** and navigate to `http://127.0.0.1:5000`.

3. **Login** using the provided credentials:
    - **Username**: `20BCS5602`
    - **Password**: `1234567`

4. **Search for a product** and view a comparison of prices across different websites.

## Features

- **Price Comparison**: Compare product prices across multiple e-commerce sites.
- **User Authentication**: Secure login using Flask sessions.
- **Web Scraping**: Fetch product data using `requests` and `BeautifulSoup`.


**Created by [Rishab Tiwari](https://github.com/rishab1wnl)**
