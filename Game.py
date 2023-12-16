from utils import load_image, load_images
from pygame.locals import *
from docx import Document
from player import Player
from buff import Buff
from car import Car
from menu import *
import pygame, sys, smtplib, random, re, time, Aready, TakePhotos, os, FaceID

class TextInput:
    def __init__(self, name, screen, font, position, color, width, height):
        self.text = name  
        self.screen = screen  
        self.font = font  
        self.position = position  
        self.color = color
        self.width = width
        self.height = height
        self.cursor_visible = True
        self.cursor_timer = 0
        self.cursor_switch_interval = 400
        self.draw()
    def draw(self):
        self.username_f = self.font.render(f'{self.text}', True, (0, 0, 0))
        self.name_box = self.username_f.get_rect(midleft=self.position)
        self.rect = pygame.draw.rect(self.screen, self.color, (self.position[0] - 5, self.position[1] - 15, self.width, self.height))
        self.screen.blit(self.username_f, self.name_box)
    def update_text(self, new_text):
        self.text = new_text
    def update_cursor(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.cursor_timer > self.cursor_switch_interval:
            self.cursor_visible = not self.cursor_visible
            self.cursor_timer = current_time
        if self.cursor_visible:
            pygame.draw.line(self.screen, (0, 0, 0), (self.name_box.right + 2, self.name_box.top + 2), (self.name_box.right + 2, self.name_box.bottom - 2), 2)

class Button:
    def __init__(self, name, screen, position, width, height):
        self.name = name
        self.screen = screen
        self.position = position
        self.width = width
        self.height = height
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.position
    def draw(self, border_radius, color):
        pygame.draw.rect(self.screen, color, self.rect, border_radius = border_radius)
        self.button_rect = self.name.get_rect(center=self.rect.center)
        self.screen.blit(self.name, self.button_rect.topleft)

class Gmail:
    def is_gmail_address(self, email):
        self.pattern = r'^[a-zA-Z0-9_.+-]+@gmail\.com$'
        return re.match(self.pattern, email) is not None
    def send_email(self, receiver_email):
        try:
            self.sender_email = "daihiep10092005@gmail.com"     
            self.password = "jmmq mczp qyfi pngi"
            self.verification_code = ''.join(random.choice('0123456789') for i in range(6))
            self.session = smtplib.SMTP('smtp.gmail.com', 587)
            self.session.starttls()
            self.session.login(self.sender_email, self.password)
            self.subject = 'Subject: XÁC NHẬN ĐĂNG KÝ TÀI KHOẢN GEARHEADS&GAMBLERS!'
            self.content = f'Mã xác nhận đăng ký của bạn là {self.verification_code}.'
            self.message = f'{self.subject}\n\n{self.content}'
            self.message = self.message.encode("utf-8")
            self.session.sendmail(self.sender_email, receiver_email, self.message)
            print('Mail sent successfully')
            return True
        except Exception as e:
            print(f"Lỗi khi gửi email: {str(e)}")
            return False

class Box:
    def __init__(self, text, screen, font, position, color, width, height):
        self.text = text
        self.screen = screen
        self.font = font
        self.position = position
        self.color = color
        self.width = width
        self.height = height
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.position
    def draw(self):
        self.setup_f = self.font.render(f'{self.text}', True, (0, 0, 0))
        pygame.draw.rect(self.screen, self.color, self.rect, border_radius = 10)
        self.box_rect = self.setup_f.get_rect(center=self.rect.center)
        self.screen.blit(self.setup_f, self.box_rect.topleft)
    def update_text(self, new_text):
        self.text = new_text 

class Login_Game:
    def __init__(self):
        pygame.init()
        self.ID_Login =[0]
        self.screenWidth = 1268
        self.screenHeight = 746
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.Gamename = pygame.display.set_caption('GEARHEADS&GAMBLERS')
        self.background = pygame.image.load(r'Picture\background.png').convert_alpha()
        self.logo = pygame.image.load(r'Picture/LOGO.png')
        self.logo = pygame.display.set_icon(self.logo)
        self.background = pygame.transform.scale(self.background, (self.screenWidth, self.screenHeight))
        self.Face_ID_1 = pygame.image.load(r'Picture\Face_ID_1.png')
        self.Face_ID_1 = pygame.transform.scale(self.Face_ID_1, (90, 90))
        self.Face_ID_1_rect = self.Face_ID_1.get_rect()
        self.Face_ID_1_rect.topleft = (self.screenWidth // 3 + 310, self.screenHeight // 3 + 265)
        self.Face_ID_2 = pygame.image.load(r'Picture\Face_ID_2.png')
        self.Face_ID_2 = pygame.transform.scale(self.Face_ID_2, (85, 85))
        self.Game_font = pygame.font.Font(r'Font\seguili.ttf', 20)
        self.Game_font_setup = pygame.font.Font(r'Font\segoeui.ttf', 30)
        self.Game_font_button_send = pygame.font.Font(r'Font\ARIAL.TTF', 15)
        self.Game_font_button = pygame.font.Font(r'Font\ARIAL.TTF', 20)
        self.name = "Username"
        self.pas = "Password"
        self.conpas = "Confirm password"
        self.email = "Email"
        self.verify = 'Verity'
        self.announcement = ''
        self.mode = 'LOGIN'
        self.check = ''
        self.setup = ''
        self.docx_filename = "Accounts.docx"
        self.gmail = Gmail()
        self.money = 500
        self.match = 0
        self.win = 0
        self.lose = 0
        self.cursor_click = [False, False, False, False, False]
        self.verify_check = False
        self.gmail_codecheck = False
        self.button_click_send = False
        self.Face_ID_1_click = False
        self.Clock = pygame.time.Clock()
        self.username_rect = TextInput(self.name, self.screen, self.Game_font, (self.screenWidth // 3, self.screenHeight // 3), (255, 255, 255), 400, 30)
        self.password_rect = TextInput(self.pas, self.screen, self.Game_font, (self.screenWidth // 3, self.screenHeight // 3 + 50), (255, 255, 255), 400, 30)
        self.conpasword_rect = TextInput(self.conpas, self.screen, self.Game_font, (self.screenWidth // 3, self.screenHeight // 3 + 100), (255, 255, 255), 400, 30)
        self.email_rect = TextInput(self.email, self.screen, self.Game_font, (self.screenWidth // 3, self.screenHeight // 3 + 150), (255, 255, 255), 400, 30)
        self.verify_rect = TextInput(self.verify, self.screen, self.Game_font, (self.screenWidth // 3 + 44 , self.screenHeight // 3 + 185), (255, 255, 255), 300, 30)
        self.announcement_rect = TextInput(self.announcement, self.screen, self.Game_font, (self.screenWidth // 3 , self.screenHeight // 3 + 235), (220, 240, 230), 400, 30)
        self.Setup = Box(self.setup, self.screen, self.Game_font_setup, (self.screenWidth // 3 + 200, self.screenHeight // 3 - 75), (0, 128, 0), 500, 50)
        self.Login_button = Button(self.Game_font_button.render('LOGIN', True, (0, 0, 0)), self.screen, (self.screenWidth // 3 + 145, self.screenHeight // 3 + 285), 275, 30)
        self.SignUp_button = Button(self.Game_font_button.render('SIGN UP', True, (0, 0, 0)), self.screen, (self.screenWidth // 3 + 145, self.screenHeight // 3 + 335), 275, 30)
        self.send_rect = Button(self.Game_font_button_send.render('Send', True, (0, 0, 0)), self.screen, (self.screenWidth // 3 + 365, self.screenHeight // 3 + 185), 50, 30)

    def get_ID(self):
        return self.ID_Login[0]
    
    def save_account(self, username, password, money, match, win, lose):
        try:
            if os.path.exists(self.docx_filename):
                doc = Document(self.docx_filename)
            else:
                doc = Document()
                table = doc.add_table(rows=1, cols=7)
                table.cell(0, 0).text = "ID"
                table.cell(0, 1).text = "Tên đăng nhập"
                table.cell(0, 2).text = "Mật khẩu"
                table.cell(0, 3).text = "Số tiền"
                table.cell(0, 4).text = "Số trận đã chơi"
                table.cell(0, 5).text = "Số trận thắng"
                table.cell(0, 6).text = "Số trận thua"
            if not doc.tables:
                doc.add_table(rows=1, cols=7)
                table = doc.tables[0]
                table.cell(0, 0).text = "ID"
                table.cell(0, 1).text = "Tên đăng nhập"
                table.cell(0, 2).text = "Mật khẩu"
                table.cell(0, 3).text = "Số tiền"
                table.cell(0, 4).text = "Số trận đã chơi"
                table.cell(0, 5).text = "Số trận thắng"
                table.cell(0, 6).text = "Số trận thua"
            for table in doc.tables:
                for row in table.rows:
                    if row.cells[1].text == username:
                        if row.cells[3].text == '0' and row.cells[4].text == '0' and row.cells[5].text == '0' and row.cells[6].text == '0':
                            print(f"Người dùng '{username}' đã tồn tại. Không thể đăng ký.")
                            return False
                        else:
                            row_cells = row.cells
                            row_cells[2].text = password
                            row_cells[3].text = str(money)
                            row_cells[4].text = str(match)
                            row_cells[5].text = str(win)
                            row_cells[6].text = str(lose)

                            doc.save(self.docx_filename)
                            return True
            if len(doc.tables) > 0 and len(doc.tables[0].rows) > 1:
                last_id = int(doc.tables[0].cell(len(doc.tables[0].rows) - 1, 0).text)
            else:
                last_id = 0
            new_id = last_id + 1
            new_id_str = f"{new_id:03d}" 
            table = doc.tables[0] 
            row_cells = table.add_row().cells
            row_cells[0].text = new_id_str
            row_cells[1].text = username
            row_cells[2].text = password 
            row_cells[3].text = str(money)
            row_cells[4].text = str(match)
            row_cells[5].text = str(win)
            row_cells[6].text = str(lose)
            print('Tài khoản đã được lưu!')
            doc.save(self.docx_filename)
            return True
        except Exception as e:
            print(f"Lỗi khi lưu tài khoản vào tệp Word: {str(e)}")
            return False

    def Count_id(self):
        doc = Document(self.docx_filename)
        if len(doc.tables) > 0 and len(doc.tables[0].rows) > 1:
            last_id = int(doc.tables[0].cell(len(doc.tables[0].rows) - 1, 0).text)
        else:
            last_id = 0
        id_count = last_id
        id_count_str = f"{id_count:03d}"
        return id_count_str
    def check_login(self, username, password):
        try:
            doc = Document(self.docx_filename)
            for table in doc.tables:
                for row in table.rows:
                    stored_username = row.cells[1].text
                    stored_password = row.cells[2].text
                    if username == stored_username and password == stored_password:
                        return True
            return False
        except Exception as e:
            print(f"Lỗi khi kiểm tra thông tin đăng nhập từ tệp Word: {str(e)}")
            return False  
        
    def SignUp(self):
        if self.mode == 'LOGIN':
            self.username_rect.update_text('Username')
            self.password_rect.update_text('Password')
            self.conpasword_rect.update_text('Confirm password')
            self.email_rect.update_text('Email')
            self.announcement = ''
            self.mode = 'SIGN UP'
            self.check = 'SIGN UP'
        elif self.mode == 'SIGN UP':
            self.check = 'SIGN UP'
            self.samename = 0
            if self.username_rect.text == "Username" or self.username_rect.text == '':
                self.announcement_rect.update_text("Please enter your username.")
            elif self.password_rect.text == "Password" or self.conpasword_rect.text == '':
                self.announcement_rect.update_text("Please enter your password.")
            elif self.conpasword_rect.text == "Confirm password" or self.password_rect.text == '':
                self.announcement_rect.update_text("Please enter your confirm password.")
            elif self.email_rect.text == "Email" or self.email_rect.text == '':
                self.announcement_rect.update_text("Please enter your email: 'example@gmail.com'.")
            elif self.conpasword_rect.text != self.password_rect.text :
                self.username_rect.update_text('Username')
                self.password_rect.update_text('Password')
                self.conpasword_rect.update_text('Confirm password')
                self.email_rect.update_text('Email')
                self.announcement_rect.update_text('Passwords do not match. Please try again.')
            elif self.gmail.is_gmail_address(self.email_rect.text) == False:
                self.announcement_rect.update_text("Email address is not valid.Please enter your email again.")
            if not self.samename:
                doc = Document(self.docx_filename)
                for table in doc.tables:
                    for row in table.rows:
                        stored_username = row.cells[1].text
                        if self.username_rect.text == stored_username:
                            self.announcement_rect.update_text("The account already exists, please give different username.")
                            self.samename = 1
            if not self.samename:
                if self.gmail.is_gmail_address(self.email_rect.text) == True:
                    if self.gmail.send_email(self.email_rect.text):
                        self.announcement_rect.update_text("Check your gmail, then enter the Verification Code.")
                        self.verify_check = True
                        self.SignUp_button.name = self.Game_font_button.render('RESEND', True, (0, 0, 0))
                    else:
                        self.announcement_rect.update_text("Email address is not valid.Please enter your email again.")

 
    def Login(self):
        if self.mode == 'SIGN UP':
            self.username_rect.update_text('Username')
            self.password_rect.update_text('Password')
            self.conpasword_rect.update_text('Confirm password')
            self.email_rect.update_text('Email')
            self.announcement = ''
            self.announcement_rect.update_text(self.announcement)
            self.mode = 'LOGIN'
            self.check = 'LOGIN'
        elif self.mode == 'LOGIN':
            self.check = 'LOGIN'
            if self.username_rect.text == "Username" or self.username_rect.text == '':
                self.announcement_rect.update_text("Please enter your username.")
            elif self.password_rect.text == "Password" or self.password_rect.text == '':
                self.announcement_rect.update_text("Please enter your password.")
            elif self.check_login(self.username_rect.text, self.password_rect.text):
                try:
                    doc = Document(self.docx_filename)
                    for table in doc.tables:
                        for row in table.rows:
                            stored_username = row.cells[1].text
                            myID = row.cells[0].text
                            if self.username_rect.text == stored_username:
                                return myID
                    return False
                except Exception as e:
                    return False


    def Send(self):

        if self.gmail.verification_code == self.verify_rect.text:
            self.gmail_codecheck = True
        else:
            self.verify_rect.update_text('')
            self.announcement_rect.update_text("Sorry, the verification code you entered is incorrect.")
        if self.gmail_codecheck:
            if self.save_account(self.username_rect.text, self.password_rect.text, self.money, self.match, self.win, self.lose):
                return True
            else:
                self.announcement_rect.update_text(f"The account '{self.username_rect.text}' already exists. Cannot add.")

    def Run(self):
        LoginGame = 0
        while not LoginGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if self.username_rect.rect.collidepoint(x, y):
                        if self.password_rect.text == '':
                            self.password_rect.update_text("Password")
                        if self.conpasword_rect.text == '':
                            self.conpasword_rect.update_text("Confirm password")
                        if self.email_rect.text == '':
                            self.email_rect.update_text("Email")
                        if self.verify_rect.text == '':
                            self.verify_rect.update_text("Verity")
                        self.cursor_click = [True, False, False, False, False]
                        self.check = "Username"
                        self.username_rect.update_text('')
                        self.announcement_rect.update_text('')
                    elif self.password_rect.rect.collidepoint(x, y):
                        if self.username_rect.text == '':
                            self.username_rect.update_text("Username")
                        if self.conpasword_rect.text == '':
                            self.conpasword_rect.update_text("Confirm password")
                        if self.email_rect.text == '':
                            self.email_rect.update_text("Email")
                        if self.verify_rect.text == '':
                            self.verify_rect.update_text("Verity")
                        self.cursor_click = [False, True, False, False, False]
                        self.check = "Password"
                        self.password_rect.update_text('')
                        self.announcement_rect.update_text('')
                    elif self.conpasword_rect.rect.collidepoint(x, y):
                        if self.username_rect.text == '':
                            self.username_rect.update_text("Username")
                        if self.password_rect.text == '':
                            self.password_rect.update_text("Password")
                        if self.email_rect.text == '':
                            self.email_rect.update_text("Email")
                        if self.verify_rect.text == '':
                            self.verify_rect.update_text("Verity")
                        self.cursor_click = [False, False, True, False, False]
                        self.check = "Confirm password"
                        self.conpasword_rect.update_text('')
                        self.announcement_rect.update_text('')
                    elif self.email_rect.rect.collidepoint(x, y):
                        if self.username_rect.text == '':
                            self.username_rect.update_text("Username")
                        if self.password_rect.text == '':
                            self.password_rect.update_text("Password")
                        if self.conpasword_rect.text == '':
                            self.conpasword_rect.update_text("Confirm password")
                        if self.verify_rect.text == '':
                            self.verify_rect.update_text("Verity")
                        self.cursor_click = [False, False, False, True, False]
                        self.check = "Email"
                        self.email_rect.update_text('')    
                        self.announcement_rect.update_text('')
                    elif self.SignUp_button.rect.collidepoint(x, y):
                        self.announcement_rect.update_text('')
                        self.cursor_click = [False, False, False, False, False]
                        self.SignUp()
                    elif self.Login_button.rect.collidepoint(x, y):
                        self.announcement_rect.update_text('')
                        self.cursor_click = [False, False, False, False, False]
                        self.ID_Login[0] = self.Login()
                        if self.ID_Login[0]:
                            LoginGame = 1
                            break
                        else:
                            self.username_rect.update_text('Username')
                            self.password_rect.update_text('Password')
                            self.announcement_rect.update_text('Incorrect username or password.')
                    elif self.verify_check and self.verify_rect.rect.collidepoint(x, y):
                        if self.username_rect.text == '':
                            self.username_rect.update_text("Username")
                        if self.password_rect.text == '':
                            self.password_rect.update_text("Password")
                        if self.conpasword_rect.text == '':
                            self.conpasword_rect.update_text("Confirm password")
                        if self.email_rect.text == '':
                            self.email_rect.update_text("Email")
                        self.cursor_click = [False, False, False, False, True]
                        self.check = "Verity"
                        self.verify_rect.update_text('')
                        self.announcement_rect.update_text('')
                    elif self.verify_check and self.send_rect.rect.collidepoint(x, y):
                        self.cursor_click = [False, False, False, False, False]
                        self.button_click_send = True
                        self.button_click_time = pygame.time.get_ticks()
                        if self.Send():
                            time.sleep(2)
                            self.verify_check = False
                            self.SignUp_button.name = self.Game_font_button.render('SIGN UP', True, (0, 0, 0))
                            Aready.Aready()
                            TakePhotos.TakePhotos(Login_Game.Count_id())
                            self.ID_Login[0] = Login_Game.Count_id()
                            LoginGame = 1
                            break
                    elif self.Face_ID_1_rect.collidepoint(x, y):
                            self.Face_ID_1_click = True
                            self.Face_ID_click_time = pygame.time.get_ticks()
                            self.ID_Login[0] = FaceID.FaceID(FaceID.classNames)
                            if  self.ID_Login[0]:
                                LoginGame = 1
                                break
                    else:
                        if self.username_rect.text == '':
                            self.username_rect.update_text("Username")
                        if self.password_rect.text == '':
                            self.password_rect.update_text("Password")
                        if self.conpasword_rect.text == '':
                            self.conpasword_rect.update_text("Confirm password")
                        if self.email_rect.text == '':
                            self.email_rect.update_text("Email")
                        if self.verify_rect.text == '':
                            self.verify_rect.update_text("Verity")
                        self.cursor_click = [False, False, False, False, False]
                if event.type == pygame.KEYDOWN:
                    if self.check == "Username":
                        if event.key == K_BACKSPACE:
                            self.username_rect.update_text(self.username_rect.text[:-1])
                        else:
                            if len(self.username_rect.text) < 25:
                                self.username_rect.update_text(self.username_rect.text + event.unicode)
                    elif self.check == "Password":
                        if self.username_rect.text == '':
                            self.username_rect.update_text("Username")
                        if event.key == K_BACKSPACE:
                            self.password_rect.update_text(self.password_rect.text[:-1])
                        else:
                            if len(self.password_rect.text) < 25:
                                self.password_rect.update_text(self.password_rect.text + event.unicode)
                    elif self.mode == 'SIGN UP' and self.check == "Confirm password":
                        if self.password_rect.text == '':
                            self.password_rect.update_text("Password")
                        if event.key == K_BACKSPACE:
                            self.conpasword_rect.update_text(self.conpasword_rect.text[:-1])
                        else:
                            if len(self.conpasword_rect.text) < 25:
                                self.conpasword_rect.update_text(self.conpasword_rect.text + event.unicode)
                    elif self.mode == 'SIGN UP' and self.check == "Email":
                        if self.conpasword_rect.text == '':
                            self.conpasword_rect.update_text("Confirm password")
                        if event.key == K_BACKSPACE:
                            self.email_rect.update_text(self.email_rect.text[:-1])
                        else:
                            if len(self.email_rect.text) < 40:
                                self.email_rect.update_text(self.email_rect.text + event.unicode)
                    elif self.mode == 'SIGN UP' and self.check == "Verity":
                        if self.email_rect.text == '':
                            self.email_rect.update_text("Email")    
                        if event.key == K_BACKSPACE:
                            self.verify_rect.update_text(self.verify_rect.text[:-1])
                        else:
                            if len(self.verify_rect.text) < 15:
                                self.verify_rect.update_text(self.verify_rect.text + event.unicode)
            if(LoginGame):
                break
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.background, (0, 0))
            pygame.draw.rect(self.screen, (220, 240, 230), (self.screenWidth // 3 - 50, self.screenHeight // 3 - 100, 500, 480), border_radius = 20)
            self.Setup.draw()
            if self.mode == 'LOGIN':
                self.Setup.text = self.mode
            elif self.mode == 'SIGN UP':
                self.Setup.text = self.mode
            self.username_rect.draw()
            if self.cursor_click[0]:
                self.username_rect.update_cursor()
            self.password_rect.draw()
            if self.cursor_click[1]:
                self.password_rect.update_cursor()
            if self.mode == 'SIGN UP':
                self.conpasword_rect.draw()
                if self.cursor_click[2]:
                    self.conpasword_rect.update_cursor()
                self.email_rect.draw()
                if self.cursor_click[3]:
                    self.email_rect.update_cursor()
            if self.mode == 'SIGN UP':
                self.SignUp_button.draw(10, (24, 119, 242))
            else:
                self.SignUp_button.draw(10, (240, 240, 240))
            if self.mode == 'LOGIN':
                self.Login_button.draw(10, (24, 119, 242))
            else:
                self.Login_button.draw(10, (240, 240, 240))
            if self.Face_ID_1_click and pygame.time.get_ticks() - self.Face_ID_click_time >= 400:
                self.Face_ID_1_click = False
            if self.Face_ID_1_click:
                self.screen.blit(self.Face_ID_2, self.Face_ID_1_rect.topleft)
            else:
                self.screen.blit(self.Face_ID_1, self.Face_ID_1_rect.topleft)
            self.announcement_rect.draw()
            if self.mode == 'SIGN UP' and self.verify_check:
                self.verify_rect.draw()
                if self.cursor_click[4]:
                    self.verify_rect.update_cursor()
                if self.button_click_send and pygame.time.get_ticks() - self.button_click_time >= 400:
                    self.button_click_send = False
                if self.button_click_send:
                    self.send_rect.draw(0, (24, 119, 242))
                else:
                    self.send_rect.draw(0, (240, 240, 240))
            pygame.display.update()
            self.Clock.tick(60)

Login_Game = Login_Game()
Login_Game.Run()

class Game:
    def __init__(self):
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        #Sreen and surface...
        self.screen_size = [1400, 700]
        self.screen = pygame.display.set_mode((self.screen_size[0], self.screen_size[1]))
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.display = pygame.Surface(((self.screen.get_width(), self.screen.get_height())))
        self.cursor_point = pygame.image.load('data/cursor/cursor_point2.png').convert_alpha()
        self.cursor_click = pygame.image.load('data/cursor/cursor_click2.png').convert_alpha()
        pygame.display.set_caption('Gearheads&Gamblers')

        #Clock, font... 
        self.clock = pygame.time.Clock()
        self.LightPixel_font = pygame.font.Font('data/font/LightPixel.ttf', 30)
        self.SmallerLightPixel_font = pygame.font.Font('data/font/LightPixel.ttf', 20)
        self.BiggerLightPixel_font = pygame.font.Font('data/font/LightPixel.ttf', 40)
        self.SoftnBig_font = pygame.font.Font('data/font/Pixeltype.ttf', 50)
        self.Arcade_font = pygame.font.Font('data/font/Arcade.ttf', 60)
        self.DIRECTION_font = pygame.font.Font('data/font/LightPixel.ttf', 100)
        
        #User's variable
        self.ID = Login_Game.get_ID()
        self.player_name = get_information(self.ID)[1]
        self.money = get_information(self.ID)[3]
        if self.money < 100:
            self.bet = 0
        else:
            self.bet = get_information(self.ID)[3]
        
        #Game variable
        self.player_set = 1
        self.player_index = 1
        self.player_status = 1
        self.race_started = False
        self.base_color = "WHITE"
        
        #Map variable
        self.map_index = 1
        self.map_size = "SMALL"
        
        #Assets
        self.assets = {
            'loadgame' : load_image('data/graphics/interface/BACKGROUND_2.png'),
            'background' : load_image('data/graphics/background/background.png'),
            'players' : load_images(f'data/player/{self.player_set}/{self.player_index}/{self.player_status}/'),
            'map_preview' : load_images("data/map/preview"),
            'map' : load_image(f'data/map/{self.map_index}/{self.map_size}.png'),
            'cars' : load_images(f'data/graphics/car/{self.player_set}/{self.player_index}'),
            'buffs' : load_images('data/magic'),
            'board' : load_image('data/graphics/background/board.png'),
            'ranking' : load_image('data/graphics/background/ranking.png'),
        }
        
        #Image
        self.button_image = pygame.image.load('data/small.png').convert_alpha()
        self.dialogue_image = pygame.image.load('data/dialogue.png').convert_alpha()
        self.long_button_image = pygame.image.load('data/long.png').convert_alpha()
        
        #Game control variable
        self.game_running = True
        self.game_state = 1
        self.main_menu_state = 1
        self.size_state = 0
        self.credits_state = 0
        self.minigame_state = 0
        
        self.player_state = 0
        self.map_state = 0
        self.button_pressed = False
        self.text_state = 0
        self.finish_line_x = self.width * 0.9
        self.rank = 0
        
        #Player 
        # (Set, Type, Status) #
        self.player_group = pygame.sprite.Group()
        self.player1 = self.player_group.add(Player(self,self.player_set,1,self.player_status,(self.width * 0.2, self.height / 2)))
        self.player2 = self.player_group.add(Player(self,self.player_set,2,self.player_status,(self.width * 0.35, self.height / 2)))
        self.player3 = self.player_group.add(Player(self,self.player_set,3,self.player_status,(self.width * 0.5, self.height / 2)))
        self.player4 = self.player_group.add(Player(self,self.player_set,4,self.player_status,(self.width * 0.65, self.height / 2)))
        self.player5 = self.player_group.add(Player(self,self.player_set,5,self.player_status,(self.width * 0.8, self.height / 2)))
        self.main_player = pygame.sprite.GroupSingle()
        self.player =  self.main_player.add(Player(self,self.player_set,self.player_index,self.player_status,(self.width * 0.3, self.height / 2)))
        
        #Car
        # (Set, Type, Status) #
        self.car_group = pygame.sprite.Group()  
        self.car1 = self.car_group.add(Car(self,self.player_set,1,self.player_status,(100, self.height * 0.55)))
        self.car2 = self.car_group.add(Car(self,self.player_set,2,self.player_status,(100, self.height * 0.65)))
        self.car3 = self.car_group.add(Car(self,self.player_set,3,self.player_status,(100, self.height * 0.75)))
        self.car4 = self.car_group.add(Car(self,self.player_set,4,self.player_status,(100, self.height * 0.85)))
        self.car5 = self.car_group.add(Car(self,self.player_set,5,self.player_status,(100, self.height * 0.94)))
        self.main_car = pygame.sprite.GroupSingle()
        self.car = self.main_car.add(Car(self,self.player_set,self.player_index,self.player_status,(self.width * 0.6, self.height / 2)))

        #Timer
        self.buff_group = pygame.sprite.Group()
        self.buff_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.buff_timer, 2000)
        self.start_time = 0
        
    def current(self):
        if self.game_state != 5:
            self.current_time = 0
        else:
            self.current_time = pygame.time.get_ticks() - self.start_time
        if self.current_time > 4000:
            self.current_time = 0
        return self.current_time
            
    def run(self):
        while self.game_running:
            #Update variable
            self.width = self.screen.get_width()
            self.height = self.screen.get_height()
            self.mouse_pos = pygame.mouse.get_pos()
            self.display = pygame.Surface(((self.width, self.height)))
            
            #State 1
            if self.game_state == 1:
                button_animation(self)
                self.display.blit(pygame.transform.scale(self.assets['loadgame'], (self.width, self.height)), (0, 0))
                self.startgame_surface = self.LightPixel_font.render(self.startgame_text, 0, (111, 196, 169))
                self.startgame_rect = self.startgame_surface.get_rect(center = (self.display.get_width() / 2, self.display.get_height() * 0.875))
                self.display.blit(self.startgame_surface, self.startgame_rect)
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    self.game_state = 2
            
            #State 2
            elif self.game_state == 2:
                if self.main_menu_state == 1:
                    main_menu(self, self)
                if self.credits_state == 1:
                    credits_menu(self)
                if self.minigame_state == 1:
                    minigame1(self, self)
                                
            #State 3
            elif self.game_state == 3:
                Player.update_pos(self)
                choose_player_set_menu(self)
                
            #State 4
            elif self.game_state == 4:
                choose_player_menu(self)
                self.start_time = pygame.time.get_ticks()
                
            #State 5
            elif self.game_state == 5:
                Car.update_pos(self, self)
                game_play(self)
                
                for event in pygame.event.get():
                    if event.type == self.buff_timer and self.race_started:
                        self.buff_group.add(Buff(self))
                self.buff_group.update()
                
                if self.current() < 3000 and self.current() > 0:
                    self.count_down_text = self.BiggerLightPixel_font.render(str(3 - int(self.current() / 1000)), 0, (111, 196, 169))
                    self.count_down_rect = self.count_down_text.get_rect(center = (self.display.get_width() / 2, self.display.get_height() / 2))
                    self.display.blit(self.count_down_text, self.count_down_rect)
                elif self.current() >= 3000 and self.current() < 4000:
                    self.count_down_text = self.BiggerLightPixel_font.render("GO!", 0, (111, 196, 169))
                    self.count_down_rect = self.count_down_text.get_rect(center = (self.display.get_width() / 2, self.display.get_height() / 2))
                    self.display.blit(self.count_down_text, self.count_down_rect)
                if self.current() >= 3000:
                    self.game.race_started = True
                    
            #State 6
            elif self.game_state == 6:
                ranking(self)
                
            #State 7
            elif self.game_state == 7:
                leaderboard(self, self)
                
            #Mouse cursor
            pygame.mouse.set_visible(False)
            if pygame.mouse.get_pressed()[0]:
                self.display.blit(self.cursor_click, (self.mouse_pos[0] - 10, self.mouse_pos[1] - 10))
            else:
                self.display.blit(self.cursor_point, (self.mouse_pos[0] - 10, self.mouse_pos[1] - 10))
            
            #Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()            
                        
            #Update screen
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))        
            pygame.display.update()           
            self.clock.tick(60)

Game().run()