import requests
import csv
import os


def scrape_songs(start_page=1, end_page=15, genre="",output_filename="scraped_songs.csv"):
    """
    Scrape songs from LyricsDB within a given page range and save them to a CSV file.

    Args:
        start_page (int): First page to scrape.
        end_page (int): Last page to scrape.
        genre (str): Optional genre to filter songs by.
    """

    # ------------------------------
    # User credentials
    # ------------------------------
    username = 'ivan.borg.i84578@mcast.edu.mt'
    password = '0210JjtzUvKc'
    base_url = 'http://23.94.19.185'

    # ------------------------------
    # Start session
    # ------------------------------
    session = requests.Session()
    session.auth = (username, password)

    # ------------------------------
    # Verify login
    # ------------------------------
    home_resp = session.get(base_url)
    if "LyricsDB" not in home_resp.text:
        print("Login failed — LyricsDB not found.")
        return

    print("Logged in successfully — LyricsDB detected!")

    # ------------------------------
    # Scrape pages
    # ------------------------------
    all_songs_url = f'{base_url}/all_songs.php'
    all_songs = []

    for page in range(start_page, end_page + 1):
        payload = {"page": page}
        resp = session.post(all_songs_url, json=payload)
        resp.raise_for_status()

        data = resp.json()
        songs = data.get('songs', [])
        total = data.get('total', 0)

        if not songs:
            print(f"No songs found on page {page}. Stopping...")
            break

        all_songs.extend(songs)
        print(f"Scraping page {page}: {len(all_songs)} songs collected.")

        if total and len(all_songs) >= total:
            print("All songs scraped successfully.")
            break

    # ------------------------------
    # Filter by genre if provided
    # ------------------------------
    if genre:
        all_songs = [s for s in all_songs if genre.lower() in s.get('genre', '').lower()]
        print(f"{len(all_songs)} songs remaining after filtering by genre '{genre}'")

    # ------------------------------
    # Save to CSV inside /Songs
    # ------------------------------
    # Use /songs for Docker mount or C:\LyricsTextMining\Songs locally
    output_dir = "/songs"
    csv_filename = os.path.join(output_dir, output_filename)

    os.makedirs(output_dir, exist_ok=True)
    existing_songs = set()

    # Write CSV
    if all_songs:
        headers = all_songs[ 0 ].keys()
        with open(csv_filename, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(all_songs)
        print(f"Saved {len(all_songs)} songs to {csv_filename}")
    else:
        print("No songs found to save")


# ------------------------------
# Function Call
# ------------------------------
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--start_page", type=int, default=1)
    parser.add_argument("--end_page", type=int, default=5)
    parser.add_argument("--genre", type=str, default="")
    parser.add_argument("--output", type=str, default="scraped_songs.csv")

    args = parser.parse_args()
    scrape_songs(args.start_page, args.end_page, args.genre, args.output)
