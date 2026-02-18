# NLP Course Exercises - IME USP 📚🇧🇷

> Practical exercises on Natural Language Processing using spaCy, based on the curriculum of the IME-USP (University of São Paulo) course.

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?style=flat&logo=python)
![spaCy](https://img.shields.io/badge/NLP-spaCy-green?style=flat&logo=spacy)
![Status](https://img.shields.io/badge/Status-Study-yellow)

## 📖 About the Project

This repository contains solutions to introductory NLP exercises. The goal is to explore the basic capabilities of the **spaCy** library applied to Portuguese literature.

The target text for analysis is the **3rd Chapter of "Memórias Póstumas de Brás Cubas"**, a classic masterpiece by **Machado de Assis**. The code extracts linguistic features to better understand the structure and entities within the text.

## 🚀 Features & Exercises

The script performs three main linguistic tasks:

### 1. Named Entity Recognition (NER)
* **Goal:** Identify characters mentioned in the text.
* **Method:** Iterates through `doc.ents` filtering for the label `PER` (Person).

### 2. Part-of-Speech Tagging (POS) & Frequency
* **Goal:** Extract and count all pronouns used in the chapter.
* **Method:** Uses `collections.Counter` to map tokens tagged as `PRON`.

### 3. Dependency Parsing Visualization
* **Goal:** Visualize the grammatical structure of a random sentence.
* **Method:** Uses `displacy.serve` with a custom **Dark Mode** theme (custom colors and fonts) to render the dependency tree.

## 💡 Going Further (Advanced Project)

This repository focuses on **basic concepts**. If you are looking for a more complex, Object-Oriented application of spaCy with custom cleaning pipelines and rule-based extractors, please check out my other repository:

👉 **[Semantic Recipe Extractor](https://github.com/HelloAkiraS/Semantic_Recipe_Extractor)**

*There, I apply these concepts to build a real-world ETL pipeline for culinary data.*

## 🛠️ Tech Stack

* **Python 3.12
* **spaCy** (Model: `pt_core_news_sm`)
* **DisplaCy** (Visualization)

## 📦 Installation

1.  **Clone the repo:**
    
    git clone [https://github.com/HelloAkiraS/Spacy.git](https://github.com/HelloAkiraS/Spacy.git)

2.  **Install spaCy:**
    
    pip install spacy

3.  **Download the Portuguese Model:**
    *Note: This project uses the small model (`sm`) for efficiency.*
    
    python -m spacy download pt_core_news_sm

## 💻 Usage

Run the script directly via terminal. 
*Note: Exercise 3 will start a local web server.*

    python main.py

Then, open your browser at `http://localhost:5001` to see the dependency tree visualization.
*Note: default port for displacy is 5000. You can change it by setting a different "port" value onto displacy's serve method.*

## 👨‍💻 Author

**HelloAkiraS**
*Student at Fatec Rubens Lara*

---
*Exercises inspired by the "NLPortugues" course material from IME-USP.*
