from azure.cosmos import cosmos_client
import urllib3
import json
CONFIG = {
    "ENDPOINT": "https://localhost:8081",
    "PRIMARYKEY": "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw==",
    "DATABASE": "CosmosDatabase",  # Prolly looks more like a name to you
    "CONTAINER": "CosmosContainer"  # Prolly looks more like a name to you
}
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

CONTAINER_LINK = f"dbs/{CONFIG['DATABASE']}/colls/{CONFIG['CONTAINER']}"
document_link = f"dbs/{CONFIG['DATABASE']}/colls/{CONFIG['CONTAINER']}/docs/1"

FEEDOPTIONS = {}
FEEDOPTIONS["enableCrossPartitionQuery"] = True
# There is also a partitionKey Feed Option, but I was unable to figure out how to us it.

options = {}

options['enableCrossPartitionQuery'] = True
options['maxItemCount'] = 5

QUERY = {
    "query": f"SELECT * from c"
}

# Initialize the Cosmos client
client = cosmos_client.CosmosClient(
    url_connection=CONFIG["ENDPOINT"], auth={"masterKey": CONFIG["PRIMARYKEY"]}
)

results = client.QueryItems(CONTAINER_LINK, QUERY, FEEDOPTIONS)

for result in results:
    print(json.dumps(result, indent=True))


my_dict = dict()
key = input("Enter the key: ")
value = input("Enter the value: ")
my_dict[key] = value
print(my_dict)
client.CreateItem(CONTAINER_LINK, my_dict)

print("After adding new document\n")
for result in results:
    print(json.dumps(result, indent=True))

