import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="/page-1")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="/page-2"),
                dbc.DropdownMenuItem("Page 3", href="/page-3"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="TigerGraph",
    brand_href="#",
    color="#ef6c00",
    dark=False,
)

def get_navbar():
    return navbar