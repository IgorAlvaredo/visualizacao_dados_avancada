import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc

df = pd.read_csv('../dados/ecommerce_estatistica.csv')

print(df.nunique())

def cria_graficos(df):
    fig1 = px.pie(df, names='Temporada', color='Temporada', hole=0.2,  color_discrete_sequence=px.colors.sequential.RdBu)

    fig2 = px.histogram(df, x='Gênero', nbins=30, title='Distribuição de Gênero')


    fig3 = px.line(df, x='Marca_Freq', y='Material_Freq', color='Temporada', facet_col='Qtd_Vendidos')
    fig3.update_layout(
        title='Salário por Idade e Área de Atuação para cada Nível de Educação',
        xaxis_title='Marca Freq',
        yaxis_title='Material Freq'
    )

    fig4 = px.scatter(df, x='Marca_Freq', y='Material_Freq', size='Preço', color='Nota', hover_name='Temporada', size_max=60)
    fig4.update_layout(title='Salário por Idade e Anos de Experiência')

    fig5 = px.bar(df, x="Marca_Freq", y='Material_Freq', color="Qtd_Vendidos", barmode="group", color_discrete_sequence=px.colors.qualitative.Bold, opacity=1)
    fig5.update_layout(
        title='Salário por Marca Freq e Material Freq',
        xaxis_title='Marca Freq',
        yaxis_title='Material Freq',
        legend_title='Qtd Vendidos',
        plot_bgcolor='rgba(222, 255, 253, 1)', # Fundo interno
        paper_bgcolor='rgba(186, 245, 241, 1)' # Fundo Externo
    )

    fig6 = px.scatter_3d(df, x='Marca_Freq', y='Material_Freq', z='Qtd_Vendidos', color='Temporada')


    return fig1, fig2, fig3, fig4, fig5, fig6

def cria_app(df):
    # criar App
    app = Dash(__name__)

    fig1, fig2, fig3, fig4, fig5, fig6 = cria_graficos(df)

    app.layout = html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4),
        dcc.Graph(figure=fig5),
        dcc.Graph(figure=fig6),
    ])
    return app

if __name__ == '__main__':
    df = pd.read_csv('../dados/ecommerce_estatistica.csv')
    app = cria_app(df)
    # Executa App
    app.run_server(debug=True, port=8050) # Default 8050