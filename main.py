
import sys
print("MIIMenus Login v1.0 - User+SQL")

from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, 
                               QVBoxLayout, QWidget, QHBoxLayout)
from PySide6.QtCore import Qt, QTimer  # + QTimer
from PySide6.QtGui import QFont

class LoginMIIMenus(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Login UI construída")
        self.setWindowTitle("MIIMenus - Login")
        self.resize(450, 350)
        
        # Estilos (print exato)
        self.setStyleSheet("""
            QMainWindow { 
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #006400, stop:1 #006400); 
            }
            QLabel { color: white; font-size: 14px; }
            QLabel#titulo { color: #000000; font-size: 22px; font-weight: bold; }
            QLineEdit { 
                border: 2px solid #bdc3c7; border-radius: 5px; padding: 12px; 
                background: white; font-size: 14px; min-height: 20px;
            }
            QPushButton { 
                background: #4CAF50; color: white; border-radius: 8px; 
                padding: 12px 30px; font-weight: bold; font-size: 14px;
            }
            QPushButton:hover { background: #45a049; }
        """)
        
        central = QWidget()
        layout = QVBoxLayout(central)
        layout.setSpacing(18)
        layout.setContentsMargins(35, 35, 35, 35)
        
        # Cabeçalho: Título + Versão
        header_layout = QHBoxLayout()
        titulo = QLabel("MIIMenus - Login")
        titulo.setObjectName("titulo")
        titulo.setFont(QFont("Arial", 22, QFont.Bold))
        header_layout.addWidget(titulo)
        header_layout.addStretch()
        versao = QLabel("Versão 1.0")
        versao.setFont(QFont("Arial", 12))
        header_layout.addWidget(versao)
        layout.addLayout(header_layout)
        
        # Avatar cinza (print)
        avatar = QLabel()
        avatar.setStyleSheet("""
            background: #9E9E9E; border-radius: 45px; 
            min-width: 90px; min-height: 90px; border: 3px solid white;
        """)
        avatar.setAlignment(Qt.AlignCenter)
        layout.addWidget(avatar, alignment=Qt.AlignCenter)
        
        # Campo 1: Utilizador/PASS
        lbl_user = QLabel("Utilizador:")
        layout.addWidget(lbl_user)
        self.pass_input = QLineEdit()
        self.pass_input.setPlaceholderText("Digite o seu utilizador")
        self.pass_input.setEchoMode(QLineEdit.Password)  # **** cada user
        layout.addWidget(self.pass_input)
        
        # Campo 2: Ligação SQL (SEM label baixo)
        lbl_sql = QLabel("Ligação SQL:")
        layout.addWidget(lbl_sql)
        self.sql_input = QLineEdit()


        # Label status BD automática
        self.status_label = QLabel("Verificando...")
        self.status_label.setStyleSheet("color: orange; font-weight: bold; padding: 8px; background: rgba(0,0,0,0.3); border-radius: 5px;")
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)

        # Timer teste BD startup (1x)
        QTimer.singleShot(500, self.testa_ligacao_auto)  # 0.5s após abrir
        
        # Botão Entrar
        btn_entrar = QPushButton("Entrar")
        btn_entrar.clicked.connect(self.tenta_login)
        layout.addWidget(btn_entrar, alignment=Qt.AlignCenter)
        
        self.setCentralWidget(central)
        print("Login pronto")
        self.sql_input 

    def tenta_login(self):
        user_pass = self.pass_input.text()
        sql_conn = self.sql_input.text()
        print(f"Tentativa: PASS='{user_pass}' SQL='{sql_conn}'")
        
        # TESTE simples (melhorar com DB real)
        if user_pass and sql_conn:  # Não vazios
            print("Login OK! Abre menus...")
            # TODO: self.abre_tela_menus()
        else:
            print("Campos vazios!")
            
    def testa_ligacao_auto(self):
        sql_string = self.sql_input.text()
 

if __name__ == "__main__":
    print("Lançando app...")
    app = QApplication(sys.argv)
    login = LoginMIIMenus()
    login.show()
    print("Janela visível")
    sys.exit(app.exec())
