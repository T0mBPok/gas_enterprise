from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
from src.exceptions import TokenExpiredException, TokenNoFoundException
from src.deposit.router import router as deposit_router
from src.classifiers.router import router as classifier_router
from src.delivery.router import router as delivey_router
from src.customer.router import router as customer_router
from src.enterprise.router import router as enterprise_router
from src.well.router import router as well_router
from src.order.router import router as order_router
from src.prodMetrics.router import router as metrics_router
from src.productionProcess.router import router as process_router

app = FastAPI(title='Gas_enterprise')
PORT = 9000
HOST = "0.0.0.0"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173", "http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(classifier_router)
app.include_router(deposit_router)
app.include_router(customer_router)
app.include_router(delivey_router)
app.include_router(enterprise_router)
app.include_router(well_router)
app.include_router(order_router)
app.include_router(metrics_router)
app.include_router(process_router)


@app.exception_handler(TokenExpiredException)
async def token_expired_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )


@app.exception_handler(TokenNoFoundException)
async def token_no_found_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

if __name__ == "__main__":
    uvicorn.run('src.main:app', host = HOST, port=PORT, reload = True)