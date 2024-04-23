import flet as ft
import re
from datetime import datetime
import dialogs
import model
import routing

PATTERN_HOURS_MINUTES = re.compile(r'^([0-9]|1[0-2]|2[0-3]):[0-5][0-9]$')
PATTERN_HOURS = re.compile(r'^(1?[0-9]|2[0-3])$')
_selected_date = None

##################
# Event Handlers #
##################
def _update_date_button(e):
    global _selected_date
    _selected_date = _date_picker.value
    _date_button.text = "{}".format(_selected_date.strftime("%d/%m/%y"))
    e.page.update()

def _validate_time_entry(page, walked_time_entry_value):
    if PATTERN_HOURS_MINUTES.search(walked_time_entry_value):
        hours, minutes = map(int, walked_time_entry_value.split(":"))
        total_time_minutes = hours * 60 + minutes
        return total_time_minutes
    elif PATTERN_HOURS.search(walked_time_entry_value):
        total_time_minutes = int(walked_time_entry_value) * 60
        return total_time_minutes
    else:
        dialogs.show_invalid_time_format_dialog(page)
        return None

def _validate_and_save_entry(page):
    if not all([_walked_time_entry.value, _walked_kms_entry.value, _walked_kcal_entry.value,
                _walked_steps_entry.value]):
        dialogs.show_required_fields_missing_dialog(page)
        return

    if not _selected_date:
        dialogs.show_no_date_picked_dialog(page)
        return

    date = _selected_date
    kms = float(_walked_kms_entry.value)
    time = _validate_time_entry(page, _walked_time_entry.value)
    kcal = int(_walked_kcal_entry.value)
    steps = int(_walked_steps_entry.value)

    if time is None:
        return

    model.save_to_database(date, kms, time, kcal, steps)

    dialogs.show_entry_saved_success_dialog(page)

    _walked_kms_entry.value = ""
    _walked_time_entry.value = ""
    _walked_kcal_entry.value = ""
    _walked_steps_entry.value = ""
    _date_button.text = "Select date"
    _fill_recent_walks_table(page)
    page.update()

def _fill_recent_walks_table(page):
    walks_data = model.get_recent_walks()
    recent_walks = walks_data if walks_data else [("No records", "")]
    _data_table.rows = [
        ft.DataRow(
            [ft.DataCell(ft.Text(date)), ft.DataCell(ft.Text(kms))]
        ) for date, kms in recent_walks]
    page.update()

###########
#  View   #
###########
_new_record_txt = ft.Text(value="\nAdd a record!\n",
                          color=ft.colors.CYAN_900,
                          size=40,
                          theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                          text_align=ft.TextAlign.CENTER)

_data_table = ft.DataTable(
    bgcolor=ft.colors.BLUE_50,
    columns=[
        ft.DataColumn(ft.Text("Date")),
        ft.DataColumn(ft.Text("Kilometers")),
    ],
    rows=[])

_walked_kms_entry = ft.TextField(label="How much did you walk?",
                                 hint_text="km.m",
                                 width=160,
                                 border_radius=0,
                                 input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9.]",
                                                             replacement_string=""),
                                 keyboard_type=ft.KeyboardType.NUMBER)

_walked_time_entry = ft.TextField(label="For how long?",
                                  hint_text="hours:minutes",
                                  width=160,
                                  border_radius=0,
                                  input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9:]",
                                                              replacement_string=""))

_walked_kcal_entry = ft.TextField(label="How many calories?",
                                  width=160,
                                  border_radius=0,
                                  input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]",
                                                              replacement_string=""),
                                  keyboard_type=ft.KeyboardType.NUMBER)

_walked_steps_entry = ft.TextField(label="How many steps?",
                                   width=160,
                                   border_radius=0,
                                   input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]",
                                                               replacement_string=""),
                                   keyboard_type=ft.KeyboardType.NUMBER)

_date_button = ft.ElevatedButton(text="Select date",
                                 icon=ft.icons.CALENDAR_MONTH_ROUNDED,
                                 on_click=lambda _: _date_picker.pick_date())

_date_picker = ft.DatePicker(on_change=_update_date_button,
                             first_date=datetime(2023, 10, 1),
                             last_date=datetime(2030, 12, 31))

###########
#  Route  #
###########
def create_new_entry_view(page):
    if _date_picker not in page.overlay:
        page.overlay.append(_date_picker)
    _fill_recent_walks_table(page)
    view_new = ft.View(
        route="/new",
        bgcolor=ft.colors.BLUE_100,
        padding=0,
        navigation_bar=routing.nav_bar,
        controls=[
            ft.Stack(controls=[
                ft.Image(
                    src="C:/Projects/WalkingApp/WalkingApp/assets/Theme.png",
                    width=page.window_width,
                    height=page.window_height,
                    fit=ft.ImageFit.FILL),
                ft.Container(content=_new_record_txt,
                             top=-10,
                             left=65,
                             height=200,
                             width=270),
                ft.Container(content=_date_button,
                             top=160,
                             right=120),
                ft.Container(content=_walked_kms_entry,
                             top=210,
                             left=35,
                             bgcolor=ft.colors.BLUE_50),
                ft.Container(content=_walked_time_entry,
                             top=210,
                             left=215,
                             bgcolor=ft.colors.BLUE_50),
                ft.Container(content=_walked_kcal_entry,
                             top=290,
                             left=35,
                             bgcolor=ft.colors.BLUE_50),
                ft.Container(content=_walked_steps_entry,
                             top=290,
                             left=215,
                             bgcolor=ft.colors.BLUE_50),
                ft.Container(content=ft.ElevatedButton(text="Save",
                                                       on_click=lambda _: _validate_and_save_entry(page)),
                             top=380,
                             right=150),
                ft.Container(content=_data_table,
                             left=65,
                             top=450),
            ],
                width=page.window_width,
                height=page.window_height - 70)]
    )

    return view_new
