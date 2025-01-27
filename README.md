# Web-Scrapping Project 1

## Problem Statement

There is a website named as quotestoscrap.com you have to scrap the quotes, author, author_id, authorlink, tags which is in the website upto 10 pages and create a CSV file of it.
## Snapshot of website :-
![Image](https://github.com/user-attachments/assets/10005eeb-7ecc-410e-aa50-02e7be1d0191)

## Example :-
    In this example we scrapped the first 4 quotes with their author name,author_id, authorlink and tags.

![Image](https://github.com/user-attachments/assets/e52963a8-bbdd-4e2e-be9c-e282777ecc1b)

## Project code :-
python
    import requests 
    from bs4 import BeautifulSoup
    import pandas as pd
    from tqdm import tqdm 

    data=[]

    for page in tqdm(range(1,11)):
        link      = 'https://quotes.toscrape.com/page/'+str(page)
        response  = requests.get(link)
        soup      = BeautifulSoup(response.text, 'html.parser')

        for sp in soup.find_all('div',class_='quote'):
             quote     = sp.find('span',class_='text').text[1:-1]
            author    = sp.find('small').text
            author_id = sp.find('a').get('href')

            tags=[]

            for tag in sp.find_all('a',class_=('tag')):
                 tags.append(tag.text)
            tags      = ','.join(tags)
            data.append([quote, author, author_id, tags])
            
            print(quote,author,author_id,tags)
            print('-'*150)
    df = pd.DataFrame(data, columns = ['quote', 'author','author_id','tags'])
    df['author_link'] = 'https://quotes.toscrape.com'+df['author_id']
    df.to_csv('quotes.csv',index = False)

## Libraries used in this project :-

![Image](https://github.com/user-attachments/assets/8ec5108f-a0e3-4976-a253-f6ba8dc11761)

## Libraries Explanation :-

#### requests :- 
    requests is used to get the website or you can say fetch the website. 

#### BeautifulSoup :- 
    Beautiful Soup is a library that makes it easy to scrape information from web pages.

#### pandas :-
    pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.
#### tqdm :-
    Tqdm is a Python library that provides fast, extensible progress bars for loops and iterables.

## Project Code Explanation :-

    This code imports the requests library for HTTP requests,
    BeautifulSoup from bs4 for HTML parsing,
    pandas for data manipulation and analysis, and tqdm for creating progress bars in loops.
    Here's a line-by-line explanation of the code:

    1. data = []  
    Initializes an empty list data to store the scraped information.

    2. for page in tqdm(range(1,11)): 
    Loops through page numbers 1 to 10, with a progress bar provided by tqdm.

    3. link = 'https://quotes.toscrape.com/page/' + str(page)  
    Constructs the URL for each page of the website by appending the page number to the base URL.

    4. response = requests.get(link) 
    Sends an HTTP GET request to the constructed URL and stores the server's response in response.

    5. soup = BeautifulSoup(response.text, 'html.parser')  
    Parses the HTML content of the response using BeautifulSoup and stores the result in soup.

    6. for sp in soup.find_all('div', class_='quote'):  
    Iterates over all <div> elements with the class quote, which contain individual quote data.

    7. quote = sp.find('span', class_='text').text[1:-1]  
    Extracts the quote text from the <span> element with class text, stripping the outer quotes.

    8. author = sp.find('small').text  
    Extracts the author's name from the <small> element.

    9. author_id = sp.find('a').get('href')  
    Retrieves the hyperlink reference (author's profile link) from the <a> element.

    10. tags = []  
    Initializes an empty list tags to store tags related to the quote.

    11. for tag in sp.find_all('a', class_=('tag')):  
    Iterates over all <a> elements with the class tag to extract associated tags.

    12. tags.append(tag.text)  
    Appends the text of each tag to the tags list.

    13. tags = ','.join(tags)  
    Combines all tags into a single string, separated by commas.

    14. data.append([quote, author, author_id, tags])  
    Appends the extracted quote, author, author ID, and tags as a list to the data list.

    15. print(quote, author, author_id, tags)  
    Prints the scraped information for each quote.

    16. print('-' * 150)  
    Prints a separator line for better readability of the output.
    Here’s a line-by-line explanation of this code:

    17. df = pd.DataFrame(data, columns=['quote', 'author', 'author_id', 'tags'])  
    Converts the data list into a pandas DataFrame, assigning column names as 'quote', 'author', 'author_id', and 'tags'.

    18. df['author_link'] = 'https://quotes.toscrape.com' + df['author_id']  
    Creates a new column author_link in the DataFrame by concatenating the base URL 'https://quotes.toscrape.com' with the author_id values to form complete author profile links.

    19. df.to_csv('quotes.csv', index=False)  
    Exports the DataFrame to a CSV file named 'quotes.csv' without including the index column.
## Output :- 

### 1. CSV File (quotes.csv):  
   The scraped data will be saved in a file named quotes.csv. This file will contain the following columns:  
   - **quote**: The text of the quote (without enclosing quotation marks).  
   - **author**: The name of the author of the quote.  
   - **author_id**: The relative URL (path) of the author's profile page on the website.  
   - **tags**: Tags associated with the quote, separated by commas.  
   - **author_link**: The complete URL to the author's profile page by combining the base URL with author_id.

### 2. Sample Rows in the CSV:  
   Each row in the CSV represents a single quote. For example:

   | quote                                  | author        | author_id        | tags            | author_link                               |
   |----------------------------------------|---------------|------------------|-----------------|-------------------------------------------|
   | The world as we have created it...     | Albert Einstein | /author/Albert-Einstein | change,deep-thoughts,thinking,world | https://quotes.toscrape.com/author/Albert-Einstein |
   | It is our choices...                   | J.K. Rowling  | /author/J-K-Rowling | choices       | https://quotes.toscrape.com/author/J-K-Rowling |

### 3. Key Features of the Output:  
   - The CSV file organizes the scraped data for easy viewing and analysis.  
   - The author_link column provides a clickable link to the author's profile page.  
   - The tags column consolidates all tags into a single string for each quote.

This structure allows the scraped data to be used for further analysis, visualization, or storage.
