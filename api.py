from typing import Optional, List
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class NewsData(BaseModel):
    date: str
    sentiment: str
    source: str
    subject: str
    text: str
    title: str
    url: str


@app.get('/data')
def get_data(limit: int = 10, subject: Optional[List[str]] = None):
    df = pd.read_csv('cryptonews.csv')
    if subject:
        df = df[df['subject'].str.lower().isin([s.lower() for s in subject])]
    else:
        default_subjects = ['altcoin', 'bitcoin', 'ethereum']
        df = df[df['subject'].str.lower().isin(default_subjects)]
    return df.head(limit).to_dict(orient='records')


@app.post('/data')
def add_data(item: NewsData):
    try:
        new_row = item.model_dump()
        new_df = pd.DataFrame([new_row])

        existing_cols = pd.read_csv('cryptonews.csv', nrows=0).columns.tolist()
        for col in existing_cols:
            if col not in new_df.columns:
                new_df[col] = None
        new_df = new_df[existing_cols]
        new_df.to_csv('cryptonews.csv', mode='a', index=False, header=False)
        return {"status": "success", }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to add data: {str(e)}")
