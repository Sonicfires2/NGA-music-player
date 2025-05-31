from downloader import download_audio
from player import play_song
import os
import sys
from prompt_toolkit.shortcuts import radiolist_dialog

def view_songs():
    while True:
        songs = [f for f in os.listdir("downloads") if f.endswith(".mp3")]
        if not songs:
            print("⚠️ No songs available. Download some first.")
            return

        # Display interactive song list
        song = radiolist_dialog(
            title="Your Songs",
            text="Select a song (use arrows):",
            values=[(s, s) for s in songs]
        ).run()
        if song is None:
            return

        # Song action menu
        while True:
            print(f"\nSelected: {song}")
            print("1. ▶️ Play")
            print("2. 🔙 Back to Song List")
            print("3. ❌ Exit")
            print("4. 🗑️ Delete Song")
            choice = input("Choose an option: ")
            if choice == "1":
                print(f"▶️ Playing {song}...")
                play_song(os.path.join("downloads", song))
            elif choice == "2":
                break  # back to song list
            elif choice == "3":
                sys.exit(0)
            elif choice == "4":
                confirm = input(f"Are you sure you want to delete '{song}'? (y/n): ").lower()
                if confirm == "y":
                    try:
                        os.remove(os.path.join("downloads", song))
                        print(f"🗑️ Deleted '{song}' successfully.")
                        break  # go back to song list since it's now gone
                    except Exception as e:
                        print(f"❌ Error deleting song: {e}")
                else:
                    print("Deletion cancelled.")
            else:
                print("Invalid option, please choose 1, 2, 3, or 4.")

def main():
    os.makedirs("downloads", exist_ok=True)
    while True:
        print("\n=== Main Menu ===")
        print("1. View All Songs")
        print("2. Download Song")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            view_songs()
        elif choice == "2":
            query = input("Search song: ")
            download_audio(query)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()