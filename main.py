import remote_login as rl

from rich import print,box
from datetime import datetime
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.style import Style
from rich.console import Console

console = Console()

grid = Table.grid(expand=True)
grid.add_column(justify="center", ratio=1)
grid.add_column(justify="right")
grid.add_row(
    "Remote System stats",
    datetime.now().ctime().replace(":", "[blink]:[/]"),
)
print(Panel(grid, style="white on blue"))

def fn_menu():

    grid1 = Table(expand=True,border_style="white")
    grid1.add_column("[purple]Choice[purple]",justify="right",style="purple")
    grid1.add_column("[purple]Details[purple]",justify="center",style="purple")
    grid1.add_row(
        "1","free memory"
    )
    grid1.add_row(
        "2","Load Average"
    )
    grid1.add_row(
        "3","Routing Table"
    )
    grid1.add_row(
        "4","Uptime"
    )
    grid1.add_row(
        "5","Exit"
    )
    print(grid1)
    console.print("Enter your choice : ",style="orchid1")

def ram_rich():
    total,used,free,avail = rl.free_mem()
    grid1 = Table(box=box.HORIZONTALS,border_style="bright_red")
    grid1.add_column("[#FFF300]Ram Deatails[#FFF300]",justify="right",style="#FFF300")
    grid1.add_row(
        f"Available RAM : {free}"
    )
    grid1.add_row(
        f"Used RAM : {used}"
    )
    grid1.add_row(
        f"Available : {avail}"
    )
    grid1.add_row(
        f"Total RAM : {total}"
    )
    print(grid1)
    console.print("Enter your choice : ",style="orchid1")
    rl.disconnect()
    choice()

def load_rich():
    ld = rl.Load_avg()
    grid1 = Table(box=box.HORIZONTALS,border_style="bright_red")
    grid1.add_column("[#FFF300]Load Average[#FFF300]",justify="right",style="#FFF300")
    grid1.add_row(
        ld
    )
    print(grid1)
    console.print("Enter your choice : ",style="orchid1")
    rl.disconnect()
    choice()

def rt_rich():
    rt = rl.routing()
    grid1 = Table(box=box.HORIZONTALS,border_style="bright_red")
    grid1.add_column("[#FFF300]Routing Table[#FFF300]",justify="right",style="#FFF300")
    grid1.add_row(
        rt
    )
    print(grid1)
    console.print("Enter your choice : ",style="orchid1")
    rl.disconnect()
    choice()

def up_rich():
    up = rl.uptime()
    grid1 = Table(box=box.HORIZONTALS,border_style="bright_red")
    grid1.add_column("[#FFF300]Uptime status[#FFF300]",justify="right",style="#FFF300")
    grid1.add_row(
        up
    )
    print(grid1)
    console.print("Enter your choice : ",style="orchid1")
    rl.disconnect()
    choice()

def choice():
    fn_menu()
    rl.connect("127.0.0.1","22","wgz","wgz")
    ch = int(input())
    if ch == 1:
        ram_rich()
    elif ch == 2:
        load_rich()
    elif ch == 3:
        rt_rich()
    elif ch == 4:
        up_rich()
    elif ch == 5:
        rl.disconnect()
        exit()
    else:
        print("\n invalid choice")
        choice()

choice()