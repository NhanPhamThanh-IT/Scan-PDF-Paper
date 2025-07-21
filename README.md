<div align="justify">

# <div align="center">📄 Scan-PDF-Paper</div>

<div align="center">

A powerful document analysis tool that extracts text from various document formats (PDF, DOCX, TXT) and performs intelligent topic classification and keyword matching analysis.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/) [![Streamlit](https://img.shields.io/badge/Streamlit-1.47.0+-red.svg)](https://streamlit.io/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-orange.svg)](https://pytorch.org/) [![Transformers](https://img.shields.io/badge/🤗_Transformers-4.0+-green.svg)](https://huggingface.co/transformers/) [![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/NhanPhamThanh-IT/Scan-PDF-Paper/graphs/commit-activity)

[![GitHub stars](https://img.shields.io/github/stars/NhanPhamThanh-IT/Scan-PDF-Paper.svg?style=social&label=Star)](https://github.com/NhanPhamThanh-IT/Scan-PDF-Paper) [![GitHub forks](https://img.shields.io/github/forks/NhanPhamThanh-IT/Scan-PDF-Paper.svg?style=social&label=Fork)](https://github.com/NhanPhamThanh-IT/Scan-PDF-Paper/fork)

</div>

## 🌟 Features

- **Multi-format Document Support**: Extract text from PDF, DOCX, and TXT files
- **Intelligent Topic Classification**: AI-powered topic classification using Sentence Transformers
- **Keyword Matching Analysis**: Calculate topic relevance based on predefined keyword sets
- **Interactive Web Interface**: User-friendly Streamlit-based web application
- **Real-time Analysis**: Get instant results with visual progress indicators
- **Multiple Analysis Pages**: Main analysis page and advanced features

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/NhanPhamThanh-IT/Scan-PDF-Paper.git
   cd Scan-PDF-Paper
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**

   ```bash
   streamlit run app/main.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

## 📖 Usage

### Main Analysis Page

1. **Select a Topic**: Choose from predefined topics including:

   - AI & Technology
   - Healthcare
   - Finance
   - Environment
   - Cybersecurity
   - Software Development
   - And more...

2. **Upload Document**: Support for multiple file formats:

   - PDF files
   - Microsoft Word documents (.docx)
   - Plain text files (.txt)

3. **Get Analysis Results**: View detailed analysis including:
   - Total word count
   - Keyword matches found
   - Topic relevance percentage
   - Detailed breakdown of analysis

### Advanced Features

Access the Advanced page for additional functionality and enhanced analysis options.

## 🏗️ Project Structure

```
Scan-PDF-Paper/
├── app/
│   ├── main.py                 # Main Streamlit application
│   ├── assets/
│   │   └── themes.css          # CSS styling
│   ├── core/
│   │   ├── AI/
│   │   │   └── TopicClassifier.py  # AI-powered topic classification
│   │   └── Utils/
│   │       ├── DataHandling.py     # Data processing utilities
│   │       ├── FileHandling.py     # File extraction utilities
│   │       └── TextHandling.py     # Text processing utilities
│   ├── dataset/
│   │   ├── metadata/
│   │   │   └── topics.json         # Available topics list
│   │   └── topics_keywords/        # Keyword datasets for each topic
│   │       ├── AI.json
│   │       ├── Healthcare.json
│   │       ├── Finance.json
│   │       └── ...
│   ├── pages/
│   │   ├── MainPage.py             # Main analysis interface
│   │   ├── AdvancesPage.py         # Advanced features
│   │   └── HelpsPage.py            # Help and documentation
│   ├── settings/
│   │   └── ThemeManager.py         # Theme management
│   └── ui/
│       ├── PageHeaderComponent.py  # Reusable header component
│       ├── ResultComponent.py      # Results display component
│       └── TabsComponent.py        # Navigation tabs component
├── requirements.txt                # Python dependencies
└── README.md                      # Project documentation
```

## 🛠️ Technical Details

### Core Technologies

- **Streamlit**: Web framework for the user interface
- **PyMuPDF (fitz)**: PDF text extraction
- **python-docx**: Microsoft Word document processing
- **Sentence Transformers**: AI-powered text analysis
- **spaCy**: Natural language processing and stop words removal

### AI-Powered Classification

The application uses the `all-MiniLM-L6-v2` model from Sentence Transformers to:

- Generate embeddings for input text
- Compare against predefined topic embeddings
- Calculate cosine similarity scores
- Provide confidence percentages for topic classification

### Text Processing Pipeline

1. **Document Parsing**: Extract raw text from uploaded files
2. **Text Preprocessing**: Remove stop words and normalize text
3. **Keyword Analysis**: Match against topic-specific keyword sets
4. **AI Classification**: Use machine learning for intelligent topic detection
5. **Results Generation**: Calculate relevance scores and generate insights

## 📊 Supported Topics

The application supports analysis across 21+ topic categories:

- **Technology**: AI, Software, Cybersecurity
- **Sciences**: Healthcare, Environment, Science
- **Business**: Finance, Economy, Business
- **Society**: Education, Politics, Law, Culture
- **Lifestyle**: Sports, Travel, Food, Art
- **Others**: Media, Religion, Agriculture, Energy, Security

## 🧪 Testing

Run the test suite using pytest:

```bash
pytest
```

Test configuration is available in `pytest.ini`.

## 📋 Requirements

### Core Dependencies

- `streamlit>=1.47.0` - Web application framework
- `PyMuPDF` - PDF processing
- `python-docx` - Word document processing
- `sentence-transformers>=2.6.1` - AI text analysis
- `torch>=2.0.0` - Machine learning backend
- `spacy` - Natural language processing

### Development Dependencies

- `pytest` - Testing framework
- `pytest-mock` - Testing utilities

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: Visit the Help & Documentation page in the application
- **Issues**: Report bugs or request features via GitHub Issues
- **Discussions**: Join project discussions on GitHub

## 🔮 Future Enhancements

- Support for additional file formats (RTF, ODT)
- Batch processing capabilities
- Export results to various formats
- Custom topic creation
- Advanced visualization features
- REST API integration

## ⚡ Performance Notes

- First-time loading may take longer due to AI model initialization
- Large documents (>10MB) may require additional processing time
- Recommended RAM: 4GB+ for optimal performance

---

**Built with ❤️ using Python and Streamlit**

</div>
