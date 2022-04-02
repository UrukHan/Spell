docker build -t spell .
docker run --rm --name ruspell -p 8000:8000 spell
docker run -d --name ruspell -p 8000:8000 spell

docker run --rm --gpus 'device=0' --name ruspell -p 8000:8000 spell
docker run -it -d --gpus 'device=0' --name ruspell -p 8000:8000 spell

/health_check
curl -X GET http://10.9.1.156:8000/api/health_check
curl -X POST -H "Content-Type: application/json" -d "{ \"text\": \"Введите текст\" }" http://192.168.1.25:8000/api/predict
curl -X POST -H "Content-Type: application/json" -d "{ \"text\": \"Введите текст\" }" localhost:8000/api/predict

curl -X POST -H "Content-Type: application/json" -d "{ \"text\": \"ывсем привет выныканалетоп армии и это двадцать пятый день спец операций на украине ет самый главной новости российские военные ракетами кинжалы калибр уничтожили крупную военную топливную базу украины ракетным ударом по населенному пункту под жетамиром уничтжены более стаукраинских военных\" }"  http://172.28.144.1:8000/api/predict


docker exec -it <container_id> bash
tensorflow==2.8.0

//RUN apt-get install nvidia-container-runtime

curl -X POST -H "Content-Type: application/json" -d "{ \"text\": \"Украина по сути согласилась на принципиальные требования России, заявил глава российской делегации, помощник президента Владимир Мединский в эфире телеканала\" }" http://172.20.192.1:8000/api/predict


docker kill $(docker ps -a -q) 
docker rm $(docker ps -a -q)  
docker rmi $(docker images -a -q)

sudo chmod 666 /var/run/docker.sock

docker login http://docker-ici-cyrm.fdi.group:443
ici
cyrmE3r1x5a1J

docker tag news docker-ici-cyrm.fdi.group:443/class_news:310322
docker push docker-ici-cyrm.fdi.group:443/class_news:310322

docker tag t5 uruk/summarizet5:t5

