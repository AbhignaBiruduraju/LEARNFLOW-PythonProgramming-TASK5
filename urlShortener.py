import pyperclip
import pyshorteners

urls = {}


def shortver(lu):
    a = pyshorteners.Shortener()
    su = a.tinyurl.short(lu)
    return su


def main():
    while True:
        b = (
            input("Type of operation to be done:(s:short l:long e:exit}: ")
            .strip()
            .lower()
        )
        if b == "s":
            lu = input("Input the url: ").strip()
            su = shortver(lu)
            urls[su] = lu
            pyperclip.copy(su)
            print(f"Shorter version of the input url: {su}")

        elif b == "l":
            su = input("Input the url: ").strip()
            lu = urls.get(su)
            if lu:
                pyperclip.copy(lu)
                print(f"Longer version of the url: ")

            else:
                print("Given url is not found")

        elif b == "e":
            break

        else:
            print("Entered operation cannot be performed")


if __name__ == "__main__":
    main()
