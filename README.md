🌐 Website Text Extractor 📝

This Python project is a simple website text extractor that allows you to save the main content of a website as a text file. It uses libraries like tkinter for the GUI, filedialog for file operations, time for delays, selenium for web scraping, BeautifulSoup for HTML parsing, requests for making HTTP requests, os for environment settings, and spacy for natural language processing (NLP).

Prerequisites 🛠️

Before running this project, ensure you have the required libraries installed. You can install them using the following command:



```
$ pip install tkinter selenium beautifulsoup4 requests spacy

$ python -m spacy download en_core_web_sm
```




Also, make sure you have the Chrome WebDriver installed and available in your system's PATH.

Project Overview 📝

The extract_main_content(url) function scrapes the main content of a given website URL. It uses selenium with a headless Chrome browser to render the website and then applies BeautifulSoup to extract the main content. If it fails to find the main content, it extracts all possible content from the website's HTML source.

The extract_and_save_main_content() function opens a GUI window using tkinter. It prompts the user to enter a website URL and select a location to save the extracted text. After clicking the "Save" button, the program extracts the main content and applies NLP to filter out stop words and punctuation. Finally, it saves the filtered text to the selected file.

Usage 🚀


-Run the script.

-The GUI window will appear. 🖥️.

-Enter the URL of the website you want to extract the main content from.

-Click the "Save" button to save the extracted text to a file. 💾

-The text will be filtered using NLP to remove stop words and punctuation.


Note: The project uses headless Chrome to scrape websites. If you encounter any issues, make sure you have the Chrome WebDriver properly set up and that the website you are trying to scrape allows web scraping.

Enjoy extracting and saving website content with ease! Happy coding! 😄
