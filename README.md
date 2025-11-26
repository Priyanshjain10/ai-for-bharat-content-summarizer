# 🤖 AI-Powered Content Summarizer

[![AWS](https://img.shields.io/badge/AWS-Bedrock-orange)](https://aws.amazon.com/bedrock/)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28-red)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green)](#)

AI-powered content summarization application using **Amazon Bedrock** and **Claude** models. Built for [AI for Bharat Workshop 1](https://hack2skill.com/aiforBharat) hackathon.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Demo](#demo)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

## 🎯 Overview

This project demonstrates the power of generative AI for document summarization. It uses **Amazon Bedrock** with **Anthropic's Claude** models to generate concise, meaningful summaries from PDF documents.

**Key Benefits:**
- ⚡ Fast processing of large documents
- 🎯 Accurate context preservation
- 💡 Simple and intuitive interface
- 🔒 Secure AWS infrastructure
- 📱 Responsive web application

## ✨ Features

- **PDF Processing**: Upload and extract text from multi-page PDF documents
- **AI Summarization**: Leverage Claude's advanced NLP capabilities
- **Real-time Processing**: Get summaries in seconds
- **User-Friendly Interface**: Clean Streamlit-based UI
- **Customizable**: Easy to modify prompts and parameters
- **Scalable**: Built on AWS serverless architecture

## 🏗️ Architecture

```
User → Streamlit UI → Python Backend → Amazon Bedrock API → Claude Model → Summary Response
```

**Components:**
1. **Frontend**: Streamlit web application
2. **Backend**: Python with Boto3 SDK
3. **AI Service**: Amazon Bedrock (Claude v2)
4. **Processing**: PyPDF2 for PDF text extraction

## 🛠️ Technologies Used

| Technology | Purpose | Version |
|------------|---------|----------|
| **Python** | Core programming language | 3.11+ |
| **Amazon Bedrock** | AI model hosting and inference | - |
| **Claude (Anthropic)** | Foundation model for summarization | v2 |
| **Streamlit** | Web application framework | 1.28+ |
| **Boto3** | AWS SDK for Python | Latest |
| **PyPDF2** | PDF text extraction | Latest |

## 📦 Installation

### Prerequisites

- Python 3.11 or higher
- AWS Account with Bedrock access
- AWS CLI configured with appropriate credentials

### Step 1: Clone the Repository

```bash
git clone https://github.com/Priyanshjain10/ai-for-bharat-content-summarizer.git
cd ai-for-bharat-content-summarizer
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure AWS Credentials

```bash
aws configure
# Enter your AWS Access Key ID
# Enter your AWS Secret Access Key
# Enter region: us-west-2
# Enter output format: json
```

## 🚀 Usage

### Running the Application

```bash
streamlit run summarization_app.py
```

The application will open in your browser at `http://localhost:8501`

### Using the App

1. **Upload PDF**: Click "Choose a PDF file" and select your document
2. **Generate Summary**: Click "Generate Summary" button
3. **View Results**: Wait a few seconds for the AI-generated summary
4. **Copy/Save**: Copy the summary text for your use

### Example

```python
# For programmatic use:
from summarization_lib import get_summary

with open('document.pdf', 'rb') as file:
    text = extract_text_from_pdf(file)
    summary = get_summary(text)
    print(summary)
```

## 📁 Project Structure

```
ai-for-bharat-content-summarizer/
│
├── summarization_app.py        # Main Streamlit application
├── summarization_lib.py        # Core summarization logic
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore rules
│
└── data/                       # Sample PDF files (optional)
    └── sample.pdf
```

## ⚙️ Configuration

### AWS Bedrock Configuration

```python
# summarization_lib.py

REGION = 'us-west-2'  # Change to your preferred region
MODEL_ID = 'anthropic.claude-v2'  # Claude model version
MAX_TOKENS = 500  # Maximum summary length
TEMPERATURE = 0.7  # Creativity vs. accuracy (0-1)
```

### Customizing Prompts

Edit the prompt in `summarization_lib.py`:

```python
prompt = f"""
Please provide a concise summary of the following document:

{file_content}

Summary:
"""
```

## 🎬 Demo

### Screenshots

**Application Interface:**
![App Screenshot](https://via.placeholder.com/800x400?text=Streamlit+App+Interface)

**Sample Summary Output:**
```
Input: 5-page AWS Leadership Principles document
Output: 3-paragraph summary capturing core principles, leadership expectations, and cultural values
Processing Time: ~3-5 seconds
```

### Video Demo

[Watch Demo Video](#) _(Add your video link here)_

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👨‍💻 Author

**Priyansh Jain**
- GitHub: [@Priyanshjain10](https://github.com/Priyanshjain10)
- Email: priyanshj1304@gmail.com
- Institution: VIT Bhopal
- Workshop: AI for Bharat - Workshop 1
- Date: November 25, 2025

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **AI for Bharat** hackathon organizers
- **Hack2Skill** for the amazing workshop
- **AWS** for providing Bedrock access
- **Anthropic** for the Claude models
- **Shashank Chinchli** (AWS Solutions Architect) for workshop guidance

## 📚 Resources

- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [AI for Bharat Website](https://hack2skill.com/aiforBharat)
- [AWS Workshop Studio](https://catalog.us-east-1.prod.workshops.aws/)

## 🔗 Related Projects

- [Bedrock Examples](https://github.com/aws-samples/amazon-bedrock-samples)
- [Streamlit Gallery](https://streamlit.io/gallery)

## 💬 Support

For issues or questions:
- Open an [Issue](https://github.com/Priyanshjain10/ai-for-bharat-content-summarizer/issues)
- Email: priyanshj1304@gmail.com

---

<div align="center">

**Built with ❤️ for AI for Bharat Workshop 1**

⭐ Star this repo if you find it helpful!

[Report Bug](https://github.com/Priyanshjain10/ai-for-bharat-content-summarizer/issues) · [Request Feature](https://github.com/Priyanshjain10/ai-for-bharat-content-summarizer/issues)

</div>
