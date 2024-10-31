import util.constant as constant
import util.sys_info as sys_info
import subprocess
from typing import Union

LINE = "-" * 25

available_tool_hacking = ["sqlmap"]
package_info = sys_info.show_package_info()


def menu_banner() -> None:
    print(f"{constant.GREEN}{LINE}{constant.RESET}")
    print(f"{constant.RED}\tPhatom{constant.RESET}")
    print(f"{constant.GREEN}{LINE}{constant.RESET}")
    print(
        f"{constant.GREEN}version: {constant.RESET}{constant.BOLD}{constant.VERSION}{constant.RESET}"
    )

    menu_info()


def menu_info() -> None:
    print(f"{constant.NEWLINE}package info: {sys_info.show_package_info()}")
    print(f"{constant.BOLD}1. Available Tool{constant.RESET}")
    print(f"{constant.BOLD}2. Install Tool{constant.RESET}")


def installation(package_name: str) -> Union[list, None]:
    if package_info == "apt":
        command = ["sudo", "apt", "get", "install", package_name, "-y"]
    elif package_info == "pacman":
        command = ["sudo", "pacman", "-S", package_name, "--noconfirm"]
    else:
        print("Unknown Linux Distro")

    try:
        package_install = subprocess.run(command, check=True)
        return package_install
    except subprocess.CalledProcessError:
        print("Error installing package")
        return None


def available_tool() -> None:
    print(f"{constant.NEWLINE}{constant.BOLD}Available Tool{constant.RESET}")
    for number, data in enumerate(available_tool_hacking):
        print(f"{constant.BOLD}{number + 1}.{data}{constant.RESET}")


def install_tool() -> None:
    available_tool()
    input_data = input("enter your choice: ")
    if input_data == "1":
        print("installing sqlmap...")
        installation("sqlmap")


if __name__ == "__main__":
    print(installation())
