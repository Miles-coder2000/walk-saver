from tkinter import dialog
import flet as ft
import webbrowser

##################
# Event Handlers #
##################
def _changing_route(index, e):
    if index == 0:
        return e.page.go("/")
    if index == 1:
        return e.page.go("/new")
    if index == 2:
        return e.page.go("/statistics")
    if index == 3:
        return dialog.show_confirm_exit_dialog(e.page)
    if index == 4:
        # Handle the 'support' destination
        show_support_flash_card(e.page)
    if index == 5:
        # Handle the 'share' destination
        share_content()  

def show_support_flash_card(page):
    gcash_number = "0956-0367-162"
    support_flash_card = ft.AlertDialog(
        modal=True,
        title=ft.Text("Support Information"),
        content=ft.Text(f"Please support us by sending your donation to GCash number: {gcash_number}"),
        actions=[
            ft.ElevatedButton("OK", on_click=lambda _: page.close_dialog())
        ],
        open=True,
    )

    page.dialog = support_flash_card
    page.update()

def share_content():
    # Example share functionality
    share_url = "https://www.facebook.com/share"
    
    # Open the share URL in a new browser window
    webbrowser.open(share_url)


###########
#  View   #
###########
nav_bar = ft.NavigationBar(
    bgcolor=ft.colors.BLUE_100,
    on_change=lambda e: _changing_route(e.control.selected_index, e),
    destinations=[
        ft.NavigationDestination(icon=ft.icons.HOME_ROUNDED, label="Home"),
        ft.NavigationDestination(icon=ft.icons.POST_ADD, label="New Entry"),
        ft.NavigationDestination(icon=ft.icons.INSERT_CHART_ROUNDED, label="Statistics"),
        ft.NavigationDestination(icon=ft.icons.LOGOUT, label="Exit"),
        ft.NavigationDestination(icon=ft.icons.SUPPORT, label="Support"),
        ft.NavigationDestination(icon=ft.icons.SHARE, label="Share")
    ])
