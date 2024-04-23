import flet as ft
import dialogs
import model
import routing

def create_statistics_view(pages):
    """
    Return the view for the '/statistics' route.
    :param page: ft.Page
    """
    total_km, total_time, total_kcal, total_steps = model.calculate_overall_statistics()
    view_statistics = ft.View(
        "/statistics",
        bgcolor=ft.colors.BLUE_100,
        navigation_bar=routing.nav_bar,
        padding=0,
        controls=[
            ft.Stack(controls=[
                ft.Image(
                    src="C:/Projects/WalkingApp/WalkingApp/assets/Theme.png",
                    width=pages.window_width,
                    height=pages.window_height,
                    fit=ft.ImageFit.FILL),
                ft.Container(content=ft.Text(f"{round(total_km) if total_km else 0} Km",
                                             weight=ft.FontWeight.W_600),
                             margin=10,
                             padding=10,
                             alignment=ft.Alignment.CENTER,
                             bgcolor=ft.colors.AMBER,
                             border_radius=90,
                             width=175,
                             height=100,
                             left=100,
                             top=100),
                ft.Container(content=ft.Text(f"{total_time // 60}:{total_time % 60:02}:00 hours." if total_time
                                             else "0 hour.",
                                             weight=ft.FontWeight.W_600),
                             margin=10,
                             padding=10,
                             alignment=ft.Alignment.CENTER,
                             bgcolor=ft.colors.GREEN_200,
                             border_radius=90,
                             width=175,
                             height=100,
                             left=100,
                             top=230),
                ft.Container(content=ft.Text(f"{total_kcal or 0} cal",
                                             weight=ft.FontWeight.W_600),
                             margin=10,
                             padding=10,
                             alignment=ft.Alignment.CENTER,
                             bgcolor=ft.colors.CYAN_200,
                             border_radius=90,
                             width=175,
                             height=100,
                             left=100,
                             top=360),
                ft.Container(content=ft.Text(f"{total_steps or 0} steps",
                                             weight=ft.FontWeight.W_600),
                             margin=10,
                             padding=10,
                             alignment=ft.Alignment.CENTER,
                             bgcolor=ft.colors.RED_200,
                             border_radius=90,
                             width=175,
                             height=100,
                             left=100,
                             top=490),
                ft.Container(content=ft.ElevatedButton(text="Reset",
                                                       on_click=lambda _: dialogs.show_confirm_deleting_records_dialog
                                                       (pages, model.reset_database)),
                             top=650,
                             right=160),
            ],
                width=pages.window_width,
                height=pages.window_height - 70)]
    )

    return view_statistics
