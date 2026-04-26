# 📚 DocuMentor

> AI-powered document learning platform that helps you upload PDFs, generate summaries, ask questions, take quizzes, and get detailed explanations—all in one place.

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 🎯 Overview

**DocuMentor** is a full-stack application that leverages **Google Gemini AI** to help students and professionals learn more effectively from documents. Upload any PDF, and our AI will help you:

- 📝 **Summarize** documents automatically
- ❓ **Ask Questions** and get intelligent answers
- 🧠 **Take Quizzes** to test your knowledge
- 💡 **Get Explanations** for complex topics
- 🔍 **Search** through your documents intelligently

---

## ✨ Key Features

- ✅ **PDF Upload & Processing** - Upload multiple PDFs with automatic processing
- ✅ **AI Summarization** - Generate concise summaries using Google Gemini
- ✅ **Intelligent Search** - Find answers from your documents using AI
- ✅ **Auto Quiz Generation** - Create quizzes automatically from document content
- ✅ **Detailed Explanations** - Get AI-powered explanations for any topic
- ✅ **User Authentication** - Secure login with JWT tokens
- ✅ **Document Management** - Organize and manage your uploaded documents
- ✅ **Responsive UI** - Works seamlessly on desktop and mobile
- ✅ **Real-time Processing** - Fast AI responses using Google Gemini 2.0 Flash

---

## 🛠️ Tech Stack

### **Frontend**
- **React 18** - UI library
- **Vite** - Fast build tool
- **Tailwind CSS** - Styling
- **Radix UI** - Component library
- **Redux Toolkit** - State management
- **Axios** - HTTP client
- **React PDF Viewer** - PDF preview

### **Backend (Node.js)**
- **Express.js** - Web framework
- **MongoDB** - Database
- **Mongoose** - ODM
- **JWT** - Authentication
- **Multer** - File uploads
- **Puppeteer** - PDF generation
- **Nodemon** - Development tool

### **AI Service (Python)**
- **FastAPI** - API framework
- **Google Generative AI** - Gemini API integration
- **ChromaDB** - Vector database
- **Sentence Transformers** - Embeddings
- **PyPDF** - PDF processing

### **Deployment**
- **Docker** - Containerization
- **Docker Compose** - Multi-service orchestration

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

