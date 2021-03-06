import dash_bootstrap_components as dbc
from dash import html


def perfil_principal():
    avatar = dbc.Button(id='botao_avatar',
                        children=[html.Img(src="/assets/rikemorais.png",
                                           id="avatar_change",
                                           alt="Avatar",
                                           className='perfil_avatar'),
                                  ],
                        style={'background-color': 'transparent',
                               'border-color': 'transparent'})
    return avatar
