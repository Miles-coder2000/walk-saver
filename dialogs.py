import flet as ft
import routing


def _close_dialog(page, dlg):
    dlg.open = False
    page.update()

def show_confirm_exit_dialog(page):
    confirm_exit_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Confirmation"),
        content=ft.Text("Do you really want to exit the app?"),
        actions=[
            ft.ElevatedButton("Yes", on_click=lambda _: page.window_destroy()),
            ft.ElevatedButton("No", on_click=lambda _: _close_dialog(page, confirm_exit_dialog)),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        open=True,
    )

    page.dialog = confirm_exit_dialog
    page.update()

def show_required_fields_missing_dialog(page):
    required_fields_missing_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Something is missing"),
        content=ft.Text("All fields must be filled in"),
        actions=[
            ft.ElevatedButton("OK, I'll fill it in", on_click=lambda _: _close_dialog(page, required_fields_missing_dialog))
        ],
        open=True,
    )

    page.dialog = required_fields_missing_dialog
    page.update()

def show_invalid_time_format_dialog(page):
    invalid_time_format_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Invalid time format"),
        content=ft.Text("Please enter whole hours or hours and minutes."),
        actions=[
            ft.ElevatedButton("OK", on_click=lambda _: _close_dialog(page, invalid_time_format_dialog))
        ],
        open=True,
    )

    page.dialog = invalid_time_format_dialog
    page.update()

def show_entry_saved_success_dialog(page):
    entry_saved_success_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Success"),
        content=ft.Text("Everything was saved successfully"),
        actions=[
            ft.ElevatedButton("OK", on_click=lambda _: _close_dialog(page, entry_saved_success_dialog))
        ],
        open=True,
    )

    page.dialog = entry_saved_success_dialog
    page.update()

def show_no_date_picked_dialog(page):
    no_date_picked_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("No date selected"),
        content=ft.Text("Please select a date"),
        actions=[
            ft.ElevatedButton("Go select", on_click=lambda _: _close_dialog(page, no_date_picked_dialog))
        ],
        open=True,
    )

    page.dialog = no_date_picked_dialog
    page.update()

def show_confirm_deleting_records_dialog(page, on_yes_action):
    def on_yes_handler(e):
        on_yes_action()
        _close_dialog(page, confirm_deleting_records_dialog)
        routing.nav_bar.selected_index = 0
        e.page.go("/")

    confirm_deleting_records_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Delete all records?"),
        content=ft.Text("This action will irreversibly delete all records.\nDo you wish to continue?"),
        actions=[
            ft.ElevatedButton("Yes", on_click=on_yes_handler),
            ft.ElevatedButton("No", on_click=lambda _: _close_dialog(page, confirm_deleting_records_dialog)),
        ],
        open=True,
    )

    page.dialog = confirm_deleting_records_dialog
    page.update()