### Required
- **Node.js** (v16 or higher) - [Download](https://nodejs.org/)
- **Python** (v3.9 or higher) - [Download](https://www.python.org/)
- **Docker** (optional but recommended) - [Download](https://www.docker.com/)
- **Git** - [Download](https://git-scm.com/)

### Accounts & API Keys
- **MongoDB Atlas** - Create a free account at [mongodb.com](https://www.mongodb.com/cloud/atlas)
- **Google Gemini API Key** - Get free API key from [aistudio.google.com](https://aistudio.google.com/app/apikey)

---

## 📁 Project Structure

```
DocuMentor/
├── frontend/                      # React + Vite application
│   ├── src/
│   │   ├── api/                  # API service calls
│   │   ├── components/           # React components
│   │   ├── pages/                # Page components
│   │   ├── store/                # Redux store
│   │   ├── utils/                # Utility functions
│   │   ├── App.jsx              
│   │   └── main.jsx              
│   ├── package.json
│   └── vite.config.js
│
├── server/                        # Node.js + Express backend
│   ├── controllers/              # Business logic
│   ├── models/                   # MongoDB schemas
│   ├── routes/                   # API routes
│   ├── middlewares/              # Express middlewares
│   ├── utils/                    # Helper functions
│   ├── uploads/                  # User uploaded files
│   ├── index.js                 # Entry point
│   └── package.json
│
├── AIserver/                      # Python AI service
│   ├── app/
│   │   ├── api/                  # API endpoints
│   │   │   ├── embed.py         # Document embeddings
│   │   │   ├── search.py        # Semantic search
│   │   │   ├── summarize.py     # Text summarization
│   │   │   ├── quiz.py          # Quiz generation
│   │   │   ├── explanation.py   # Topic explanations
│   │   │   └── summarize_doc.py # Document summarization
│   │   ├── core/
│   │   │   ├── config.py        # Configuration
│   │   │   ├── model.py         # AI models & Gemini setup
│   │   │   └── paths.py         # Path definitions
│   │   ├── services/            # Business logic services
│   │   ├── prompts/             # AI prompt templates
│   │   └── __init__.py
│   ├── chroma_dbs/              # Vector database storage
│   ├── main.py                  # FastAPI application
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env.example
│
├── docker-compose.yml           # Multi-service orchestration
└── README.md                    # This file
```

---

## 🚀 Installation & Setup

### Option 1: Using Docker (Recommended)

This is the easiest way to get everything running!

#### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/DocuMentor.git
cd DocuMentor
```

#### Step 2: Set Up Environment Variables
Create a `.env` file in the root directory:
```bash
# MongoDB Connection
MONGO_DB_URI=mongodb+srv://username:password@cluster.mongodb.net/documenor

# JWT Secrets
JWT_ACCESS_TOKEN_SECRET=your_random_secret_key_here
JWT_REFRESH_TOKEN_SECRET=your_another_random_secret_key

# Server Port
PORT=5000
```

Create `AIserver/.env`:
```bash
# Google Gemini API Key
GEMINI_API_KEY=your_gemini_api_key_from_aistudio
```

#### Step 3: Build and Run with Docker
```bash
docker-compose up --build
```

The application will be available at:
- **Frontend**: http://localhost:3000
- **Backend**: http://localhost:5000
- **AI Service**: http://localhost:8000

---

### Option 2: Manual Installation

#### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/DocuMentor.git
cd DocuMentor
```

#### Step 2: Set Up Environment Variables

**Root `.env` file:**
```bash
MONGO_DB_URI=mongodb+srv://username:password@cluster.mongodb.net/documenor
JWT_ACCESS_TOKEN_SECRET=your_random_secret_key_here
JWT_REFRESH_TOKEN_SECRET=your_another_random_secret_key
PORT=5000
```

**`AIserver/.env` file:**
```bash
GEMINI_API_KEY=your_gemini_api_key_from_aistudio
```

#### Step 3: Install Backend Dependencies
```bash
cd server
npm install
```

#### Step 4: Install Frontend Dependencies
```bash
cd ../frontend
npm install
```

#### Step 5: Set Up Python Environment
```bash
cd ../AIserver
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## ⚙️ Configuration

### Google Gemini API Setup

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click "Get API Key"
3. Create a new API key
4. Copy the key and add it to `AIserver/.env`:
```bash
GEMINI_API_KEY=your_api_key_here
```

### MongoDB Setup

1. Create a free account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create a new project and cluster
3. Add your IP to the network access list
4. Create a database user
5. Copy the connection string and add to root `.env`:
```bash
MONGO_DB_URI=mongodb+srv://username:password@cluster.mongodb.net/documenor
```

---

## 🏃 Running the Application

### With Docker (Recommended)
```bash
docker-compose up
```

Access the application:
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000/documentor
- AI Service: http://localhost:8000

### Without Docker

**Terminal 1 - Start Backend:**
```bash
cd server
npm run dev
```

**Terminal 2 - Start Frontend:**
```bash
cd frontend
npm run dev
```

**Terminal 3 - Start AI Service:**
```bash
cd AIserver
source venv/bin/activate  # or venv\Scripts\activate on Windows
python main.py
```

---

## 📡 API Endpoints

### Authentication Routes
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/documentor/user-auth/signup` | Register new user |
| POST | `/documentor/user-auth/login` | User login |
| POST | `/documentor/user-auth/logout` | User logout |
| POST | `/documentor/user-auth/refresh` | Refresh JWT token |

### Document Routes
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/documentor/document/upload` | Upload PDF document |
| GET | `/documentor/document/list` | Get all user documents |
| GET | `/documentor/document/:id` | Get specific document |
| DELETE | `/documentor/document/:id` | Delete document |

### Summarization Routes
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/documentor/summarize/text` | Summarize text content |
| POST | `/documentor/summarize/document` | Summarize entire document |
| GET | `/documentor/summarize/:id` | Get saved summary |

### Quiz Routes
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/documentor/quiz/generate` | Generate quiz from document |
| POST | `/documentor/quiz/submit` | Submit quiz answers |
| GET | `/documentor/quiz/:id` | Get specific quiz |

### Explanation Routes
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/documentor/explain` | Get explanation for a topic |
| GET | `/documentor/explain/history` | Get explanation history |

---

## 🤔 Troubleshooting

### **Frontend won't load**
```bash
# Clear node_modules and reinstall
cd frontend
rm -rf node_modules package-lock.json
npm install
npm run dev
```

### **Backend connection errors**
```bash
# Check MongoDB connection string in .env
# Verify your IP is added to MongoDB Atlas network access
# Test connection: npm run dev
```

### **AI Service not responding**
```bash
# Verify GEMINI_API_KEY is set in AIserver/.env
# Check if API key is valid and not expired
# Restart the service: python main.py
```

### **Docker issues**
```bash
# Rebuild containers
docker-compose down
docker-compose up --build

# Check logs
docker-compose logs -f
```

### **Port already in use**
```bash
# Change ports in docker-compose.yml
# Or kill process using the port:
# Windows: netstat -ano | findstr :3000
# Mac/Linux: lsof -i :3000
```

---

## 📚 User Guide

### Getting Started

1. **Sign Up** - Create a new account with email and password
2. **Upload PDF** - Click "Upload Document" and select your PDF file
3. **Generate Summary** - Select a document and click "Summarize"
4. **Ask Questions** - Use the search bar to ask questions about your document
5. **Take Quiz** - Generate and take quizzes to test your knowledge
6. **Get Explanations** - Ask for explanations on any topic covered in your documents

---

## 🤝 Contributing

We welcome contributions! Here's how to help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines
- Follow existing code style
- Add comments for complex logic
- Test your changes before submitting
- Update documentation as needed

---

## 🐛 Reporting Issues

Found a bug? Please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)
- Your environment details

---

## 📞 Support

Need help? Try these resources:

- **Documentation**: Check the inline code comments
- **API Docs**: Available at http://localhost:8000/docs (when running)
- **Issues**: Check GitHub issues for similar problems
- **Discussions**: Start a discussion for general questions

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🎉 Acknowledgments

- **Google Gemini API** - For powerful AI capabilities
- **MongoDB** - For reliable data storage
- **FastAPI** - For fast and modern Python API
- **React & Vite** - For amazing frontend development
- **Express.js** - For robust backend framework

---

## 📈 Roadmap

- [ ] Dark mode support
- [ ] Advanced analytics dashboard
- [ ] Multi-language support
- [ ] Collaborative document sharing
- [ ] Export to PDF/Word
- [ ] Mobile app (React Native)
- [ ] Advanced search filters
- [ ] Team workspaces

---

## 👨‍💻 Authors

- **Your Name** - Project Lead & Full-Stack Developer

---

## 📧 Contact

For inquiries, suggestions, or feedback:
- Email: your-email@example.com
- LinkedIn: [Your Profile](https://linkedin.com)
- GitHub: [@your-username](https://github.com)

---

**Made with ❤️ by the DocuMentor Team**

---

### Quick Links
- [Getting Started](#-installation--setup)
- [API Documentation](#-api-endpoints)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
