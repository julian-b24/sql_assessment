# SQL Assessment: Chats & Appointments

This proyect aims to show a set of metrics related to the operations in a business case.
The scope of this short proyect was expanded and you cand find more than raw SQL queries (despite that's the core of it).
Using streamlit and GCP any person is able to visualize the same metrics that we are trying to calculate in local enviroments.

## Deployment 🚀
The deployment of a simple visualization dashboard has been completed using Streamlit and it's cloud service. Here is the link: 
[Streamlit App](https://sqlassessment.streamlit.app/).

## Video 🎥
Also to ease the understanding of what has been made you can find a video of Julian Bolaños explaining the project, what was achieved, 
some points of improvement and the ideas to iterate and keep ading more features to this project. [Video](https://sqlassessment.streamlit.app/)

## Setup 🛠️
If you are interested in cloning this repository, here is a brief list of suggestions/item that you have to complete in order to run the
project sucessfully in a local envirmoment. First of all, virtual enviroment definition (In my case I prefer conda as my env manager):

```
conda create -n sql_assessment
conda activate sql_assessment
```

After this you will have to install pip and all the requierements that the project has:

```
conda install pip
pip install -r requierements.txt
```

Once the requierements are completed you will have to create the folder `.streamlit` in the root of the project and create your `secrets.toml`:

```
DB_SOURCE = "postgresql://your_user:secret_password@localhost:5432/your_db?sslmode=disable"
```

The previous secret variable is related to a postgres DB, independent of it you can use the relational DB that you prefer.

## Docker Local DB
Usin the terminal you can run the folllowing command to create a postgres:alpine-16 container that allows you to
test in a local enviroment:

```
docker run -d \                                                                              
    --name your_db \
    -p 5432:5432 \
    -e POSTGRES_DB=your_db_name \
    -e POSTGRES_USER=your_user \
    -e POSTGRES_PASSWORD=secret_password \
    postgres:16-alpine \
```

## Next Steps
Once the local DB the nest step are:

1. Create the schemas using [schema.sql](https://github.com/julian-b24/sql_assessment/blob/main/schema.sql)
2. Insert the data using the [inserts.sql](https://github.com/julian-b24/sql_assessment/blob/main/inserts.sql)
3. Do any query you would like to! Or execute the ones we have in [querys.sql](https://github.com/julian-b24/sql_assessment/blob/main/querys.sql)