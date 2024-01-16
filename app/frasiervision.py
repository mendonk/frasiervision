import os
import script_scraper
import script_loader
import script_chat
import logging
import glob

from script_loader import vstore, ASTRA_DB_COLLECTION

def main():
    logging.basicConfig(level=logging.ERROR, filename='error_log.txt', filemode='w',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    pdf_files_exist = len(glob.glob('./pdfs/*.pdf')) > 0
    vectors_exist = len(vstore.astra_db.collection(ASTRA_DB_COLLECTION).find()) > 0

    if pdf_files_exist:
        print(str(len(glob.glob('./pdfs/*.pdf'))) + " PDFs exist, no downloading required.")
    else:
        print("PDFs don't exist, scraping scripts...")
        try:
            script_scraper.run()
        except Exception as e:
            logging.error(f"Error in script_scraper: {e}")

    if vectors_exist:
        print(str(len(vstore.astra_db.collection(ASTRA_DB_COLLECTION).find())) + " or more vectors exist, no embedding required.")
    else:
        print("Vectors don't exist, embedding scripts...")
        try:
            script_loader.run()
        except Exception as e:
            logging.error(f"Error in script_loader: {e}")

    # Run script_chat regardless of the above conditions
    try:
        script_chat.run()
    except Exception as e:
        logging.error(f"Error in script_chat: {e}")

if __name__ == '__main__':
    main()
