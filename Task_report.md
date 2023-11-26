# Тестовое задание на должность стажера DevOps
## Создаем приложение, собираем образ и загружаем на DockerHub
Создаем веб-приложение "Hello world!" на фреймворке Django .Создаем Dockerfile .
```
FROM python:3.9-slim
WORKDIR /app
RUN pip install gunicorn
COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:32777", "web_project.wsgi"]
```


![Создание образа](pictures/Создание образа.png)

Авторизуемся в DockerHub

![авторизация](https://github.com/PetryakovPavel/Test_Task_for_Biocad/blob/main/pictures/Вход%20в%20ДХ.png)

 Собраный образ  загружаем на DockerHub


![загрузка](https://github.com/PetryakovPavel/Test_Task_for_Biocad/blob/main/pictures/Загрузка%20в%20ДХ.png)

## Запуск Minikube, создание demployment с двумя репликами
Запускаем minikube
```
minikube start 
```
![миникуб](https://github.com/PetryakovPavel/Test_Task_for_Biocad/blob/main/pictures/МиникубСтарт.png)

Пишим манифест для deployment 

![deploy](https://github.com/PetryakovPavel/Test_Task_for_Biocad/blob/main/pictures/Деплой.png)

Создаем deployment на основе манифеста.


Проверяем наличие деплоймента и двух реплик контейнера.

![depl](https://github.com/PetryakovPavel/Test_Task_for_Biocad/blob/main/pictures/Деплой%20командой.png)


## Создание сервиса для доступа
Расширяем deploy  с помощью сервиса NodePort.После выполнения команды  проверяем наличие сервиса. Вывод в формате Yaml сохраняем в файл service.yml.

![service](https://github.com/PetryakovPavel/Test_Task_for_Biocad/blob/main/pictures/сервис.png)

Манифеста сервиса:

```
apiVersion: v1
kind: Service
metadata:
  creationTimestamp: "2023-11-23T15:20:24Z"
  labels:
    app: hello-world
  name: hello-world-service
  namespace: default
  resourceVersion: "11232"
  uid: 352568b5-fd96-4285-a2d6-1a474f3eeb19
spec:
  clusterIP: 10.97.88.75
  clusterIPs:
  - 10.97.88.75
  externalTrafficPolicy: Cluster
  internalTrafficPolicy: Cluster
  ipFamilies:
  - IPv4
  ipFamilyPolicy: SingleStack
  ports:
  - nodePort: 31229
    port: 32777
    protocol: TCP
    targetPort: 32777
  selector:
    app: hello-world
  sessionAffinity: None
  type: NodePort
status:
  loadBalancer: {}

```
## Запуск проброса портов и проверка результата

```
kubectl port-forward service/hello-world-service 32777
```

![HelloWorld](https://github.com/PetryakovPavel/Test_Task_for_Biocad/blob/main/pictures/Хеллоу%20ворлд.png)
