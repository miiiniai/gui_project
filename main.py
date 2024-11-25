import main_ui as mu 


class main():
    def __init__(self):
        super().__init__()
        self.ui = mu.main_window()

if __name__ == "__main__":
    import sys
    app = mu.QApplication(sys.argv)
    main_file = main()
    main_file.ui.show()
    sys.exit(app.exec_())



