import api


# Run Application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(api.app, host="localhost", port=5432)
# In command line
# uvicorn main:app --host 0.0.0.0 --port 5432