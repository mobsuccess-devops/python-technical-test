# Test statement

## Part 0

Install poetry using pip:
  
```bash
pip install poetry
```

Set virtual environment location to local folder:

```bash
poetry config virtualenvs.in-project true
```

Install dependencies:

```bash
poetry install
```

Run the server:

```bash
poetry run python main.py
```

> **Note**
> 

## Part 1

- Create a first endpoint to get horse results with as option the horseback category as optional filter. Use GET method.
If the horse is not found with ffe_service return a 404 error.

## Part 2

- Implement the algorithm on `models.horseback.points()`. For each horseback the number of points earned is :
  - first quarter* : 8 points
  - second quarter* : 4 points
  - third quarter* : 2 points
  - last quarter* : 0 point

  Use `ceil` to determine the quarter size.

## Part 3

- Create a second endpoint that accept a list of Horse Id (data source: FFE). Use POST method to give the list as payload.
  
  The endpoint return the horse classment for each category / discipline. Only the best 3 horses must be returned, with name and total points for this category/discipline. The pandas library must be used for this implementation.

## Notes

Results of the two endpoint must be filtered on the current year.

To get the horse data, you can use the ffe_service.
:warning: Please note, ffe_service can be slow as it perform IO operations.

You can test your API, for the following horses :

- TURNeE1EUTVNak4vdTdjS3dNQ3RlUT09
- TVRRMU5ETXlOemtGalNWSzZxTHU5UT09
- TmpBd016UXlOamN4bEIrc2R4RFlWZz09
- TURFek5EYzJOemtrV2xYU3FGaFpXUT09
