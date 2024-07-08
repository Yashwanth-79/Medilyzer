


![](https://github.com/Yashwanth-79/Medilyzer/blob/main/LOGO%20(1).png?raw=true)

<h1 style="text-align: left; font-size:50px;color: orange;">Welcome to Medilyzer</h1>

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
   - [Running the Application](#running-the-application)
   - [Text Input Mode](#text-input-mode)
   - [Image Input Mode](#image-input-mode)
   - [Voice Input Mode](#voice-input-mode)


## Introduction

Medilyzer is a powerful tool designed to analyze generic medicines, leveraging advanced AI models and technologies. It enables users to input medical information through text, images, and voice, providing detailed insights into generic medicines' properties and usage.

## Features

- **Text, Image, and Voice Input:** Users can input medical information through text, images, or voice inputs.
- **OCR with Tesseract:** Utilizes Tesseract OCR to extract text from images accurately.
- **Gemini Model Analysis:** Employs  Gemini model for analyzing medical information and generating detailed summaries.
- **Entity Extraction:** Detects and extracts medical entities such as symptoms, diagnosis, and treatments using AWS Comprehend Medical.
- **Comprehensive Summaries:** Generates comprehensive summaries and insights based on the analyzed medical information.


## What is Medilyzer?

Medilyzer is your ultimate solution for analyzing generic medicines with precision and ease. Leveraging advanced technologies such as optical character recognition (OCR) and AI models, Medilyzer extracts, analyzes, and summarizes medical information from text, images, and voice inputs. Whether you're a healthcare professional or a curious individual, Medilyzer empowers you with accurate insights into generic medicines.

## Uses of Our Project

### Analyze Medical Texts, Images, and Voice Inputs
- Seamlessly input medical data through text, image upload, or voice.
- Extract text from images with Tesseract OCR for accurate analysis.
- Utilize Gemini model to analyze and provide insights into medical texts, images, and voice inputs.

### Entity Extraction
- Detect and extract medical entities such as symptoms, diagnosis, and treatments using AWS Comprehend Medical.

### Detailed Summaries
- Generate comprehensive summaries and additional insights based on the analyzed medical information.

## How to Run Locally

### Installation

To run Medilyzer locally, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/Medilyzer.git
   cd Medilyzer
2. **Create and activate a virtual environmen**
   ```sh
   python -m venv venv
   `venv\Scripts\activate`
3. **Install the required dependencies:**
   ```sh
   pip install -r requirements.txt
4. Set up Tesseract OCR:

   1. Download and install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).
   2. Update the pytesseract.pytesseract.tesseract_cmd variable in the script with the path to the Tesseract executable.
5. Configure gemini and AWS credentials:

   1. Set up your gemini API key.
   2. Set up your AWS credentials for Comprehend Medical.

### Usage

1. To start the Streamlit application,
   ```run streamlit app.py ```


2. **Text Input Mode:**

- Click the "Text" button to enable text input mode.
- Enter your medical text in the provided text area.
- Click "Submit" to analyze the text.
- View the results, including extracted entities and detailed summaries.

3. **Image Input Mode:**

- Click the "Image" button to enable image input mode.
- Upload an image containing text.
- Click "Submit" to analyze the extracted text.
- View the results, including extracted entities and detailed summaries.

4. **Voice Input Mode:**

- Click the "Voice" button to enable voice input mode.
- Speak the medical information.
- Click "Submit" to analyze the spoken text.
- View the results, including extracted entities and detailed summaries.

  
   
## Tools that are used to build this application

1. **Frontend**
   
   Streamlit

   ![](https://github.com/amBITion-24/phoenix_wizards/blob/main/Medilyzer%201.0.0/Screenshot%202024-07-07%20132558.png)
    
   HTML & CSS


   ![](https://github.com/amBITion-24/phoenix_wizards/blob/main/Medilyzer%201.0.0/Screenshot%202024-07-07%20125241.png)

1. **Backend**
   
   Firebase

   ![](https://github.com/amBITion-24/phoenix_wizards/blob/main/Medilyzer%201.0.0/Screenshot%202024-07-07%20125139.png)


   pillow

   ![](https://github.com/amBITion-24/phoenix_wizards/blob/main/Medilyzer%201.0.0/Screenshot%202024-07-07%20130110.png)


   Gemini

   ![](https://github.com/amBITion-24/phoenix_wizards/blob/main/Medilyzer%201.0.0/Screenshot%202024-07-07%20142001.png)

   
