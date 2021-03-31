# My_Kivy

<MyGrid>:

    name: name
    email: email

    GridLayout:
        cols:1
        size: root.width -200, root.height -200
        pos: 100, 100


        GridLayout:
            cols:2


            Label:
                text: "Name: "


            TextInput:
                id: name
                multiline:False


            Label:
                text: "Email: "


            TextInput:
                id: email
                multinline:False


        Button:
            text:"Submit"
            on_press: root.btn()
