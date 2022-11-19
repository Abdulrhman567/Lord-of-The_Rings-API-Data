import requests

API_KEY = None #Enter your API key after creating you account

# Handling the URL and the Requests
class LondOfTheRingsData:
    def __init__(self, api_key) -> None:
        self.sections = ['book', 'movie','character', 'chapter','quote']
        self.base_url = 'https://the-one-api.dev/v2/.'
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
        }
        self.manage_section()

    def manage_section(self):
        self.section = input('Enter a section (book, movie, character, chapter, quote): ')
        if self.section in self.sections:
            self.final_url = f'{self.base_url}/{self.section}'
            if input(f'Do you want to get a particular {self.section}?? (y/n) ') == 'Y'.lower():
                self.manage_section_id()
        else: 
            print('Oops, Please make sure you selected one of the available sections!')
            self.manage_section()

    def manage_section_id(self): 
        self.section_id = input(f'Then please enter a {self.section} ID: ')
        self.final_url += f'/{self.section_id}'
        self.manage_deep_section()

    def manage_deep_section(self): 
        if self.section == 'book':
                if input(f'Do you want to get all the chapters of this pirticular {self.section} that you chose??(y/n) ') == 'Y'.lower():
                 self.final_url += '/chapter'
        elif self.section == 'movie' or self.section == 'character':
            if input(f'Do you want list all the quotes related to this {self.section} that you chose??(y/n) ') == 'Y'.lower:
                self.final_url += '/quote'
            
    def get_data(self):
        reponse = requests.get(url=self.final_url, headers=self.headers)
        reponse.raise_for_status
        print(reponse.text)


if __name__ == '__main__': 
    print("""Welcome to the Lord of the rings world where you can find anything related to lord of the rings books, movies and characters. with this awesome data provider and without further ado let's jump right to it.""")
    lotr_data = LondOfTheRingsData(API_KEY)
    lotr_data.get_data()
