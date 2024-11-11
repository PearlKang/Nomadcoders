from fastapi import FastAPI


app = FastAPI(
    title="Nicolacus Maximus Quote Giver",
    description="Get a real quote said by Nicolacus Maximus himself.",
)


@app.get("/quote")
def get_quote():
    return {
        "quote": "Life is short so eat it all.",
    }
