import console_engine

# start finction
def main():
    while True:
        user_command: str = console_engine.get_promt_from_user()
        console_engine.perform_command(user_command)



if __name__ == "__main__":
    main()