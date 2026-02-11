WellBot – Global Wellness Assistant Chatbot
WellBot – AI Powered Global Wellness Assistant
An intelligent AI-driven healthcare assistant that analyzes medical reports, detects potential health conditions, generates personalized recovery plans, and provides smart reminders to guide users through their complete wellness lifecycle.
 1. Project Statement & Outcomes
Project: AI-Based Personalized Health Recovery System

WellBot is designed to bridge the gap between medical data and daily health action. Users can upload medical reports or describe symptoms, and the system uses OCR + AI models to detect conditions, assess risk levels, and generate personalized recovery plans including diet, exercise, lifestyle tips, and do’s & don’ts. The platform also tracks daily progress and sends smart reminders (including WhatsApp notifications).

 Outcomes

Secure authentication with login/signup & Google OAuth

OCR-based medical report text extraction

AI-powered disease detection & risk assessment

Personalized recovery lifecycle plan

Interactive dashboard with visual progress tracking

Smart reminder automation (including WhatsApp alerts)

Report history & analytics tracking

 2. Core Modules Implemented
1️ Authentication Module
Email/password login
Google authentication
JWT-based session management

2️ Medical Report Processing Module
Upload medical reports (PDF/Image)
OCR text extraction
Text cleaning & keyword extraction
Disease detection using AI

3️ AI Analysis Engine
Risk assessment
Recovery plan generation
Diet plan
Exercise plan
Lifestyle tips

4️ Dashboard & Tracking
Health score visualization
Water intake tracking
Sleep tracking
Steps tracking
Progress percentage updates
Graph updates in real-time

5️.Chat with AI Assistant
Symptom input
Intelligent response generation
Personalized advice
Conversation history storage

 3. System Workflow (High-Level Flow)
User Flow
Open WellBot
Login / Signup / Google Auth
Access Dashboard
Choose input method
Upload medical report
Enter symptoms manually
AI Analysis Engine
Disease Identification
Generate Recovery Plan
Store in Database
Push updates to Dashboard
Ongoing tracking & reminders

 4. AI Processing Pipeline

Input (Report / Symptoms)
OCR Extraction

Text Cleaning
Keyword Extraction
Disease Detection
Risk Assessment
Plan Generation Engine
Store in Database
Update Dashboard

 5. Weekly Development Plan
Weeks 1–2:Frontend and  Backend & Database Setup
Flask API setup
PostgreSQL/MySQL integration
JWT authentication
Basic API routes

 Key Features
AI-powered medical insights
Complete recovery lifecycle system
Interactive dashboards
Smart automation reminders
Secure authentication
Modern responsive UI
Scalable architecture

Tech Stack
 Frontend
React.js
React Router
Axios
Framer Motion (animations)

Recharts (data visualization)
 Backend
Python
Flask
Flask-JWT-Extended
SQLAlchemy

Database
PostgreSQL / MySQL
 AI & Processing
OCR (Tesseract)
LLM Integration
Text preprocessing

