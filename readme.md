# Galaxy Search
---

* Search Engine for Astronomy picture using ElasticSearch Database
* FastAPI for backend and Streamlit for frontent
* Based on [Nasa's APOD website](https://apod.nasa.gov/apod/archivepix.html)  


### Setup

```
pip install requirements.txt
```

#### Runing elasticsearch container
```
$ sudo docker-compose up -d
```

elastic url: http://localhost:9201/

#### Inserting Documents
./backend
```
$ python index_data.py
```

#### Staring backend server
./backend
```
$ uvicorn main:app
```

### Starting frontend
./frontend
```
$ streamlit run app.py
```

### Demo

galaxy_search_sr.webm