# The pandas library is the gold standard open-source Python tool used for data manipulation, analysis, and cleaning. It essentially gives Python the capability to work with spreadsheet-like tables,
# allowing you to load, alter, and analyze structured data using only a few lines of code.
import pandas as pd

def get_imdb_top_250(min_votes: int = 25000, output_csv: str = "temp/imdb_top_250_ranked.csv") -> pd.DataFrame:
    """
    Downloads IMDb title and rating datasets, calculates the Bayesian
    weighted rating, and returns the top 250 movies.
    """
    ratings_url = "https://datasets.imdbws.com/title.ratings.tsv.gz"
    basics_url = "https://datasets.imdbws.com/title.basics.tsv.gz"

    print("Loading ratings data...")
    ratings = pd.read_csv(ratings_url, sep="\t", compression="gzip")

    print("Loading titles data...")
    basics = pd.read_csv(
        basics_url,
        sep="\t",
        compression="gzip",
        usecols=["tconst", "titleType", "primaryTitle", "startYear"],
        dtype=str,
    )

    print("Merging and filtering dataset...")
    # Merge titles and ratings for feature-length movies only
    movies = basics[basics["titleType"] == "movie"].merge(ratings, on="tconst")

    # Enforce numeric types for rating calculations
    movies["numVotes"] = pd.to_numeric(movies["numVotes"], errors="coerce")
    movies["averageRating"] = pd.to_numeric(movies["averageRating"], errors="coerce")

    # Filter by minimum vote threshold
    qualified = movies[movies["numVotes"] >= min_votes].copy()

    # Calculate Bayesian Weighted Rating: (v / (v + m)) * R + (m / (v + m)) * C
    C = qualified["averageRating"].mean()
    v = qualified["numVotes"]
    R = qualified["averageRating"]

    qualified["weighted_rating"] = (v / (v + min_votes)) * R + (min_votes / (v + min_votes)) * C

    # Sort descending by weighted rating and slice top 250
    top_250 = qualified.sort_values(by="weighted_rating", ascending=False).head(250)

    # Save to CSV
    export_columns = ["primaryTitle", "startYear", "averageRating", "numVotes", "weighted_rating"]
    top_250[export_columns].to_csv(output_csv, index=False)
    print(f"Exported top 250 list to {output_csv}\n")

    return top_250

def main():
    top_250_movies = get_imdb_top_250()

    for rank, (_, row) in enumerate(top_250_movies.iterrows(), start=1):
        print(
            f"{rank:3d}. {row['primaryTitle']} ({row['startYear']}) "
            f"- Weighted: {row['weighted_rating']:.2f} | "
            f"Raw: {row['averageRating']} ({int(row['numVotes']):,} votes)"
        )


if __name__ == "__main__":
    main()
