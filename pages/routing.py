import tkinter as Tkinter
from tkinter import messagebox
import flet as ft
import webbrowser

##################
# Event Handlers #
##################
def _changing_route(index, e,):
    if index == 0:
        return e.pages.go("/")
    if index == 1:
        return e.pages.go("/new")
    if index == 2:
        return e.pages.go("/statistics")
    if index == 3:
        return show_confirm_exit_dialog()
    if index == 4:
        # Handle the 'support' destination
        show_support_flash_card(e.pages, index)
        pages_changing_route(index, e)
    if index == 5:
        # Handle the 'share' destination
        share_content()

def show_support_flash_card(pages):
    gcash_number = "0956-0367-162"
    return ft.Column(
        controls=[
           ft.ElevatedButton("Button with icon", icon="outlined_card"),
           ft.ElevatedButton(
               text=f"Show some support on our project by sending donation at: {gcash_number}",
               icon="assets/icons/donate.png",
               on_click=lambda _: pages.go("/")
           ), 
        ]
    )

def share_content():
    # Example share functionality
    share_url = "https://www.facebook.com/share"
    
    # Open the share URL in a new browser window
    webbrowser.open(share_url)

def show_confirm_exit_dialog():
    result = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    return result

def pages_changing_route(selected_index, e):
    if show_confirm_exit_dialog():
        e.pages.go()
   


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
