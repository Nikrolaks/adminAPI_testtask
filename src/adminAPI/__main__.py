import uvicorn

uvicorn.run(
    'adminAPI.app:app',
    reload=True
)