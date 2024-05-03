from fastapi import FastAPI, Depends, Header, Request

app = FastAPI()

@app.get('/')
#async def index(real_ip: str = Header(None, alias='X-Real-IP')):
#async def get_client_ip(request: Request):
#    client_host = request.client.host
#    #print("Client IP:", client_host)
#    results = {"client_host": client_host }
#    return results
async def get_client_ip(request: Request):
    # Get the client IP address from the X-Forwarded-For header
    client_ip = request.headers.get("X-Forwarded-For")
    
    # If X-Forwarded-For header is not present, fall back to request.client.host
    if not client_ip:
        client_ip = request.client.host
        
    result = {"Client_IP": client_ip}
    return result
