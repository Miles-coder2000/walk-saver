import flet as ft
import dialogs
import statistics_r
import new_entry_r
import home_r

def main(pages: ft.Page):  # Change ft.pages to ft.Page
    pages.title = "Walk Saver"
    pages.padding = 0
    pages.window_width = 400
    pages.window_height = 850
    pages.bgcolor = ft.colors.BLUE_100
    pages.window_resizable = False
    pages.window_maximizable = False
    pages.theme_mode = ft.ThemeMode.LIGHT

    def show_exit_dialog(e):
        if e.data == "close":
            dialogs.show_confirm_exit_dialog(pages)

    pages.window_prevent_close = True
    pages.on_window_event = show_exit_dialog

    def handle_route_change(_):
        """
        Update the views list of the page when the route changes.
        """
        views_list = [home_r.create_home_view(pages)]
        if pages.route == "/new" or pages.route == "/statistics":
            views_list.append(new_entry_r.create_new_entry_view(pages))
        if pages.route == "/statistics":
            views_list.append(pages.statistics_r.create_statistics_view(pages))
        pages.views[:] = views_list
        pages.update()

    pages.on_route_change = handle_route_change
    pages.go(pages.route)


# START OF THE APP
ft.app(target=main)  # Pass the function reference, not the function call
