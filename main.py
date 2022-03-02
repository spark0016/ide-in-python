class EclipsaIDE:
    def __init__(self):
        def syntaxHightLight(evnt):
            def_h(editor, "lime")
            function_h(editor, "red")
            True_h(editor, "red")
            False_h(editor, "red")
            import_h(editor, "red")
            from_h(editor, "red")
            if_h(editor, "red")
            else_h(editor, "red")
            elif_h(editor, "red")
            try_h(editor, "red")
            except_h(editor, "red")
            for_h(editor, "red")
            while_h(editor, "red")
            yield_h(editor, "red")
            pass_h(editor, "red")
            break_h(editor, "red")
            continue_h(editor, "red")
            with_h(editor, "red")
            del_h(editor, "red")
            open_h(editor, "red")
            as_h(editor, "red")
            in_h(editor, "red")
            or_h(editor, "red")
            and_h(editor, "red")
            class_h(editor, "lime")
            print_h(editor, "red")
            int_h(editor, "red")
            float_h(editor, "red")
            str_h(editor, "red")
            return_h(editor, "red")
            input_h(editor, "red")
            None_h(editor, "red")
            global_h(editor, "red")
            Exception_h(editor, "red")

        def run():
            exec(editor.get("1.0", END))
        
        filename = ""
        _filetypes = [
            ('Text', '*.txt'),
                ('All files', '*'),
                ]

        def openFile():
            filename = filedialog.askopenfilename(initialdir = "/",
                                                title = "Select a File",
                                                filetypes = (("Text files",
                                                                "*.txt*"),
                                                            ("all files",
                                                                "*.*")))
        
        def save_file_as():
            filename = filedialog.asksaveasfilename(filetypes=_filetypes)
            f = open(filename, 'w')
            f.write(editor.get('1.0', 'end'))
            f.close()
        
        def save_file():
            if (filename == ""):
                save_file_as()
            else:
                f = open(filename, 'w')
                f.write(editor.get('1.0', 'end'))
                f.close()

        top = Tk()
        top.title("Eclipsa-IDE")
        top.configure(bg="#515151")

        top.bind('<Control-s>', save_file)

        _font = ("Consolas", 12, "bold")

        editor = Text(insertbackground="red", bg="#505050", fg="white")
        editor.configure(font=_font)
        editor.bind("<Key>", syntaxHightLight)

        menuBar = Menu(top)

        FILE = Menu(menuBar)
        FILE.add_command(label="Open", command=openFile)

        RUN = Menu(menuBar, tearoff=0)
        RUN.add_command(label="Run", command=run)

        menuBar.add_cascade(label="File", menu=FILE)
        menuBar.add_cascade(label="Run", menu=RUN)

        editor.pack(fill=BOTH, expand=True)

        top.config(menu=menuBar)
        top.mainloop()
