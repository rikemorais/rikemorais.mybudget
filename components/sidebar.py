from pydoc import classname
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd


# ========= Layout ========= #
layout = dbc.Col([
    html.H1("Budget", className="text-primary"),
    html.P("By Henrique Morais", className="text-info"),
    html.Hr(),

    # Profile Section
    dbc.Button(id='botao_avatar',
               children=[
                   html.Img(
                       src='assets/rikemorais.png',
                       id='avatar_change',
                       alt='Avatar',
                       className='perfil_avatar')
               ],
               style={'background-color': 'transparent',
                      'border-color': 'transparent'}),

    # Insertion Section
    dbc.Row([
        dbc.Col([
            dbc.Button(
                color='success',
                id='open_novo-receita',
                children=['Receita']
            )
        ], width=6),
        dbc.Col([
            dbc.Button(
                color='danger',
                id='open_novo-despesa',
                children=['Despesa'])
        ], width=6)
    ]),

    # Navigation Section
    html.Hr(),
    dbc.Nav(
        [
            dbc.NavLink("Dashboard", href="/dashboards", active="exact"),
            dbc.NavLink("Extratos", href="/extratos", active="exact"),
        ],
        vertical=True,
        pills=True,
        id="nav_buttons",
        style={"margin-bottom": "50px"}
    ),
], id='sidebar_completa'
)
# Callbacks
# Pop-up receita
