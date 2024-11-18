from fastapi import FastAPI, Request
from pydantic import BaseModel, Field
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Nicolacus Maximus Quote Giver",
    description="Get a real quote said by Nicolacus Maximus himself.",
    servers=[
        {
            "url": "https://definitely-character-postage-fee.trycloudflare.com",
        },
    ],
)


class Quote(BaseModel):
    quote: str = Field(
        description="The quote that Nicolacus Maximus said.",
    )
    year: int = Field(
        description="The year when Nicolacus Maximus said the quote.",
    )


@app.get(
    "/quote",
    summary="Returns a random quote by Nicolacus Maximus",
    description="Upon receiving a GET request this endpoint will return a real quote said by Nicolacus Maximus himself.",
    response_description="A Quote object that contains the quote said by Nicolacus Maximus and the date when the quote was said.",
    response_model=Quote,
    openapi_extra={
        "x-openai-isConsequential": False,
    },
)
def get_quote(request: Request):
    print(request.headers)
    return {
        "quote": "Life is short so eat it all.",
        "year": 1950,
    }


@app.get(
    "/authorize",
    response_class=HTMLResponse,
)
def handle_authorize(client_id: str, redirect_uri: str, state: str):
    print(
        client_id,
        redirect_uri,
        state,
    )
    return {
        "ok": True,
    }
