import wikipedia
from os import system

def main():
    system('clear')
    print("Welcome to wikisearch!\n")
    works = ["1) 5 Random Wikipedia articles", "2) Search for something on wikipedia", "3) Exit"]
    
    for item in works:
        print(item)
    
    work = input("\nSelect an option (please use serial number): ")
    if work == "1":
        randomer()
    elif work == "2":
        searcher()
    elif work == "1" or work == "exit":
        exit()

def randomer():
    system('clear')
    lis = wikipedia.random(5)
    for item in lis:
        item_page = wikipedia.page(item)
        page_url = item_page.url
        print(f"{item}: {page_url}\n")
    
    input("Hit enter to exit to main menu")
    main()

def searcher():
    system('clear')
    query = input("What do you want to search?\nPlease be specific to ensure no errors\n>")

    obj = wikipedia.page(query)
    title = obj.title
    summary = wikipedia.summary(query, 5)
    link = obj.url
    
    system('clear')
    print(f"{query}\n\n{title}\n\n{summary}\n\nUrl: {link}")

    input("\nHit enter to exit to main menu")
    main()

main()
