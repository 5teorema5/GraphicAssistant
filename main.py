import flet as ft


class State:
    toggle = True


s = State()


def main(page: ft.Page):
    page.title = "Graphic Assistant"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    data_1 = [
        ft.LineChartData(
            data_points=[
                ft.LineChartDataPoint(0, 0),
                ft.LineChartDataPoint(1, 1),
                ft.LineChartDataPoint(2, 4),
                ft.LineChartDataPoint(3, 9),
                ft.LineChartDataPoint(4, 4),
                ft.LineChartDataPoint(5, 1),
                ft.LineChartDataPoint(6, 0),
            ],
            stroke_width=5,
            color=ft.colors.CYAN,
            curved=True,
            stroke_cap_round=True,
        ),
    ]

    chart = ft.LineChart(
        data_series=data_1,
        border=ft.border.only(left=ft.border.BorderSide(3, ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE)),
                              bottom=ft.border.BorderSide(3, ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE)),
                              right=ft.border.BorderSide(3, ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE)),
                              top=ft.border.BorderSide(3, ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE)),

                              ),
        horizontal_grid_lines=ft.ChartGridLines(
            interval=1, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
        ),
        vertical_grid_lines=ft.ChartGridLines(
            interval=1, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
        ),
        left_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=1,
                    label=ft.Text("1", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=2,
                    label=ft.Text("2", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=9,
                    label=ft.Text("9", size=14, weight=ft.FontWeight.BOLD),
                ),
            ],
            labels_size=20,
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=1,
                    label=ft.Container(
                        ft.Text(
                            "1",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=2,
                    label=ft.Container(
                        ft.Text(
                            "2",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                ft.ChartAxisLabel(
                    value=3,
                    label=ft.Container(
                        ft.Text(
                            "3",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
            ],
            labels_size=32,
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
        min_y=0,
        max_y=10,
        min_x=0,
        max_x=10,
        # animate=5000,
        expand=True,
    )

    def textbox_change_min_x(e):
        chart.min_x = e.control.value
        page.update()

    def textbox_change_max_x(e):
        chart.max_x = e.control.value
        page.update()

    def textbox_change_min_y(e):
        chart.min_y = e.control.value
        page.update()

    def textbox_change_max_y(e):
        chart.max_y = e.control.value
        page.update()

    textbox_min_x = ft.TextField(label='min', value=chart.min_x, width=100, on_change=textbox_change_min_x)
    textbox_max_x = ft.TextField(label='max', value=chart.max_x, width=100, on_change=textbox_change_max_x)
    textbox_min_y = ft.TextField(label='min', value=chart.min_y, width=100, on_change=textbox_change_min_y)
    textbox_max_y = ft.TextField(label='max', value=chart.max_y, width=100, on_change=textbox_change_max_y)

    def minus_click_min_x(e):
        textbox_min_x.value = str(int(textbox_min_x.value) - 1)
        chart.min_x -= 1
        page.update()

    def plus_click_min_x(e):
        textbox_min_x.value = str(int(textbox_min_x.value) + 1)
        chart.min_x += 1
        page.update()

    def minus_click_max_x(e):
        textbox_max_x.value = str(int(textbox_max_x.value) - 1)
        chart.max_x -= 1
        page.update()

    def plus_click_max_x(e):
        textbox_max_x.value = str(int(textbox_max_x.value) + 1)
        chart.max_x += 1
        page.update()

    def minus_click_min_y(e):
        textbox_min_y.value = str(int(textbox_min_y.value) - 1)
        chart.min_y -= 1
        page.update()

    def plus_click_min_y(e):
        textbox_min_y.value = str(int(textbox_min_y.value) + 1)
        chart.min_y += 1
        page.update()

    def minus_click_max_y(e):
        textbox_max_y.value = str(int(textbox_max_y.value) - 1)
        chart.max_y -= 1
        page.update()

    def plus_click_max_y(e):
        textbox_max_y.value = str(int(textbox_max_y.value) + 1)
        chart.max_y += 1
        page.update()

    page.add(
        chart,
        ft.Row(
            [
                ft.Text('axis X:'),
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click_min_x),
                textbox_min_x,
                ft.IconButton(ft.icons.ADD, on_click=plus_click_min_x),
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click_max_x),
                textbox_max_x,
                ft.IconButton(ft.icons.ADD, on_click=plus_click_max_x),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.Text('axis Y:'),
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click_min_y),
                textbox_min_y,
                ft.IconButton(ft.icons.ADD, on_click=plus_click_min_y),
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click_max_y),
                textbox_max_y,
                ft.IconButton(ft.icons.ADD, on_click=plus_click_max_y),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )


ft.app(target=main)
