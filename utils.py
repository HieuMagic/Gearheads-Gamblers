from docx import Document
import pygame, os

def load_image(path):
    img = pygame.image.load(path).convert_alpha()
    return img

def load_images(path):
    images = []
    for img_name in os.listdir(path):
        images.append(load_image(path + '/' + img_name))
    return images

def get_text_size(self, text):
	self.text_width, self.text_height = self.LightPixel_font.size(text)
	return self.text_width, self.text_height

def get_image_size(self, image):
    self.image_width, self.image_height = image.get_width(), image.get_height()
    return self.image_width, self.image_height

def update_assets(self, assets):
    print(self.player_set, self.player_index)
    assets['cars'] = load_images(f'data/graphics/car/{self.player_set}/{self.player_index}')
    assets['players'] = load_images(f'data/player/{self.player_set}/{self.player_index}/{self.player_status}/')
    assets['map'] : load_image(f'data/map/{self.map_index}/{self.map_size}.png')

def count_child_folders(folder_path):
    count = 0
    for entry in os.scandir(folder_path):
        if entry.is_dir():
            count += 1
    return count

def count_images_in_folder(folder_path):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']  # Add more extensions if needed
    image_count = 0

    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            if any(file_name.lower().endswith(ext) for ext in image_extensions):
                image_count += 1
    return image_count

def get_information( id_user):
    docx_filename = "Accounts.docx"
    doc = Document(docx_filename)
    for table in doc.tables:
        for row in table.rows:
            if row.cells[0].text == id_user:
                username = row.cells[1].text
                password = row.cells[2].text
                money = int(row.cells[3].text)
                match = int(row.cells[4].text)
                win = int(row.cells[5].text)
                lose = int(row.cells[6].text)
                win_money = int(row.cells[7].text)
                lose_money = int(row.cells[8].text)
                information = [id_user, username, password, money, match, win, lose, win_money, lose_money]
                return information