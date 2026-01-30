from database import create_tables, add_user, add_task, get_tasks

create_tables()

while True:
    print("\n1 - kullanıcı oluştur")
    print("2 - görev ekle")
    print("3 - görevleri listele")
    print("4 - çıkış")

    secim = input("seçim: ")

    try:
        if secim == "1":
            username = input("username: ")
            add_user(username)
            print("kullanıcı oluşturuldu")

        elif secim == "2":
            user_id = str(input("kullanıcı ID: "))
            task = input("görev: ")
            add_task(user_id, task)
            print("görev eklendi")

        elif secim == "3":
            user_id = str(input("kullanıcı ID: "))
            tasks = get_tasks(user_id)

            if tasks:
                print("\ngörevler:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task[0]}")
            else:
                print("bu kullanıcıya ait görev yok.")

        elif secim == "4":
            print("çıkış yapılıyor")
            break

        else:
            print("geçersiz seçim")

    except Exception as e:
        print("Hata:", e)
