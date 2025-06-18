# eloshapes-data

Analyzing data on gaming mice


## Instructions

1. Install the required packages by running (TODO: create a requirements.txt file):
```bash
pip install requirements.txt
```

2. To obtain your API key, visit the EloShapes [database](https://www.eloshapes.com/mouse/database) page and open the Network tab of the Developer Tools. You may need to refresh the page.
Look for a request with a name that starts with `products_available_v2` and copy the `Apikey` value from the request headers. Go to `.env.example` and replace the `API_KEY` value with your key. Then, rename the file to `.env`.


3. To obtain the raw data, run the following:
```bash
python -m src.scraping.scraper
```

4. TODO

Make sure to run any code in the `src` directory from the root of the repository.


## References

- Data from the [EloShapes](https://www.eloshapes.com/) website


## Remarks

From what I can tell, the API key is static and does not change if I switch Google accounts or go to incognito mode. It may be the same for everyone, but out of caution I am not sharing it here
in case it is not. There is a good chance this repository will break in the future if the API changes or the website is updated, so I will not be maintaining it.