from typing import Union
from app.nmap.main import start_nmap_scan #Deprecated
# from app.nmap.nmap3.main import *
from fastapi import FastAPI

app = FastAPI()


@app.get("/api")
def read_root():
    return {"Hello": "World"}


@app.get("/api/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/nmap/")
async def scan_network(target_ip: str, ports: str):
    # Need to implement else if statments in case flags or ports are not provided
    print("Here")
    #Deprecated
    result = start_nmap_scan(target_ip = target_ip, ports=ports)
    
    # Example response (you should customize this based on your needs)
    return {"message": f"Scan initiated {result}", "targetIP": target_ip, "ports": ports}


# start_nmap_scan(target_ip ='127.0.0.1', ports='1-1000')