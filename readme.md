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

<video width="720" height="480" controls>
  <source src="galaxy_search_sr.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

<!-- ![Demo](https://raw.githubusercontent.com/hiiimanshusharma/Galaxy-Search//main/galaxy_search_sr.mp4) -->