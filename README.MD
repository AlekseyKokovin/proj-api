**Base URL:** `https://proj-api-a99p.onrender.com/`

This REST API allows you to retrieve and add cryptocurrency news articles from the CryptoNews dataset used in this project.

### Available Endpoints

#### 1. GET `/data` – Retrieve News Data
Returns a list of news articles with support for pagination and filtering.

**Parameters:**
`limit`      integer   Number of records to return (default: 10)        `limit=20`

`offset`     integer   Number of records to skip                        `offset=50`             

`subject`    list      Filter by one or more subjects (optional)        `subject=altcoin&subject=bitcoin` 

#### 2. POST `/data` – Add New News Record
Adds a new news article to the dataset.

**Required Fields to Fill:**

| Field        | Type   | Description                                           | Example                                                       |
|--------------|--------|-------------------------------------------------------|---------------------------------------------------------------|
| `date`       | string | Date of the news article (YYYY-MM-DD HH:MM:SS format) | `2067-67-67 06:09:07`                                         |
| `sentiment`  | string | Sentiment in dictionary format                        | `{'class': 'positive', 'polarity': 0.5, 'subjectivity': 0.3}` |
| `source`     | string | News source                                           | `CryptoNews`                                                  |
| `subject`    | string | Topic of the news                                     | `altcoin`                                                     |
| `text`       | string | Full text of the news article                         | `Bitcoin price increased after...`                            |
| `title`      | string | Title of the news article                             | `Bitcoin Surges Past $70,000`                                 |
| `url`        | string | Link to the original article                          | `https://example.com/news/123`                                |

---

You can test the API here:  
**https://proj-api-a99p.onrender.com/docs**