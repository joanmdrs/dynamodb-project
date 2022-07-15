import uvicorn

if __name__ == '__main__':
    uvicorn.run(app="index:app",host="127.0.0.1",port=8002, reload=True)