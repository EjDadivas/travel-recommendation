# Travel Recommender Documentation

Welcome to the Travel Recommender documentation. This document provides an overview of the project, installation instructions, usage guidelines, and information about project structure and testing.

## Table of Contents

1. [Introduction](#1-introduction)
2. [Installation](#2-installation)
3. [Usage](#3-usage)
4. [Configuration](#4-configuration)
5. [Contributing](#5-contributing)
6. [License](#6-license)
7. [Project Structure](#7-project-structure)
8. [HTML Templates and Static Files](#8-html-templates-and-static-files)

---

## 1. Introduction

The Travel Recommender is a FastAPI-based web application that recommends travel destinations based on user input, including the destination country and season.

## 2. Installation

To run the Travel Recommender locally, follow these steps:

1. Clone the repository:
   git clone https://github.com/EjDadivas/travelRecommendation.git

2. Change into the project directory:
   cd travelRecommendation

3. Install dependencies using pip:
   pip install -r requirements.txt

4. Run the application:
   uvicorn main:app --host localhost --port 3000 --reload --access-log

5. Access the application in your web browser at [http://localhost:3000](http://localhost:3000)

## 3. Usage

- Access the application in your web browser at `/travel-recommendations`.
- Provide the following query parameters to get travel recommendations:
- `country` (string): Name of the country (e.g., "Canada").
- `season` (string): Season (e.g., "Winter", "Summer", "Spring", "Autumn").
- If no parameters are provided, the application will display a homepage.
- The endpoint validates input parameters and displays travel recommendations or errors.

## 4. Configuration

Configure the application by setting environment variables, including the OpenAI API key, in a `.env` file.

## 5. Project Structure

The project structure is organized as follows:

- `main.py`: The main FastAPI application.
- `api` folder: Contains API-related modules.
- `routes.py`: Defines API routes and endpoints.
- `utils.py`: Contains utility functions for input validation and recommendation generation.
- `tests` folder: Contains unit tests for the project.

## 6. HTML Templates and Static Files

- `static` folder: Contains static assets such as CSS styles and images.
- `templates` folder: Contains HTML templates used for rendering web pages, including `home.html`.

---
