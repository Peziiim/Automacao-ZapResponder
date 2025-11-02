# Automação de Criação de Grupos e Campanhas no ZapResponder

Este projeto utiliza **Selenium WebDriver** para automatizar o processo de criação de grupos de contatos e agendamento de campanhas na plataforma [ZapResponder](https://app.zapresponder.com.br).

O script realiza as seguintes ações automaticamente:

1. Login na plataforma com credenciais fornecidas.
2. Criação de múltiplos grupos de contatos.
3. Criação e agendamento de campanhas associadas a esses grupos.
4. Seleção de templates e preenchimento do conteúdo da campanha.
5. Definição de horários específicos para disparo.

---

## Pré-requisitos

- Python 3.8+
- Google Chrome instalado
- Chromedriver compatível com a versão do Chrome
- Bibliotecas Python necessárias:

```bash
pip install selenium
```
# Configuração

grupoDeContatos = [
    "teste 20/20 SELENIUM tel2",
    "teste 20/20 SELENIUM tel5"
]

tel = Departamento (com Whatsapp)

horas = [
    "",
    "",
]

email = "SEU_EMAIL_AQUI"
senha = "SUA_SENHA_AQUI"

temp_CLT1 = 'nome do template'
temp_CLT2 = 'nome de outro template'
