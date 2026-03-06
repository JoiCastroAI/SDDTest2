from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.domain.exceptions import DomainError
from src.infrastructure.config import settings
from src.presentation.middleware import domain_exception_handler
from src.presentation.routers.companies import router as companies_router


def create_app() -> FastAPI:
    app = FastAPI(title="Companies API", version="0.1.0")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[settings.FRONTEND_URL],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_exception_handler(DomainError, domain_exception_handler)  # type: ignore[arg-type]

    app.include_router(companies_router)

    return app


app = create_app()
