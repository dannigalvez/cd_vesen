## Upload á Firebase Storage

* Firebase býður upp á þjónustuna Storage til að hýsa myndir, hljóðskrár, video og aðrar skrár.  Skránum er hægt að "uploada" og "downloada" til of frá geymslunni í gegnum Python Flask.
* Firebase Storage is a stand-alone solution for uploading user generated content like images and videos from an iOS and Android device, as well as the Web. In typical Firebase fashion, there's no server required. Firebase Storage is designed specifically for scale, security, and network resiliency.

### Kóðadæmi

* [Python Flask Upload to Storage](https://github.com/kanuarj/FirebasePython/blob/master/Storage/app.py)

### Myndbönd

* [Python + Firebase Cloud Storage - Upload/Download Files | Pyrebase](https://www.youtube.com/watch?v=I1eskLk0exg)

---

## Upload localt ( eða á pythonanywhere)

* Mjög einfalt að Upload-a skrá með Python Flask.
* Ef þú ætlar að uploada t.d. mynd inn á pythonanywhere svæðið þitt í t.d. möppuna static þarftu að stilla UPLOAD_FOLDER rétt.
    - app.config['UPLOAD_FOLDER'] = "/home/þittnotendanafn/mysite/static" ef þú ert með möppuna static inn 

### Kóðadæmi

* [Flask-File-Upload](https://github.com/arpanneupane19/Flask-File-Uploads/blob/main/main.py)

### Myndbönd

* [How to Upload Files with Flask Using Python (Með WTForms)](https://www.youtube.com/watch?v=GeiUTkSAJPs)

---

## Paginate. 

* Ef vefsíða er að birta mikið af gögnum ( tweet / blog / ... ) getur verið þreytandi að scrolla niður alla síðuna til að finna réttu gögnin.  *Paginate* er leið til að brjóta gögnin niður í minni einingar og birta færri færlsur á hverri síðu en dreifa svo gögnunum á fleiri síður.  Tilheyrandi flipar birtast til að birta mismunandi síður...

### Myndbönd

* [Python 3 Flask Bootstrap 4 Pagination Example to Paginate Array of Users Using flask-paginate](https://www.youtube.com/watch?v=vt0OXl2WCGI)

### Vefgreinar

* [Flask-paginate](https://flask-paginate.readthedocs.io/en/master/)
* [What is pagination](https://www.techtarget.com/whatis/definition/pagination)

---

## Deployment og hýsing á [pythonanywhere](https://www.pythonanywhere.com/). 

* PythonAnywhere is an online integrated development environment and web hosting service based on the Python programming language. Founded by Giles Thomas and Robert Smithson in 2012, it provides in-browser access to server-based Python and Bash command-line interfaces, along with a code editor with syntax highlighting (Wikipedia).

### Myndbönd

* [How to deploy a Python (Flask) web app on a (PythonAnywhere) live server](https://www.youtube.com/watch?v=75-oCKUx3oU)
