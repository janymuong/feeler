### **MoodLens - Sentiment Analysis**  
> The Machine Learning model was trained on the [Sentiment 140](https://www.tensorflow.org/datasets/catalog/sentiment140) dataset.

MoodLens is a web application that packages a machine learning model to analyze text sentiment. It allows users to input text, view sentiment predictions, track their history, and visualize mood trends over time. The app features a secure backend with user authentication and a responsive, user-friendly frontend.


### **Features**
- **User Authentication**: secure registration, login, and logout using JWT.
- **Sentiment Analysis**: analyze text and receive sentiment predictions with confidence scores.
- **History Tracking**: save and view past sentiment analyses in a Twitter-like interface.
- **Mood Visualization**: view mood trends using interactive graphs.
- **Responsive Design**: works seamlessly on both desktop only for now.


### **Tech Stack**
- **Frontend**: React.js, Chart.js
- **Backend**: Django, Django REST Framework
- **Machine Learning**: TensorFlow for sentiment prediction
- **Database**: PostgreSQL

---

### **Setup Instructions:**
```bash
git clone https://github.com/Jeff-kimani/moodlens.git
```
#### **1. Backend**
1. Install dependencies:
   ```bash
   cd moodlens
   pip install -r requirements.txt
   ```
2. Configure `.env` with the following variables:
   ```
   DJANGO_SECRET_KEY=your_secret_key
   DB_NAME=moodlens
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_PORT=5432
   ```
3. Run migrations and start the server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

#### **2. Frontend**
1. Navigate to the frontend directory:
   ```bash
   # do in root directory;
   cd moodlens-frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```



### **Testing**
- **Frontend**:
  ```bash
  npm test
  ```
- **Backend**:
  ```bash
  python manage.py test
  ```


### **Usage**
1. Register or log in to the app.
2. Navigate to the **Model** page to analyze text sentiment.
3. View past analyses in the **Mood History** section.
4. Explore mood trends/visualization in the **Mood Graphs** section.
5. Log out.

---

### **Contributors**
- [Jany Muong ](https://github.com/janymuong) 
- Jeff Chege  
