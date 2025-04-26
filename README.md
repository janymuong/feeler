### **`Feelr` - a Sentiment Analysis Platform Using NLP**  
> The Machine Learning model was trained on the [Sentiment 140](https://www.tensorflow.org/datasets/catalog/sentiment140) dataset.


### Premise
This is what `feelr` does - it is a web application that packages machine learning(narural language processing) models to analyze text sentiment. It allows users to input text, view sentiment predictions, track their history, and visualize sentiment trends over time. The app features a secure backend with user authentication and a responsive, user-friendly frontend.

#### Feeler Landing Page:
You can find more information about `Feeler` on this [webpage](https://ohangadon.github.io/FEELER-WEB/)


### **Features**
- **Sentiment Analysis**: analyze text and receive sentiment predictions with confidence scores.
- **History Tracking**: save and view past sentiment analyses in a Twitter-like interface.
- **Customer Sentiment Visuals**: sentiment trends using interactive graphs and word clouds.
- **User Authentication**: secure registration, login, and logout using JWT.
- **Responsive Design**: works seamlessly on both desktop only for now.


### **Tech Stack**
- **Frontend**: React.js, Chart.js
- **Backend**: Django, Django REST Framework
- **Machine Learning**: TensorFlow for sentiment prediction + Twitter-roBERTa Transformer model
- **Database**: PostgreSQL

---

### **Setup Instructions:**
```bash
git clone git@github.com:janymuong/feeler.git
```


#### 1. Backend Set-Up

It's recommended to leverage a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [Python Docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).


- Create a siloed virtual environment with **Python 3.12** and **activate** it. You should have **Python 3.12** available in your host/local machine. 
Check the Python path using: 
```bash
$ which python3
```
```bash
$ python3 -m pip install --user virtualenv 
# use a command similar to this one to create environment(working dir: feeler(backend)):
$ python3 -m virtualenv --python=<path-to-python3.12> ../.feelr_env/
$ source ../.feelr_env/bin/activate
```
> Alternatively, you could setup the virtual environment via `make setup` in this [`Makefile`](./Makefile).

- Run `make install` to install **Django**, **TensorFlow** and other dependencies for it. This will install all relevant pip packages for the project.



##### **Stand Up Backend**
1. Install dependencies:
   ```bash
   cd feeler
   pip install -r requirements.txt
   ```
2. Configure `.env` with the following variables:
   ```
   DJANGO_SECRET_KEY=your_secret_key
   DB_NAME=feeler # database
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
   cd FE-feeler
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
3. View past analyses in the **Emotion History** section.
4. Explore mood trends/visualization in the **Emotion Graphs** section.
5. Log out.


---
### **Feeler Developers**

<div style="border: 2px solid #000; padding: 10px; width: fit-content; border-radius: 5px;">

- [Jany Muong ](https://github.com/janymuong)  
- [Joram Kireki ](https://github.com/Joram-kireki)  
- [Vincent Ochieng ](https://github.com/OhangaDon)
- [Gatmach Yuol Nyuon](https://github.com/Gatmach) 
- [Josphat Waweru Thumi](https://github.com/J-Thumi)
- [Akech Atem](https://github.com/akechsmith)

</div>