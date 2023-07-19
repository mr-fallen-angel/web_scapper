import tkinter as tk
from tkinter import filedialog
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import os 
import spacy
os.environ['KMP_DUPLICATE_LIB_OK']='TRUE'
def extract_main_content(url):
    options = Options()
    options.headless = True
    options.add_argument("--disable-dev-shm-usage")  
    options.add_argument("--no-sandbox")  
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    time.sleep(5)

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'html.parser')
    # Main content can be added as this is a growing model most websites are unique
    main_content = soup.find('div', id='mw-parser-output') or soup.find('main') or soup.find('article') or \
                   soup.find('class_', id='content') or soup.find('div', id='content') or soup.find('class_', id='content') \
                   or soup.find('div', id='root') or soup.find('class_', id='article-content-wrapper') \
                   or soup.find('class_', id='scope') or soup.find('div', id='docs-body') \
                   or soup.find('class', id='container article-section')
    if main_content:
        text = main_content.get_text()
        text = ' '.join(text.split())

        return text
    else:
        print("Failed to find main content on the website.")
        print("Extracting all possible content...")
        # Get all possible HTML content of the website
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text

            soup = BeautifulSoup(content, 'html.parser')

            # Cleaning
            text = soup.get_text()

            text = ' '.join(text.split())

            return text
    print("All possible content extracted")

    driver.quit()

def extract_and_save_main_content():
    nlp = spacy.load("en_core_web_sm")

    window = tk.Tk()

    def open_file_dialog():
        output_file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if output_file_path:
            website_url = entry.get()
            text = extract_main_content(website_url)

            if text:
                doc = nlp(text)
                filtered_content = [token.text for token in doc if not token.is_stop and not token.is_punct]
                filtered_text = ' '.join(filtered_content)

                with open(output_file_path, 'w', encoding='utf-8') as file:
                    file.write(filtered_text)

    label = tk.Label(window, text="Website URL:")
    label.pack()

    entry = tk.Entry(window)
    entry.pack()

    button = tk.Button(window, text="Save", command=open_file_dialog)
    button.pack()

    window.title('Website Text Extractor')
    window_width = 600
    window_height = 400
    window_position_x = 100
    window_position_y = 100
    window.geometry(f"{window_width}x{window_height}+{window_position_x}+{window_position_y}")
    window.mainloop()


extract_and_save_main_content()
 
