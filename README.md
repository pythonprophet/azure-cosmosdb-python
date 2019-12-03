# Azure-CosmoDB-Python
A python program which connects to Azure Cosmos DB SQL API and performs read, create feature.

## Prerequisites
- Download the Azure Cosmos DB Emulator. The emulator is currently only supported on Windows. The sample shows how to use the sample with a production key from Azure, which can be done on any platform.

- If you don’t already have Visual Studio Code installed, you can quickly install VS Code for your platform (Windows, Mac, Linux).

## Install the dependencies
Pinning down dependencies
```
pip freeze > requirements.txt
```
Run the following command to install the python modules.

pip install -r .\requirements.txt
Database Config
```
CONFIG = {
    "ENDPOINT": "https://localhost:8081",
    "PRIMARYKEY": "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw==",
    "DATABASE": "CosmosDatabase",  # Prolly looks more like a name to you
    "CONTAINER": "CosmosContainer"  # Prolly looks more like a name to you
}
```
- Change DATABASE to your db name
- Change container name to your container

Youtube Tutorial: 
 
