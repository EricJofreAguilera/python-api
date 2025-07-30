from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from app.routes import user

app = FastAPI()
app.include_router(user.router)

# Manejador de errores personalizado
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errores = []

    for error in exc.errors():
        loc = error.get("loc", [])
        campo = loc[-1] if loc else "dato"
        errores.append(f"Error en '{campo}' validar formato.")

    return JSONResponse(
        status_code=422,
        content=jsonable_encoder({"mensaje": errores}),
    )

